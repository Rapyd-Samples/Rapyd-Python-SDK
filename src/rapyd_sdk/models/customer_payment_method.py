from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .category import Category
from .next_action import NextAction


@JsonMap({"id_": "id", "type_": "type"})
class CustomerPaymentMethod(BaseModel):
    """Describes the fields contained in REST messages and webhooks for payment methods saved to a customer profile

    :param category: category, defaults to None
    :type category: Category, optional
    :param fingerprint_token: Hash of the card number, expiration date and CVV. Read-only. Relevant to cards., defaults to None
    :type fingerprint_token: str, optional
    :param id_: ID of the Payment Method object. String starting with card_ or other_, defaults to None
    :type id_: str, optional
    :param image: A URL to the image of the icon for the type of payment method. Response only, defaults to None
    :type image: str, optional
    :param last4: last4 - Last four digits of the card number. Read-only. Relevant to cards, defaults to None
    :type last4: str, optional
    :param metadata: A JSON object defined by the client, defaults to None
    :type metadata: dict, optional
    :param name: The name of the customer, defaults to None
    :type name: str, optional
    :param network_reference_id: Identifier for use in a recurring card payment. In recurring payments, use the network reference ID you got from the response or webhook when adding the payment method to the customer. In the payment_method.fields object, use it in place of the cvv field, along with the other required fields for the card payment method. This field cannot be used together with a payment method ID or a customer ID. Note that for all payments, you must use the network reference ID from adding the payment method to the customer. The response in each subsequent payment contains a different network reference ID, which is not for use in requests. Relevant to clients with PCI certification who have been authorized to use this feature, defaults to None
    :type network_reference_id: str, optional
    :param next_action: Indicates the next action for completing the payment. Response only. One of the following values are - * 3d_verification - The next action is 3DS authentication. To simulate 3DS authentication in the sandbox, see Simulating 3DS Authentication. Relevant only to card payments. * pending_capture - The next action is pending the capture of the amount. Relevant only to card payments when the amount is not zero. * pending_confirmation - The next action is pending the confirmation for the payment. Relevant to all payment methods excluding card payment. * not_applicable - The payment has completed or the next action is not relevant., defaults to None
    :type next_action: NextAction, optional
    :param redirect_url: URL where the customer is redirected for additional steps required for the payment. Response only. To simulate 3DS authentication in the sandbox, see Simulating 3DS Authentication - https://docs.rapyd.net/build-with-rapyd/reference-link/simulating-3ds-authentication, defaults to None
    :type redirect_url: str, optional
    :param supporting_documentation: Reserved. Response only., defaults to None
    :type supporting_documentation: str, optional
    :param token: ID of the token that represents the card. String starting with card_. Relevant to cards. Relevant if the value of is_tokenizable is true for the payment method in the response to List Payment Methods by Country. See Payment Method Type Object at https://docs.rapyd.net/build-with-rapyd/reference-link/payment-method-type-object, defaults to None
    :type token: str, optional
    :param type_: Name of the payment method type. For example, us_mastercard_card. To get a list of payment methods for a country, use List Payment Methods by Country., defaults to None
    :type type_: str, optional
    :param webhook_url: Reserved. Response only, defaults to None
    :type webhook_url: str, optional
    """

    def __init__(
        self,
        category: Category = None,
        fingerprint_token: str = None,
        id_: str = None,
        image: str = None,
        last4: str = None,
        metadata: dict = None,
        name: str = None,
        network_reference_id: str = None,
        next_action: NextAction = None,
        redirect_url: str = None,
        supporting_documentation: str = None,
        token: str = None,
        type_: str = None,
        webhook_url: str = None,
    ):
        """Describes the fields contained in REST messages and webhooks for payment methods saved to a customer profile

        :param category: category, defaults to None
        :type category: Category, optional
        :param fingerprint_token: Hash of the card number, expiration date and CVV. Read-only. Relevant to cards., defaults to None
        :type fingerprint_token: str, optional
        :param id_: ID of the Payment Method object. String starting with card_ or other_, defaults to None
        :type id_: str, optional
        :param image: A URL to the image of the icon for the type of payment method. Response only, defaults to None
        :type image: str, optional
        :param last4: last4 - Last four digits of the card number. Read-only. Relevant to cards, defaults to None
        :type last4: str, optional
        :param metadata: A JSON object defined by the client, defaults to None
        :type metadata: dict, optional
        :param name: The name of the customer, defaults to None
        :type name: str, optional
        :param network_reference_id: Identifier for use in a recurring card payment. In recurring payments, use the network reference ID you got from the response or webhook when adding the payment method to the customer. In the payment_method.fields object, use it in place of the cvv field, along with the other required fields for the card payment method. This field cannot be used together with a payment method ID or a customer ID. Note that for all payments, you must use the network reference ID from adding the payment method to the customer. The response in each subsequent payment contains a different network reference ID, which is not for use in requests. Relevant to clients with PCI certification who have been authorized to use this feature, defaults to None
        :type network_reference_id: str, optional
        :param next_action: Indicates the next action for completing the payment. Response only. One of the following values are - * 3d_verification - The next action is 3DS authentication. To simulate 3DS authentication in the sandbox, see Simulating 3DS Authentication. Relevant only to card payments. * pending_capture - The next action is pending the capture of the amount. Relevant only to card payments when the amount is not zero. * pending_confirmation - The next action is pending the confirmation for the payment. Relevant to all payment methods excluding card payment. * not_applicable - The payment has completed or the next action is not relevant., defaults to None
        :type next_action: NextAction, optional
        :param redirect_url: URL where the customer is redirected for additional steps required for the payment. Response only. To simulate 3DS authentication in the sandbox, see Simulating 3DS Authentication - https://docs.rapyd.net/build-with-rapyd/reference-link/simulating-3ds-authentication, defaults to None
        :type redirect_url: str, optional
        :param supporting_documentation: Reserved. Response only., defaults to None
        :type supporting_documentation: str, optional
        :param token: ID of the token that represents the card. String starting with card_. Relevant to cards. Relevant if the value of is_tokenizable is true for the payment method in the response to List Payment Methods by Country. See Payment Method Type Object at https://docs.rapyd.net/build-with-rapyd/reference-link/payment-method-type-object, defaults to None
        :type token: str, optional
        :param type_: Name of the payment method type. For example, us_mastercard_card. To get a list of payment methods for a country, use List Payment Methods by Country., defaults to None
        :type type_: str, optional
        :param webhook_url: Reserved. Response only, defaults to None
        :type webhook_url: str, optional
        """
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
        )
        self.fingerprint_token = self._define_str(
            "fingerprint_token", fingerprint_token, nullable=True
        )
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.image = self._define_str("image", image, nullable=True)
        self.last4 = self._define_str("last4", last4, nullable=True, pattern="^\d{4}$")
        self.metadata = metadata
        self.name = self._define_str("name", name, nullable=True)
        self.network_reference_id = self._define_str(
            "network_reference_id", network_reference_id, nullable=True
        )
        self.next_action = (
            self._enum_matching(next_action, NextAction.list(), "next_action")
            if next_action
            else None
        )
        self.redirect_url = self._define_str(
            "redirect_url", redirect_url, nullable=True
        )
        self.supporting_documentation = self._define_str(
            "supporting_documentation", supporting_documentation, nullable=True
        )
        self.token = self._define_str("token", token, nullable=True)
        self.type_ = self._define_str("type_", type_, nullable=True)
        self.webhook_url = self._define_str("webhook_url", webhook_url, nullable=True)
