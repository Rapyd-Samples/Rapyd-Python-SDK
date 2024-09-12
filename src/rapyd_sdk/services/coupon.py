from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.inline_response_200_32 import InlineResponse200_32
from ..models.inline_response_200_31 import InlineResponse200_31
from ..models.inline_response_200_30 import InlineResponse200_30
from ..models.inline_response_200_29 import InlineResponse200_29
from ..models.coupon import Coupon


class CouponService(BaseService):

    @cast_models
    def list_coupon(
        self, starting_after: str = None, ending_before: str = None, limit: str = None
    ) -> InlineResponse200_29:
        """Retrieve a list of all coupons

        :param starting_after: The ID of the coupon created before the first coupon you want to retrieve, defaults to None
        :type starting_after: str, optional
        :param ending_before: The ID of the coupon created after the last coupon you want to retrieve, defaults to None
        :type ending_before: str, optional
        :param limit: The maximum number of coupons to return. Range is 1-100. Default is 10, defaults to None
        :type limit: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of coupons
        :rtype: InlineResponse200_29
        """

        Validator(str).is_optional().validate(starting_after)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().pattern("([1-9]|[1-9]\d|100)").validate(limit)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/coupons", self.get_default_headers())
            .add_query("starting_after", starting_after)
            .add_query("ending_before", ending_before)
            .add_query("limit", limit)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_29._unmap(response)

    @cast_models
    def create_coupon(self, request_body: Coupon) -> InlineResponse200_30:
        """create a coupon

        :param request_body: The request body.
        :type request_body: Coupon
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Coupon was created
        :rtype: InlineResponse200_30
        """

        Validator(Coupon).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/coupons", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_30._unmap(response)

    @cast_models
    def retrieve_coupon(self, coupon_id: str) -> InlineResponse200_31:
        """Retrieve a coupon

        :param coupon_id: coupon Id. String starting with coupon_.
        :type coupon_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: get Coupon details By coupon Id
        :rtype: InlineResponse200_31
        """

        Validator(str).validate(coupon_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/coupons/{{couponId}}", self.get_default_headers()
            )
            .add_path("couponId", coupon_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_31._unmap(response)

    @cast_models
    def update_coupon(
        self, request_body: Coupon, coupon_id: str
    ) -> InlineResponse200_31:
        """Modify the metadata of a coupon with coupon Id in Path

        :param request_body: The request body.
        :type request_body: Coupon
        :param coupon_id: coupon Id. String starting with coupon_.
        :type coupon_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: coupon was updated
        :rtype: InlineResponse200_31
        """

        Validator(Coupon).validate(request_body)
        Validator(str).validate(coupon_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/coupons/{{couponId}}", self.get_default_headers()
            )
            .add_path("couponId", coupon_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_31._unmap(response)

    @cast_models
    def delete_coupon(self, coupon_id: str) -> InlineResponse200_32:
        """Delete a coupon from the Rapyd platform. Deleting a coupon removes it from all customers and subscriptions, but does not affect invoices and payment authorizations that have already been calculated

        :param coupon_id: coupon Id. String starting with coupon_.
        :type coupon_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: coupon was deleted
        :rtype: InlineResponse200_32
        """

        Validator(str).validate(coupon_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/coupons/{{couponId}}", self.get_default_headers()
            )
            .add_path("couponId", coupon_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_32._unmap(response)
