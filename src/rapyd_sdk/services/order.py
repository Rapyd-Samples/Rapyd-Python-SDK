from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.v1_orders_body import V1OrdersBody
from ..models.utils.cast_models import cast_models
from ..models.orders_order_id_body import OrdersOrderIdBody
from ..models.order_id_returns_body import OrderIdReturnsBody
from ..models.order_id_pay_body import OrderIdPayBody
from ..models.inline_response_200_50 import InlineResponse200_50
from ..models.inline_response_200_49 import InlineResponse200_49
from ..models.inline_response_200_48 import InlineResponse200_48
from ..models.inline_response_200_47 import InlineResponse200_47
from ..models.inline_response_200_46 import InlineResponse200_46


class OrderService(BaseService):

    @cast_models
    def list_order(
        self, limit: str = None, ending_before: str = None, starting_after: str = None
    ) -> InlineResponse200_46:
        """Retrieve a list of all orders.

        :param limit: The maximum number of orders to return. Range - 1-100. Default is 10., defaults to None
        :type limit: str, optional
        :param ending_before: The ID of the order created after the last order you want to retrieve., defaults to None
        :type ending_before: str, optional
        :param starting_after: The ID of the order created before the first order you want to retrieve., defaults to None
        :type starting_after: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of orders.
        :rtype: InlineResponse200_46
        """

        Validator(str).is_optional().validate(limit)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(starting_after)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/orders", self.get_default_headers())
            .add_query("limit", limit, explode=False)
            .add_query("ending_before", ending_before, explode=False)
            .add_query("starting_after", starting_after, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_46._unmap(response)

    @cast_models
    def create_order(self, request_body: V1OrdersBody = None) -> InlineResponse200_47:
        """Create an order for goods. For services, see Create Subscription.

        :param request_body: The request body., defaults to None
        :type request_body: V1OrdersBody, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created order.
        :rtype: InlineResponse200_47
        """

        Validator(V1OrdersBody).is_optional().validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/orders", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_47._unmap(response)

    @cast_models
    def retrieve_order(self, order_id: str) -> InlineResponse200_48:
        """Retrieve the details of an order.

        :param order_id: ID of the order. String starting with order_.
        :type order_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: SUCCESS
        :rtype: InlineResponse200_48
        """

        Validator(str).validate(order_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/orders/{{orderId}}", self.get_default_headers()
            )
            .add_path("orderId", order_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_48._unmap(response)

    @cast_models
    def update_order(
        self, request_body: OrdersOrderIdBody, order_id: str
    ) -> InlineResponse200_48:
        """Change or modify an order.

        :param request_body: The request body.
        :type request_body: OrdersOrderIdBody
        :param order_id: ID of the order. String starting with order_.
        :type order_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: SUCCESS
        :rtype: InlineResponse200_48
        """

        Validator(OrdersOrderIdBody).validate(request_body)
        Validator(str).validate(order_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/orders/{{orderId}}", self.get_default_headers()
            )
            .add_path("orderId", order_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_48._unmap(response)

    @cast_models
    def returns_order(
        self, request_body: OrderIdReturnsBody, order_id: str
    ) -> InlineResponse200_49:
        """Make a return against an order. The maximum amount of the return is the amount of the order

        :param request_body: The request body.
        :type request_body: OrderIdReturnsBody
        :param order_id: ID of the order. String starting with order_.
        :type order_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: SUCCESS
        :rtype: InlineResponse200_49
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
        return InlineResponse200_49._unmap(response)

    @cast_models
    def pay_order(
        self, request_body: OrderIdPayBody, order_id: str
    ) -> InlineResponse200_48:
        """Pay an order.

        :param request_body: The request body.
        :type request_body: OrderIdPayBody
        :param order_id: ID of the order. String starting with order_.
        :type order_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: SUCCESS
        :rtype: InlineResponse200_48
        """

        Validator(OrderIdPayBody).validate(request_body)
        Validator(str).validate(order_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/orders/{{orderId}}/pay", self.get_default_headers()
            )
            .add_path("orderId", order_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_48._unmap(response)

    @cast_models
    def list_order_return(
        self,
        limit: str = None,
        ending_before: str = None,
        starting_after: str = None,
        tokens: List[str] = None,
    ) -> InlineResponse200_50:
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
        :rtype: InlineResponse200_50
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
        return InlineResponse200_50._unmap(response)

    @cast_models
    def retrieve_order_return(self, order_returns_id: str) -> InlineResponse200_49:
        """Retrieve the details of a return.

        :param order_returns_id: ID of the return. String starting with orre_.
        :type order_returns_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: SUCCESS
        :rtype: InlineResponse200_49
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
        return InlineResponse200_49._unmap(response)
