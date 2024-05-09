from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GetCountries200Response import (
    GetCountries200Response as GetCountries200ResponseModel,
)
from ..models.GetCurrencies200Response import (
    GetCurrencies200Response as GetCurrencies200ResponseModel,
)
from ..models.GetDailyRate200Response import (
    GetDailyRate200Response as GetDailyRate200ResponseModel,
)
from ..models.GetWebhooks200Response import (
    GetWebhooks200Response as GetWebhooks200ResponseModel,
)
from ..models.GetWebhookByToken200Response import (
    GetWebhookByToken200Response as GetWebhookByToken200ResponseModel,
)
from ..models.ResendWebhookByToken200Response import (
    ResendWebhookByToken200Response as ResendWebhookByToken200ResponseModel,
)


class GeneralResources(BaseService):
    def get_countries(self) -> GetCountries200ResponseModel:
        """
        List Countries
        """

        url_endpoint = "/v1/data/countries"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetCountries200ResponseModel._unmap(res)
        return res

    def get_currencies(self) -> GetCurrencies200ResponseModel:
        """
        List Currencies
        """

        url_endpoint = "/v1/data/currencies"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetCurrencies200ResponseModel._unmap(res)
        return res

    def get_daily_rate(
        self,
        sell_currency: str,
        buy_currency: str,
        action_type: str,
        amount: float = None,
        date_: str = None,
        fixed_side: str = None,
    ) -> GetDailyRate200ResponseModel:
        """
        Resource Methods
        Parameters:
        ----------
            action_type: str
                Determines the type of transaction that the currency exchange applies to. One of the following - payment, payout
            amount: float
                Amount of the currency exchange transaction, in units of the fixed-side currency in Decimal.
            buy_currency: str
                Defines the currency purchased in the currency exchange transaction. Three-letter ISO 4217 code in Uppercase.
            date_: str
                The date when the rate is applicable. Today or earlier. Format YYYY-MM-DD
            fixed_side: str
                Indicates whether the rate is fixed for the currency defined by buy_currency or sell_currency. One of the following - buy, sell.
            sell_currency: str
                Defines the currency sold in the currency exchange transaction. Three-letter ISO 4217 code in Uppercase.
        """

        url_endpoint = "/v1/rates/daily"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not action_type:
            raise ValueError(
                "Parameter action_type is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", True, "action_type", action_type)
        )
        if amount:
            query_params.append(
                query_serializer.serialize_query("form", True, "amount", amount)
            )
        if not buy_currency:
            raise ValueError(
                "Parameter buy_currency is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", True, "buy_currency", buy_currency)
        )
        if date_:
            query_params.append(
                query_serializer.serialize_query("form", True, "date", date_)
            )
        if fixed_side:
            query_params.append(
                query_serializer.serialize_query("form", True, "fixed_side", fixed_side)
            )
        if not sell_currency:
            raise ValueError(
                "Parameter sell_currency is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", True, "sell_currency", sell_currency
            )
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetDailyRate200ResponseModel._unmap(res)
        return res

    def get_webhooks(
        self,
        from_created_at: float = None,
        limit: str = None,
        page: float = None,
        status: str = None,
        type_: str = None,
        to_created_at: float = None,
    ) -> GetWebhooks200ResponseModel:
        """
        List Webhooks.
        Parameters:
        ----------
            from_created_at: float
                The earliest date and time when the object was created, in Unix time (seconds).
            limit: str
                The maximum number of objects to return. Range: 1-1000.
            page: float
                Page number for pagination.
            status: str
                The status of the webhook. One of the following values: *NEW - The webhook was created and has not yet been sent successfully. *RET - The webhook was resent. *CLO - The webhook was sent successfully. *ERR - Attempts were made to send the webhook, but the maximum number of retries was reached. The automatic retry process failed. The webhook was not sent.
            type_: str
                The type of webhook.
            to_created_at: float
                The latest date and time when the object was created, in Unix time (seconds).
        """

        url_endpoint = "/v1/webhooks"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if from_created_at:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "from_created_at", from_created_at
                )
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        if page:
            query_params.append(
                query_serializer.serialize_query("form", False, "page", page)
            )
        if status:
            query_params.append(
                query_serializer.serialize_query("form", False, "status", status)
            )
        if type_:
            query_params.append(
                query_serializer.serialize_query("form", False, "type", type_)
            )
        if to_created_at:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "to_created_at", to_created_at
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetWebhooks200ResponseModel._unmap(res)
        return res

    def get_webhook_by_token(
        self, webhook_id: str
    ) -> GetWebhookByToken200ResponseModel:
        """
        Use List Webhooks to find the IDs of webhooks.
        Parameters:
        ----------
            webhook_id: str
                ID of the webhook. String starting with wh_.
        """

        url_endpoint = "/v1/webhooks/{webhook_id}"
        headers = {}
        self._add_required_headers(headers)
        if not webhook_id:
            raise ValueError(
                "Parameter webhook_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{webhook_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, webhook_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetWebhookByToken200ResponseModel._unmap(res)
        return res

    def resend_webhook_by_token(
        self, webhook_id: str
    ) -> ResendWebhookByToken200ResponseModel:
        """
        Use List Webhooks to find the IDs of webhooks. You can resend a webhook that is in status ERR.
        Parameters:
        ----------
            webhook_id: str
                The webhook ID. String starting with wh_.
        """

        url_endpoint = "/v1/webhooks/{webhook_id}"
        headers = {}
        self._add_required_headers(headers)
        if not webhook_id:
            raise ValueError(
                "Parameter webhook_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{webhook_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, webhook_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return ResendWebhookByToken200ResponseModel._unmap(res)
        return res
