from __future__ import annotations
from enum import Enum
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .Status import Status
from .HostedPageStatus import HostedPageStatus


class RequestType1(Enum):
    STORE = "store"
    VERIFY = "verify"

    def list():
        return list(map(lambda x: x.value, RequestType1._member_map_.values()))


@JsonMap({})
class MerchantCustomerSupport1(BaseModel):
    def __init__(self, email: str = None, url: str = None, phone_number: str = None):
        self.email = email
        self.url = url
        self.phone_number = phone_number


@JsonMap({})
class Data9(BaseModel):
    def __init__(
        self,
        id: str = None,
        reference_id: str = None,
        wallet: str = None,
        contact: str = None,
        country: str = None,
        request_type: RequestType1 = None,
        force_camera: bool = None,
        document_type: str = None,
        status: HostedPageStatus = None,
        complete_url: str = None,
        org_id: str = None,
        merchant_color: str = None,
        merchant_logo: str = None,
        merchant_website: str = None,
        merchant_customer_support: MerchantCustomerSupport1 = None,
        merchant_alias: str = None,
        merchant_terms: str = None,
        merchant_privacy_policy: str = None,
        page_expiration: float = None,
        redirect_url: str = None,
        cancel_url: str = None,
        language: str = None,
    ):
        self.id = id
        self.reference_id = reference_id
        self.wallet = wallet
        self.contact = contact
        self.country = country
        self.request_type = (
            self._enum_matching(request_type, RequestType1.list(), "request_type")
            if request_type
            else None
        )
        self.force_camera = force_camera
        self.document_type = document_type
        self.status = (
            self._enum_matching(status, HostedPageStatus.list(), "status")
            if status
            else None
        )
        self.complete_url = complete_url
        self.org_id = org_id
        self.merchant_color = merchant_color
        self.merchant_logo = merchant_logo
        self.merchant_website = merchant_website
        self.merchant_customer_support = self._define_object(
            merchant_customer_support, MerchantCustomerSupport1
        )
        self.merchant_alias = merchant_alias
        self.merchant_terms = merchant_terms
        self.merchant_privacy_policy = merchant_privacy_policy
        self.page_expiration = page_expiration
        self.redirect_url = redirect_url
        self.cancel_url = cancel_url
        self.language = language


@JsonMap({})
class GenerateIdvPage200Response(BaseModel):
    def __init__(self, data: Data9 = None, status: Status = None):
        self.data = self._define_object(data, Data9)
        self.status = self._define_object(status, Status)
