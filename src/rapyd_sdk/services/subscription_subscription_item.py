from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import (
    InlineResponse200_77,
    InlineResponse200_78,
    InlineResponse200_79,
    InlineResponse200_80,
    InlineResponse200_81,
    SubscriptionItemIdUsageRecordsBody,
    SubscriptionItemsSubscriptionItemIdBody,
    V1SubscriptionItemsBody,
)


class SubscriptionSubscriptionItemService(BaseService):

    @cast_models
    def list_subscription_item(
        self,
        ending_before: float = None,
        limit: float = None,
        starting_after: str = None,
        subscription: str = None,
    ) -> InlineResponse200_77:
        """Retrieve a list of all subscription items for a subscription.

        :param ending_before: The ID of the subscription item created after the last subscription item you want to retrieve., defaults to None
        :type ending_before: float, optional
        :param limit: The maximum number of subscription items to return. Range 1-100. Default is 10., defaults to None
        :type limit: float, optional
        :param starting_after: The ID of the subscription item created before the first subscription item you want to retrieve., defaults to None
        :type starting_after: str, optional
        :param subscription: ID of the subscription., defaults to None
        :type subscription: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of subscriptions
        :rtype: InlineResponse200_77
        """

        Validator(float).is_optional().validate(ending_before)
        Validator(float).is_optional().validate(limit)
        Validator(str).is_optional().validate(starting_after)
        Validator(str).is_optional().validate(subscription)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/subscription_items", self.get_default_headers()
            )
            .add_query("ending_before", ending_before, explode=False)
            .add_query("limit", limit, explode=False)
            .add_query("starting_after", starting_after, explode=False)
            .add_query("subscription", subscription, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_77._unmap(response)

    @cast_models
    def create_subscription_item(
        self, request_body: V1SubscriptionItemsBody
    ) -> InlineResponse200_78:
        """Create a subscription item and add it to an existing subscription for recurring payment.

        :param request_body: The request body.
        :type request_body: V1SubscriptionItemsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created subscription
        :rtype: InlineResponse200_78
        """

        Validator(V1SubscriptionItemsBody).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/subscription_items", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_78._unmap(response)

    @cast_models
    def retrieve_subscription_item(
        self, subscription_item_id: str
    ) -> InlineResponse200_78:
        """Retrieve the details of a subscription item.

        :param subscription_item_id: ID of the subscription item. String starting with **subi_**.
        :type subscription_item_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created subscription
        :rtype: InlineResponse200_78
        """

        Validator(str).validate(subscription_item_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/subscription_items/{{subscriptionItemId}}",
                self.get_default_headers(),
            )
            .add_path("subscriptionItemId", subscription_item_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_78._unmap(response)

    @cast_models
    def update_subscription_item(
        self,
        request_body: SubscriptionItemsSubscriptionItemIdBody,
        subscription_item_id: str,
    ) -> InlineResponse200_78:
        """Change or modify a subscription item.

        :param request_body: The request body.
        :type request_body: SubscriptionItemsSubscriptionItemIdBody
        :param subscription_item_id: ID of the subscription item. String starting with **subi_**.
        :type subscription_item_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created subscription
        :rtype: InlineResponse200_78
        """

        Validator(SubscriptionItemsSubscriptionItemIdBody).validate(request_body)
        Validator(str).validate(subscription_item_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/subscription_items/{{subscriptionItemId}}",
                self.get_default_headers(),
            )
            .add_path("subscriptionItemId", subscription_item_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_78._unmap(response)

    @cast_models
    def delete_subscription_item(
        self, subscription_item_id: str
    ) -> InlineResponse200_79:
        """Delete a subscription item from the Rapyd platform.

        :param subscription_item_id: ID of the subscription item. String starting with **subi_**.
        :type subscription_item_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created subscription
        :rtype: InlineResponse200_79
        """

        Validator(str).validate(subscription_item_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/subscription_items/{{subscriptionItemId}}",
                self.get_default_headers(),
            )
            .add_path("subscriptionItemId", subscription_item_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_79._unmap(response)

    @cast_models
    def usage_record_summaries(
        self,
        subscription_item_id: str,
        limit: float = None,
        ending_before: float = None,
        starting_after: float = None,
    ) -> InlineResponse200_80:
        """Retrieve a list of usage records for a subscription item

        :param subscription_item_id: ID of the subscription item. String starting with **subi_**.
        :type subscription_item_id: str
        :param limit: The maximum number of usage records that are returned. Range is 1-100. Default is 10., defaults to None
        :type limit: float, optional
        :param ending_before: The latest date and time of the returned usage records. Format is in Unix time., defaults to None
        :type ending_before: float, optional
        :param starting_after: The earliest date and time of the returned usage records. Format is in Unix time., defaults to None
        :type starting_after: float, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The subscription after updated
        :rtype: InlineResponse200_80
        """

        Validator(str).validate(subscription_item_id)
        Validator(float).is_optional().validate(limit)
        Validator(float).is_optional().validate(ending_before)
        Validator(float).is_optional().validate(starting_after)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/subscription_items/{{subscriptionItemId}}/usage_record_summaries",
                self.get_default_headers(),
            )
            .add_path("subscriptionItemId", subscription_item_id)
            .add_query("limit", limit)
            .add_query("ending_before", ending_before)
            .add_query("starting_after", starting_after)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_80._unmap(response)

    @cast_models
    def create_subscription_item_usage_record(
        self,
        request_body: SubscriptionItemIdUsageRecordsBody,
        subscription_item_id: str,
    ) -> InlineResponse200_81:
        """Create a usage record or update an existing usage record where its unique identifier is composed of timestamp and subscription_item

        :param request_body: The request body.
        :type request_body: SubscriptionItemIdUsageRecordsBody
        :param subscription_item_id: ID of the subscription item. String starting with **subi_**.
        :type subscription_item_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The subscription after updated
        :rtype: InlineResponse200_81
        """

        Validator(SubscriptionItemIdUsageRecordsBody).validate(request_body)
        Validator(str).validate(subscription_item_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/subscription_items/{{subscriptionItemId}}/usage_records",
                self.get_default_headers(),
            )
            .add_path("subscriptionItemId", subscription_item_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_81._unmap(response)
