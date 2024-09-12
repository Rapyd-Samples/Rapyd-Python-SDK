from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.v1_payouts_body import V1PayoutsBody
from ..models.utils.cast_models import cast_models
from ..models.payouts_sender_body import PayoutsSenderBody
from ..models.payouts_payout_id_body import PayoutsPayoutIdBody
from ..models.payouts_beneficiary_body import PayoutsBeneficiaryBody
from ..models.inline_response_200_18 import InlineResponse200_18
from ..models.inline_response_200_17 import InlineResponse200_17
from ..models.inline_response_200_16 import InlineResponse200_16
from ..models.inline_response_200_15 import InlineResponse200_15
from ..models.inline_response_200_14 import InlineResponse200_14
from ..models.inline_response_200_13 import InlineResponse200_13
from ..models.inline_response_200_12 import InlineResponse200_12
from ..models.inline_response_200_11 import InlineResponse200_11
from ..models.inline_response_200_10 import InlineResponse200_10
from ..models.beneficiary_validate_body import BeneficiaryValidateBody


class DisburseService(BaseService):

    @cast_models
    def get_payout_method_types_details(
        self,
        pomt: str,
        beneficiary_country: str,
        beneficiary_entity_type: str,
        payout_amount: float,
        payout_currency: str,
        sender_country: str,
        sender_currency: str,
        sender_entity_type: str,
    ) -> InlineResponse200_10:
        """Retrieve the fields required to use a payout method type. The fields are returned as an array of objects. The name of each field appears in the name field of each object. Use this information for Create Payout, Create Beneficiary and Create Sender.
         Note: The fields returned by this method are required when you create a payout. If you create a payout with a sender or beneficiary that was created previously, you are responsible for choosing a sender and beneficiary that have all the fields required by the payout method.

        :param pomt: The type of the payout method. Set to the name of a payout method listed in the response to List Payout Method Types. The two-letter prefix must match the beneficiary country code.
        :type pomt: str
        :param beneficiary_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase.
        :type beneficiary_country: str
        :param beneficiary_entity_type: Type of entity for the beneficiary. One of the following, individual, company
        :type beneficiary_entity_type: str
        :param payout_amount: Amount of the payout, in units of the currency that the beneficiary is receiving. Decimal.
        :type payout_amount: float
        :param payout_currency: Currency received by the beneficiary. Three-letter ISO 4217 code. Uppercase.
        :type payout_currency: str
        :param sender_country: Country of the sender. Two-letter ISO 3166-1 ALPHA-2 code. Uppercase.
        :type sender_country: str
        :param sender_currency: Currency that the sender is paying with. Three-letter ISO 4217 code. Uppercase.
        :type sender_currency: str
        :param sender_entity_type: Type of entity for the sender. One of the following: individual, company
        :type sender_entity_type: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: payout method types details fetched successfuly
        :rtype: InlineResponse200_10
        """

        Validator(str).validate(pomt)
        Validator(str).validate(beneficiary_country)
        Validator(str).validate(beneficiary_entity_type)
        Validator(float).validate(payout_amount)
        Validator(str).validate(payout_currency)
        Validator(str).validate(sender_country)
        Validator(str).validate(sender_currency)
        Validator(str).validate(sender_entity_type)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payout_methods/{{pomt}}/required_fields",
                self.get_default_headers(),
            )
            .add_path("pomt", pomt, explode=True)
            .add_query("beneficiary_country", beneficiary_country)
            .add_query("beneficiary_entity_type", beneficiary_entity_type)
            .add_query("payout_amount", payout_amount)
            .add_query("payout_currency", payout_currency)
            .add_query("sender_country", sender_country)
            .add_query("sender_currency", sender_currency)
            .add_query("sender_entity_type", sender_entity_type)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_10._unmap(response)

    @cast_models
    def list_payouts(
        self,
        beneficiary: str = None,
        created_after: str = None,
        created_before: str = None,
        ending_before: str = None,
        ewallet: str = None,
        limit: str = None,
        merchant_reference_id: str = None,
        payout_method_type: str = None,
        sender: str = None,
        sender_country: str = None,
        sender_currency: str = None,
        starting_after: str = None,
    ) -> InlineResponse200_11:
        """Retrieve a list of payouts that you created.

        :param beneficiary: Filters according to the beneficiary ID. String starting with beneficiary_., defaults to None
        :type beneficiary: str, optional
        :param created_after: The ID of the payout created before the first payout you want to retrieve. String starting with payout_., defaults to None
        :type created_after: str, optional
        :param created_before: The ID of the payout created after the last payout you want to retrieve. String starting with payout_., defaults to None
        :type created_before: str, optional
        :param ending_before: The ID of a payout in the list. The list ends with the payout that was created before the payout with this ID. Use this filter to get the previous page of results. String starting with payout_. Deprecated., defaults to None
        :type ending_before: str, optional
        :param ewallet: Filters according to the wallet ID. String starting with ewallet_., defaults to None
        :type ewallet: str, optional
        :param limit: The maximum number of payouts to return. Range: 1-100. Default is 10., defaults to None
        :type limit: str, optional
        :param merchant_reference_id: Filters according to the merchant reference ID., defaults to None
        :type merchant_reference_id: str, optional
        :param payout_method_type: Filters according to the type of payout method. The two-letter prefix must match the beneficiary country code., defaults to None
        :type payout_method_type: str, optional
        :param sender: Filters according to the sender ID. String starting with sender_., defaults to None
        :type sender: str, optional
        :param sender_country: Filters according to the country of the sender. Two-letter ISO 3166-1 ALPHA-2 code., defaults to None
        :type sender_country: str, optional
        :param sender_currency: Filters according to the currency that the sender is paying with. Three-letter ISO 4217 code., defaults to None
        :type sender_currency: str, optional
        :param starting_after: The ID of a payout in the list. The list begins with the payout that was created next after the payout with this ID. Use this filter to get the next page of results. Relevant when ending_before is not used. String starting with payout_. Deprecated, defaults to None
        :type starting_after: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Payouts Fetched Successfuly
        :rtype: InlineResponse200_11
        """

        Validator(str).is_optional().validate(beneficiary)
        Validator(str).is_optional().validate(created_after)
        Validator(str).is_optional().validate(created_before)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(ewallet)
        Validator(str).is_optional().validate(limit)
        Validator(str).is_optional().validate(merchant_reference_id)
        Validator(str).is_optional().validate(payout_method_type)
        Validator(str).is_optional().validate(sender)
        Validator(str).is_optional().pattern(
            "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$"
        ).validate(sender_country)
        Validator(str).is_optional().pattern(
            "/^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$/"
        ).validate(sender_currency)
        Validator(str).is_optional().validate(starting_after)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/payouts", self.get_default_headers())
            .add_query("beneficiary", beneficiary)
            .add_query("created_after", created_after)
            .add_query("created_before", created_before)
            .add_query("ending_before", ending_before)
            .add_query("ewallet", ewallet)
            .add_query("limit", limit)
            .add_query("merchant_reference_id", merchant_reference_id)
            .add_query("payout_method_type", payout_method_type)
            .add_query("sender", sender)
            .add_query("sender_country", sender_country)
            .add_query("sender_currency", sender_currency)
            .add_query("starting_after", starting_after)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_11._unmap(response)

    @cast_models
    def create_payout(self, request_body: V1PayoutsBody) -> InlineResponse200_12:
        """Create a payout (disbursement). This method triggers the Payout Created webhook. This webhook contains the same information as the response. If the action of a third party is not required, the Payout Completed webhook is also triggered.

        :param request_body: The request body.
        :type request_body: V1PayoutsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: payout created successfuly
        :rtype: InlineResponse200_12
        """

        Validator(V1PayoutsBody).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/payouts", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_12._unmap(response)

    @cast_models
    def create_beneficiary(
        self, request_body: PayoutsBeneficiaryBody
    ) -> InlineResponse200_13:
        """Create a beneficiary for use in payouts.
        The response provides a unique beneficiary ID, which you can use in place of the Beneficiary object for Create Payout.
        This method triggers the Beneficiary Created webhook. This webhook contains the same information as the response.
        Note: In addition to the required fields documented below, you must include all other beneficiary fields listed in the response to Get Payout Required Fields, and you must conform to the regex provided.
        To create a beneficiary that you can use with multiple payout methods, include all fields that are required by each payout method.
        The client is responsible for including all required fields.

        :param request_body: The request body.
        :type request_body: PayoutsBeneficiaryBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Beneficiary Created Successfully
        :rtype: InlineResponse200_13
        """

        Validator(PayoutsBeneficiaryBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payouts/beneficiary", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_13._unmap(response)

    @cast_models
    def validate_beneficiary(
        self, request_body: BeneficiaryValidateBody
    ) -> InlineResponse200_14:
        """Validate the format of the details for a payout beneficiary. You can validate a beneficiary multiple times for different payout methods. You can enter a Beneficiary object or a previously created beneficiary ID.
         Note: In addition to the required fields for Create Beneficiary, the Beneficiary object must include all required fields for the beneficiary listed in the response to Get Payout Required Fields. The examples include additional fields for the 'us_ach_bank' payout method.

        :param request_body: The request body.
        :type request_body: BeneficiaryValidateBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Beneficiary validated successfuly
        :rtype: InlineResponse200_14
        """

        Validator(BeneficiaryValidateBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payouts/beneficiary/validate",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_14._unmap(response)

    @cast_models
    def get_beneficiary(self, beneficiary_id: str) -> InlineResponse200_13:
        """Retrieve details of a payout beneficiary.
         Note: The 'Retrieve Beneficiary - individual' response includes additional fields for the 'ca_general_bank' payout method. The 'Retrieve Beneficiary - company' response includes additional fields for the 'us_ach_bank' payout method.

        :param beneficiary_id: ID of the 'beneficiary' object. String starting with beneficiary_.
        :type beneficiary_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Beneficiary retrieved successfuly
        :rtype: InlineResponse200_13
        """

        Validator(str).validate(beneficiary_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payouts/beneficiary/{{beneficiaryId}}",
                self.get_default_headers(),
            )
            .add_path("beneficiaryId", beneficiary_id, explode=True)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_13._unmap(response)

    @cast_models
    def delete_beneficiary(self, beneficiary_id: str) -> InlineResponse200_15:
        """Delete a payout beneficiary from the Rapyd platform.

        :param beneficiary_id: ID of the 'beneficiary' object. String starting with beneficiary_.
        :type beneficiary_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Beneficiary deleted successfuly
        :rtype: InlineResponse200_15
        """

        Validator(str).validate(beneficiary_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payouts/beneficiary/{{beneficiaryId}}",
                self.get_default_headers(),
            )
            .add_path("beneficiaryId", beneficiary_id, explode=True)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_15._unmap(response)

    @cast_models
    def simulate_complete_payout(
        self, payout_token: str, amount: str
    ) -> InlineResponse200_12:
        """simulate_complete_payout

        :param payout_token: ID of the payout. String starting with 'payout_'.
        :type payout_token: str
        :param amount: The payout amount. Decimal, including the correct number of decimal places for the currency exponent, as defined in ISO 2417:2015.
        :type amount: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The 'Retrieve Sender - individual' response includes additional fields for the 'ca_general_bank' payout method. The 'Retrieve Sender - company' response includes an additional field for the 'us_ach_bank' payout method.
        :rtype: InlineResponse200_12
        """

        Validator(str).validate(payout_token)
        Validator(str).validate(amount)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payouts/complete/{{payoutToken}}/{{amount}}",
                self.get_default_headers(),
            )
            .add_path("payoutToken", payout_token, explode=True)
            .add_path("amount", amount, explode=True)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_12._unmap(response)

    @cast_models
    def confirm_payout(self, payout_token: str) -> InlineResponse200_12:
        """confirm_payout

        :param payout_token: ID of the payout. String starting with 'payout_'.
        :type payout_token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The 'Retrieve Sender - individual' response includes additional fields for the 'ca_general_bank' payout method. The 'Retrieve Sender - company' response includes an additional field for the 'us_ach_bank' payout method.
        :rtype: InlineResponse200_12
        """

        Validator(str).validate(payout_token)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payouts/confirm/{{payoutToken}}",
                self.get_default_headers(),
            )
            .add_path("payoutToken", payout_token, explode=True)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_12._unmap(response)

    @cast_models
    def create_sender(self, request_body: PayoutsSenderBody) -> InlineResponse200_16:
        """Create a sender for use in payouts.
        The response provides a unique sender ID, which you can use in place of the sender object for Create Payout.
        Note: In addition to the required fields documented below, you must include all other sender fields listed in the response to Get Payout Required Fields, and you must conform to the regex provided.
        To create a sender that you can use with multiple payout methods, include all fields that are required by each payout method.
        The client is responsible for including all required fields.

        :param request_body: The request body.
        :type request_body: PayoutsSenderBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Sender Created Successfully.
        :rtype: InlineResponse200_16
        """

        Validator(PayoutsSenderBody).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/payouts/sender", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_16._unmap(response)

    @cast_models
    def get_payer(self, sender_id: str) -> InlineResponse200_16:
        """Note: The Retrieve Sender - individual response includes additional fields for the ca_general_bank payout method. The Retrieve Sender - company response includes an additional field for the us_ach_bank payout method.

        :param sender_id: ID of the Sender object. String starting with 'sender_'.
        :type sender_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The 'Retrieve Sender - individual' response includes additional fields for the 'ca_general_bank' payout method. The 'Retrieve Sender - company' response includes an additional field for the 'us_ach_bank' payout method.
        :rtype: InlineResponse200_16
        """

        Validator(str).validate(sender_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payouts/sender/{{senderId}}",
                self.get_default_headers(),
            )
            .add_path("senderId", sender_id, explode=True)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_16._unmap(response)

    @cast_models
    def delete_payer(self, sender_id: str) -> InlineResponse200_17:
        """Delete a payout sender from the Rapyd platform.

        :param sender_id: ID of the 'sender' object. String starting with sender_.
        :type sender_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Sender deleted successfuly
        :rtype: InlineResponse200_17
        """

        Validator(str).validate(sender_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payouts/sender/{{senderId}}",
                self.get_default_headers(),
            )
            .add_path("senderId", sender_id, explode=True)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_17._unmap(response)

    @cast_models
    def get_payout_method_types(
        self,
        sender_entity_type: str = None,
        beneficiary_country: str = None,
        payout_currency: str = None,
        sender_currency: str = None,
        sender_country: str = None,
        beneficiary_entity_type: str = None,
        category: str = None,
        is_cancelable: bool = None,
        is_location_specific: bool = None,
        is_expirable: bool = None,
        starting_after: str = None,
        ending_before: str = None,
        limit: str = None,
    ) -> InlineResponse200_18:
        """Retrieve a list of payout method types that you can use when creating a payout. The response contains a list of objects. Each object includes a payout method type and its attributes.

        :param sender_entity_type: Filters the type of entity for the payer. One of the following: individual, company, defaults to None
        :type sender_entity_type: str, optional
        :param beneficiary_country: Country of the beneficiary. Two-letter ISO 3166-1 ALPHA-2 code., defaults to None
        :type beneficiary_country: str, optional
        :param payout_currency: Currency received by the beneficiary. Three-letter ISO 4217 code., defaults to None
        :type payout_currency: str, optional
        :param sender_currency: Currency that the sender is paying with. Three-letter ISO 4217 code., defaults to None
        :type sender_currency: str, optional
        :param sender_country: Country of the sender. Two-letter ISO 3166-1 ALPHA-2 code. Note: This field does not appear in the response., defaults to None
        :type sender_country: str, optional
        :param beneficiary_entity_type: Filters the type of entity for the beneficiary. One of the following: individual, company, defaults to None
        :type beneficiary_entity_type: str, optional
        :param category: The category of payout method. One of the following: bank, card, cash, rapyd_ewallet, ewallet, defaults to None
        :type category: str, optional
        :param is_cancelable: Indicates whether the payout can be canceled. Relevant when category is cash., defaults to None
        :type is_cancelable: bool, optional
        :param is_location_specific: Indicates whether the payout must be made at a specific physical location. Relevant when category is cash., defaults to None
        :type is_location_specific: bool, optional
        :param is_expirable: Indicates whether the payout expires if not completed. Relevant when category is cash., defaults to None
        :type is_expirable: bool, optional
        :param starting_after: The name of a payout method in the list. The list begins with the record that was created next after the record with this payout method. Use this filter to get the next page of results. Relevant when ending_before is not used., defaults to None
        :type starting_after: str, optional
        :param ending_before: The name of a payout method in the list. The list ends with the last record that was created before the record with this payout method. Use this filter to get the previous page of results., defaults to None
        :type ending_before: str, optional
        :param limit: The maximum number of payout methods to return. Range: 1-100. Default is 10., defaults to None
        :type limit: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: payout method types fetched successfuly
        :rtype: InlineResponse200_18
        """

        Validator(str).is_optional().validate(sender_entity_type)
        Validator(str).is_optional().validate(beneficiary_country)
        Validator(str).is_optional().validate(payout_currency)
        Validator(str).is_optional().validate(sender_currency)
        Validator(str).is_optional().validate(sender_country)
        Validator(str).is_optional().validate(beneficiary_entity_type)
        Validator(str).is_optional().validate(category)
        Validator(bool).is_optional().validate(is_cancelable)
        Validator(bool).is_optional().validate(is_location_specific)
        Validator(bool).is_optional().validate(is_expirable)
        Validator(str).is_optional().validate(starting_after)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(limit)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/payout_methods", self.get_default_headers())
            .add_query("sender_entity_type", sender_entity_type)
            .add_query("beneficiary_country", beneficiary_country)
            .add_query("payout_currency", payout_currency)
            .add_query("sender_currency", sender_currency)
            .add_query("sender_country", sender_country)
            .add_query("beneficiary_entity_type", beneficiary_entity_type)
            .add_query("category", category)
            .add_query("is_cancelable", is_cancelable)
            .add_query("is_location_specific", is_location_specific)
            .add_query("is_expirable", is_expirable)
            .add_query("starting_after", starting_after)
            .add_query("ending_before", ending_before)
            .add_query("limit", limit)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_18._unmap(response)

    @cast_models
    def get_payout(self, payout_id: str) -> InlineResponse200_12:
        """Retrieve the details of a payout.

        :param payout_id: ID of the payout. String starting with 'payout_'.
        :type payout_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Payout object
        :rtype: InlineResponse200_12
        """

        Validator(str).validate(payout_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payouts/{{payoutId}}", self.get_default_headers()
            )
            .add_path("payoutId", payout_id, explode=True)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_12._unmap(response)

    @cast_models
    def update_payout(
        self, request_body: PayoutsPayoutIdBody, payout_id: str
    ) -> InlineResponse200_12:
        """Change or modify a payout. This method triggers the Payout Updated webhook. This webhook contains the same information as the response.

        :param request_body: The request body.
        :type request_body: PayoutsPayoutIdBody
        :param payout_id: ID of the payout. String starting with payout_.
        :type payout_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: payout updated successfuly
        :rtype: InlineResponse200_12
        """

        Validator(PayoutsPayoutIdBody).validate(request_body)
        Validator(str).validate(payout_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payouts/{{payoutId}}", self.get_default_headers()
            )
            .add_path("payoutId", payout_id, explode=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_12._unmap(response)

    @cast_models
    def cancel_payout(self, payout_id: str) -> InlineResponse200_12:
        """The payout can be canceled unless its status is confirmation or completed.
        This method triggers the Payout Canceled webhook. This webhook contains the same information as the response.

        :param payout_id: ID of the payout. String starting with payout_.
        :type payout_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: payout canceled successfuly
        :rtype: InlineResponse200_12
        """

        Validator(str).validate(payout_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/payouts/{{payoutId}}", self.get_default_headers()
            )
            .add_path("payoutId", payout_id, explode=True)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_12._unmap(response)
