from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import (
    InlineResponse200_71,
    InlineResponse200_72,
    InlineResponse200_73,
    ProductsProductsIdBody,
    V1ProductsBody,
)


class SubscriptionProductService(BaseService):

    @cast_models
    def get_products_list(
        self, ending_before: str = None, limit: str = None, starting_after: str = None
    ) -> InlineResponse200_72:
        """Retrieve a list of all products.

        :param ending_before: The ID of the products created after the last product you want to retrieve., defaults to None
        :type ending_before: str, optional
        :param limit: The maximum number of products to return. Range 1-100. Default is 10., defaults to None
        :type limit: str, optional
        :param starting_after: The ID of the product created before the first products you want to retrieve., defaults to None
        :type starting_after: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of products
        :rtype: InlineResponse200_72
        """

        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(limit)
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
        return InlineResponse200_72._unmap(response)

    @cast_models
    def create_product(self, request_body: V1ProductsBody) -> InlineResponse200_73:
        """Create goods or services.

        :param request_body: The request body.
        :type request_body: V1ProductsBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created Product
        :rtype: InlineResponse200_73
        """

        Validator(V1ProductsBody).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/products", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_73._unmap(response)

    @cast_models
    def get_product(self, products_id: str) -> InlineResponse200_73:
        """Retrieve details of a product or service.

        :param products_id: ID of the product.
        :type products_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The Product
        :rtype: InlineResponse200_73
        """

        Validator(str).validate(products_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/products/{{productsId}}",
                self.get_default_headers(),
            )
            .add_path("productsId", products_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_73._unmap(response)

    @cast_models
    def update_product(
        self, products_id: str, request_body: ProductsProductsIdBody = None
    ) -> InlineResponse200_73:
        """Change or modify a product or service.

        :param request_body: The request body., defaults to None
        :type request_body: ProductsProductsIdBody, optional
        :param products_id: ID of the product.
        :type products_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created Product
        :rtype: InlineResponse200_73
        """

        Validator(ProductsProductsIdBody).is_optional().validate(request_body)
        Validator(str).validate(products_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/products/{{productsId}}",
                self.get_default_headers(),
            )
            .add_path("productsId", products_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_73._unmap(response)

    @cast_models
    def delete_product(self, products_id: str) -> InlineResponse200_71:
        """Delete a product or service from the Rapyd platform. This action also deletes all associated plans.

        :param products_id: ID of the product.
        :type products_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Rapyd response with operation result, and product id
        :rtype: InlineResponse200_71
        """

        Validator(str).validate(products_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/products/{{productsId}}",
                self.get_default_headers(),
            )
            .add_path("productsId", products_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_71._unmap(response)
