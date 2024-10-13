from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import InlineResponse200_56, InlineResponse200_57, OrderIdReturnsBody


class OrderReturnService(BaseService):

    @cast_models
    def returns_order(
        self, request_body: OrderIdReturnsBody, order_id: str
    ) -> InlineResponse200_56:
        """Make a return against an order. The maximum amount of the return is the amount of the order

        :param request_body: The request body.
        :type request_body: OrderIdReturnsBody
        :param order_id: ID of the order. String starting with order_.
        :type order_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: SUCCESS
        :rtype: InlineResponse200_56
        """

        Validator(OrderIdReturnsBody).validate(request_body)
        Validator(str).validate(order_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/orders/{{orderId}}/returns",
                self.get_default_headers(),
            )
            .add_path("orderId", order_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_56._unmap(response)

    @cast_models
    def list_order_return(
        self,
        limit: str = None,
        ending_before: str = None,
        starting_after: str = None,
        tokens: List[str] = None,
    ) -> InlineResponse200_57:
        """Retrieve a list of all order returns.

        :param limit: The maximum number of returns to list. Range - 1-100. Default is 10., defaults to None
        :type limit: str, optional
        :param ending_before: The ID of the order created after the last order you want to retrieve a return from., defaults to None
        :type ending_before: str, optional
        :param starting_after: The ID of the order created before the first order you want to retrieve a return from., defaults to None
        :type starting_after: str, optional
        :param tokens: Filters the list for orders related to the specified order., defaults to None
        :type tokens: List[str], optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of orders.
        :rtype: InlineResponse200_57
        """

        Validator(str).is_optional().validate(limit)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(starting_after)
        Validator(str).is_array().is_optional().validate(tokens)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/order_returns", self.get_default_headers())
            .add_query("limit", limit, explode=False)
            .add_query("ending_before", ending_before, explode=False)
            .add_query("starting_after", starting_after, explode=False)
            .add_query("tokens", tokens, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_57._unmap(response)

    @cast_models
    def retrieve_order_return(self, order_returns_id: str) -> InlineResponse200_56:
        """Retrieve the details of a return.

        :param order_returns_id: ID of the return. String starting with **orre_**.
        :type order_returns_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: SUCCESS
        :rtype: InlineResponse200_56
        """

        Validator(str).validate(order_returns_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/order_returns/{{orderReturnsId}}",
                self.get_default_headers(),
            )
            .add_path("orderReturnsId", order_returns_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_56._unmap(response)
