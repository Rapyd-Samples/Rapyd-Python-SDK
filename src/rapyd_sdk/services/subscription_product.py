from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.v1_products_body import V1ProductsBody
from ..models.utils.cast_models import cast_models
from ..models.products_products_id_body import ProductsProductsIdBody
from ..models.inline_response_200_62 import InlineResponse200_62
from ..models.inline_response_200_61 import InlineResponse200_61
from ..models.inline_response_200_60 import InlineResponse200_60


class SubscriptionProductService(BaseService):

    @cast_models
    def get_products_list(
        self,
        ending_before: float = None,
        limit: float = None,
        starting_after: str = None,
    ) -> InlineResponse200_61:
        """Retrieve a list of all products.

        :param ending_before: The ID of the products created after the last product you want to retrieve., defaults to None
        :type ending_before: float, optional
        :param limit: The maximum number of products to return. Range 1-100. Default is 10., defaults to None
        :type limit: float, optional
        :param starting_after: The ID of the product created before the first products you want to retrieve., defaults to None
        :type starting_after: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of products
        :rtype: InlineResponse200_61
        """

        Validator(float).is_optional().validate(ending_before)
        Validator(float).is_optional().validate(limit)
        Validator(str).is_optional().validate(starting_after)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/products", self.get_default_headers())
            .add_query("ending_before", ending_before, explode=False)
            .add_query("limit", limit, explode=False)
            .add_query("starting_after", starting_after, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_61._unmap(response)

    @cast_models
    def create_product(self, request_body: V1ProductsBody) -> InlineResponse200_62:
        """Create goods or services.

        :param request_body: The request body.
        :type request_body: V1ProductsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created Product
        :rtype: InlineResponse200_62
        """

        Validator(V1ProductsBody).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/products", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_62._unmap(response)

    @cast_models
    def get_product(self, products_id: str) -> InlineResponse200_62:
        """Retrieve details of a product or service.

        :param products_id: ID of the product.
        :type products_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The Product
        :rtype: InlineResponse200_62
        """

        Validator(str).validate(products_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/products/{{products_id}}",
                self.get_default_headers(),
            )
            .add_path("products_id", products_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_62._unmap(response)

    @cast_models
    def update_product(
        self, products_id: str, request_body: ProductsProductsIdBody = None
    ) -> InlineResponse200_62:
        """Change or modify a product or service.

        :param request_body: The request body., defaults to None
        :type request_body: ProductsProductsIdBody, optional
        :param products_id: ID of the product.
        :type products_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created Product
        :rtype: InlineResponse200_62
        """

        Validator(ProductsProductsIdBody).is_optional().validate(request_body)
        Validator(str).validate(products_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/products/{{products_id}}",
                self.get_default_headers(),
            )
            .add_path("products_id", products_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_62._unmap(response)

    @cast_models
    def delete_product(self, products_id: str) -> InlineResponse200_60:
        """Delete a product or service from the Rapyd platform. This action also deletes all associated plans.

        :param products_id: ID of the product.
        :type products_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Rapyd response with operation result, and product id
        :rtype: InlineResponse200_60
        """

        Validator(str).validate(products_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/products/{{products_id}}",
                self.get_default_headers(),
            )
            .add_path("products_id", products_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_60._unmap(response)
