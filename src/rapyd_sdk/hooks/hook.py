import hashlib
import base64
import os
import urllib.parse
from datetime import datetime
import string
from random import *
import hmac
import json
import time
from decimal import Decimal


def remove_trailing_zeros(value):
    if isinstance(value, float):
        return str(Decimal(value).normalize())
    elif isinstance(value, dict):
        return {k: remove_trailing_zeros(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [remove_trailing_zeros(v) for v in value]
    else:
        return value


# salt: randomly generated for each request.
def generate_salt(length=12):
    return "".join(sample(string.ascii_letters + string.digits, length))


# Current Unix time (seconds).
def get_unix_time(days=0, hours=0, minutes=0, seconds=0):
    return int(time.time())


def update_timestamp_salt_sig(access_key, secret_key, http_method, path, body):
    if path.startswith("http"):
        path = path[path.find(f"/v1") :]

    salt = generate_salt()
    timestamp = get_unix_time()
    to_sign = (http_method, path, salt, str(timestamp), access_key, secret_key, body)

    h = hmac.new(
        secret_key.encode("utf-8"), "".join(to_sign).encode("utf-8"), hashlib.sha256
    )
    signature = base64.urlsafe_b64encode(str.encode(h.hexdigest()))
    return salt, timestamp, signature


def current_sig_headers(access_key, salt, timestamp, signature):
    sig_headers = {
        "access_key": access_key,
        "salt": salt,
        "timestamp": str(timestamp),
        "signature": signature,
        "idempotency": str(get_unix_time()) + salt,
    }
    return sig_headers


# http_method = get|put|post|delete - must be lowercase
# path = Portion after the base URL.
# body = JSON body with no whitespace except in strings.
def pre_call(access_key, secret_key, http_method, path, body=None):
    str_body = (
        json.dumps(body, separators=(",", ":"), ensure_ascii=False) if body else ""
    )
    salt, timestamp, signature = update_timestamp_salt_sig(
        access_key=access_key,
        secret_key=secret_key,
        http_method=http_method,
        path=path,
        body=str_body,
    )
    return str_body.encode("utf-8"), salt, timestamp, signature


def create_headers(access_key, secret_key, http_method, url, body=None):
    body, salt, timestamp, signature = pre_call(
        access_key=access_key,
        secret_key=secret_key,
        http_method=http_method,
        path=url,
        body=body,
    )
    return body, current_sig_headers(access_key, salt, timestamp, signature)


def get_keys(base_url):
    access_key = os.environ["ACCESS_KEY"]
    secret_key = os.environ["SECRET_KEY"]
    return access_key, secret_key


class Request:
    def __init__(self, method, url, headers, body=""):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"method={self.method}, url={self.url}, headers={self.headers}, body={self.body})"


class Response:
    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body

    def __str__(self):
        return "Response(status={}, headers={}, body={})".format(
            self.status, self.headers, self.body
        )


class CustomHook:
    def before_request(self, request: Request):
        parsed = urllib.parse.urlparse(request.url)

        http_method = (
            f"{request.method}".lower()
        )  # get|put|post|delete - must be lowercase
        base_url = (
            f"{parsed.scheme}://{parsed.hostname}"  # base url without query string
        )
        request.body = remove_trailing_zeros(request.body)
        access_key, secret_key = get_keys(base_url)
        body, headers = create_headers(
            access_key, secret_key, http_method, request.url, request.body
        )

        request.headers = dict(request.headers, **headers)

    def after_response(self, request: Request, response: Response):
        print("after_response")

    def on_error(self, error: Exception, request: Request, response: Response):
        print("on_error")
