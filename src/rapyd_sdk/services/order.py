from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import (
    InlineResponse200_54,
    InlineResponse200_55,
    OrderIdPayBody,
    OrdersOrderIdBody,
    V1OrdersBody,
)


class OrderService(BaseService):

    @cast_models
    def list_order(
        self, limit: str = None, ending_before: str = None, starting_after: str = None
    ) -> InlineResponse200_54:
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
        :rtype: InlineResponse200_54
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
        return InlineResponse200_54._unmap(response)

    @cast_models
    def create_order(self, request_body: V1OrdersBody = None) -> InlineResponse200_55:
        """Create an order for goods. For services, see Create Subscription.

        :param request_body: The request body., defaults to None
        :type request_body: V1OrdersBody, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created order.
        :rtype: InlineResponse200_55
        """

        Validator(V1OrdersBody).is_optional().validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/orders", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_55._unmap(response)

    @cast_models
    def retrieve_order(self, order_id: str) -> InlineResponse200_55:
        """Retrieve the details of an order.

        :param order_id: ID of the order. String starting with **order_**.
        :type order_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: SUCCESS
        :rtype: InlineResponse200_55
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
        return InlineResponse200_55._unmap(response)

    @cast_models
    def update_order(
        self, request_body: OrdersOrderIdBody, order_id: str
    ) -> InlineResponse200_55:
        """Change or modify an order.

        :param request_body: The request body.
        :type request_body: OrdersOrderIdBody
        :param order_id: ID of the order. String starting with **order_**.
        :type order_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: SUCCESS
        :rtype: InlineResponse200_55
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
        return InlineResponse200_55._unmap(response)

    @cast_models
    def pay_order(
        self, request_body: OrderIdPayBody, order_id: str
    ) -> InlineResponse200_55:
        """Pay an order.

        :param request_body: The request body.
        :type request_body: OrderIdPayBody
        :param order_id: ID of the order. String starting with **order_**.
        :type order_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: SUCCESS
        :rtype: InlineResponse200_55
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
        return InlineResponse200_55._unmap(response)
