from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.v1_skus_body import V1SkusBody
from ..models.utils.cast_models import cast_models
from ..models.skus_sku_id_body import SkusSkuIdBody
from ..models.inline_response_200_74 import InlineResponse200_74
from ..models.inline_response_200_73 import InlineResponse200_73
from ..models.inline_response_200_72 import InlineResponse200_72


class SkuService(BaseService):

    @cast_models
    def retrieve_sku(self, sku_id: str) -> InlineResponse200_72:
        """Retrieve the details of an SKU.

        :param sku_id: ID of the 'sku' object. String starting with sku_.
        :type sku_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The requested SKU object
        :rtype: InlineResponse200_72
        """

        Validator(str).validate(sku_id)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/skus/{{skuId}}", self.get_default_headers())
            .add_path("skuId", sku_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_72._unmap(response)

    @cast_models
    def update_sku(
        self, sku_id: str, request_body: SkusSkuIdBody = None
    ) -> InlineResponse200_72:
        """Change or modify an SKU.

        :param request_body: The request body., defaults to None
        :type request_body: SkusSkuIdBody, optional
        :param sku_id: ID of the 'sku' object. String starting with sku_.
        :type sku_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The requested SKU object
        :rtype: InlineResponse200_72
        """

        Validator(SkusSkuIdBody).is_optional().validate(request_body)
        Validator(str).validate(sku_id)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/skus/{{skuId}}", self.get_default_headers())
            .add_path("skuId", sku_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_72._unmap(response)

    @cast_models
    def delete_sku(self, sku_id: str) -> InlineResponse200_73:
        """Delete an SKU from the Rapyd platform.

        :param sku_id: ID of the 'sku' object. String starting with sku_.
        :type sku_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The SKU deletion result
        :rtype: InlineResponse200_73
        """

        Validator(str).validate(sku_id)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/skus/{{skuId}}", self.get_default_headers())
            .add_path("skuId", sku_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_73._unmap(response)

    @cast_models
    def list_sku(
        self,
        active: bool = None,
        starting_after: float = None,
        ending_before: float = None,
        limit: float = None,
    ) -> InlineResponse200_74:
        """Retrieve a list of all SKUs.

        :param active: Determines whether the query returns active SKUs or inactive SKUs. Default is true., defaults to None
        :type active: bool, optional
        :param starting_after: The ID of the SKU created before the first SKU you want to retrieve., defaults to None
        :type starting_after: float, optional
        :param ending_before: The ID of the SKU created after the last SKU you want to retrieve., defaults to None
        :type ending_before: float, optional
        :param limit: The maximum number of SKUs to return. Range 1-100. Default is 10., defaults to None
        :type limit: float, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of SKUs,
        :rtype: InlineResponse200_74
        """

        Validator(bool).is_optional().validate(active)
        Validator(float).is_optional().validate(starting_after)
        Validator(float).is_optional().validate(ending_before)
        Validator(float).is_optional().validate(limit)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/skus", self.get_default_headers())
            .add_query("active", active, explode=False)
            .add_query("starting_after", starting_after, explode=False)
            .add_query("ending_before", ending_before, explode=False)
            .add_query("limit", limit, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_74._unmap(response)

    @cast_models
    def create_sku(self, request_body: V1SkusBody = None) -> InlineResponse200_72:
        """Create an SKU and attach it to a product.

        :param request_body: The request body., defaults to None
        :type request_body: V1SkusBody, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created SKU,
        :rtype: InlineResponse200_72
        """

        Validator(V1SkusBody).is_optional().validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/skus", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_72._unmap(response)
