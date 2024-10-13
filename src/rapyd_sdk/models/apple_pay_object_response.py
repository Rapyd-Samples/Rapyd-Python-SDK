from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "domain_name": "domainName",
        "epoch_timestamp": "epochTimestamp",
        "expires_at": "expiresAt",
        "merchant_identifier": "merchantIdentifier",
        "merchant_session_identifier": "merchantSessionIdentifier",
    }
)
class ApplePayObjectResponse(BaseModel):
    """ApplePayObjectResponse

    :param display_name: The canonical name for the client's business, suitable for display. 64 or fewer UTF-8 characters. Relevant to Apple Pay., defaults to None
    :type display_name: str, optional
    :param domain_name: The domain name of the client's ecommerce site., defaults to None
    :type domain_name: str, optional
    :param epoch_timestamp: Time of creation of the Apple Pay session, in Unix time., defaults to None
    :type epoch_timestamp: float, optional
    :param expires_at: Time of expiration of the Apple Pay session, in Unix time., defaults to None
    :type expires_at: float, optional
    :param merchant_identifier: Your Apple Pay merchant ID., defaults to None
    :type merchant_identifier: str, optional
    :param merchant_session_identifier: Your Apple Pay session ID., defaults to None
    :type merchant_session_identifier: str, optional
    :param nonce: A string that uniquely identifies each call to Apple Pay., defaults to None
    :type nonce: str, optional
    :param retries: The number of previous attempts to get an Apple Pay Session object., defaults to None
    :type retries: float, optional
    :param signature: Digital signature that validates the authenticity and integrity of a digital wallet payment., defaults to None
    :type signature: str, optional
    """

    def __init__(
        self,
        display_name: str = None,
        domain_name: str = None,
        epoch_timestamp: float = None,
        expires_at: float = None,
        merchant_identifier: str = None,
        merchant_session_identifier: str = None,
        nonce: str = None,
        retries: float = None,
        signature: str = None,
    ):
        """ApplePayObjectResponse

        :param display_name: The canonical name for the client's business, suitable for display. 64 or fewer UTF-8 characters. Relevant to Apple Pay., defaults to None
        :type display_name: str, optional
        :param domain_name: The domain name of the client's ecommerce site., defaults to None
        :type domain_name: str, optional
        :param epoch_timestamp: Time of creation of the Apple Pay session, in Unix time., defaults to None
        :type epoch_timestamp: float, optional
        :param expires_at: Time of expiration of the Apple Pay session, in Unix time., defaults to None
        :type expires_at: float, optional
        :param merchant_identifier: Your Apple Pay merchant ID., defaults to None
        :type merchant_identifier: str, optional
        :param merchant_session_identifier: Your Apple Pay session ID., defaults to None
        :type merchant_session_identifier: str, optional
        :param nonce: A string that uniquely identifies each call to Apple Pay., defaults to None
        :type nonce: str, optional
        :param retries: The number of previous attempts to get an Apple Pay Session object., defaults to None
        :type retries: float, optional
        :param signature: Digital signature that validates the authenticity and integrity of a digital wallet payment., defaults to None
        :type signature: str, optional
        """
        self.display_name = self._define_str(
            "display_name", display_name, nullable=True
        )
        self.domain_name = self._define_str("domain_name", domain_name, nullable=True)
        self.epoch_timestamp = self._define_number(
            "epoch_timestamp", epoch_timestamp, nullable=True
        )
        self.expires_at = self._define_number("expires_at", expires_at, nullable=True)
        self.merchant_identifier = self._define_str(
            "merchant_identifier", merchant_identifier, nullable=True
        )
        self.merchant_session_identifier = self._define_str(
            "merchant_session_identifier", merchant_session_identifier, nullable=True
        )
        self.nonce = self._define_str("nonce", nonce, nullable=True)
        self.retries = self._define_number("retries", retries, nullable=True)
        self.signature = self._define_str("signature", signature, nullable=True)
