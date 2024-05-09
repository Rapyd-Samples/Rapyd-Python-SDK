from urllib.parse import quote
from ..net import query_serializer
from typing import List

from .base import BaseService
from ..models.CreateAddressRequest import (
    CreateAddressRequest as CreateAddressRequestModel,
)
from ..models.CreateAddress200Response import (
    CreateAddress200Response as CreateAddress200ResponseModel,
)
from ..models.RetrieveAddress200Response import (
    RetrieveAddress200Response as RetrieveAddress200ResponseModel,
)
from ..models.AddressRequest import AddressRequest as AddressRequestModel
from ..models.UpdateAddress200Response import (
    UpdateAddress200Response as UpdateAddress200ResponseModel,
)
from ..models.ListCoupon200Response import (
    ListCoupon200Response as ListCoupon200ResponseModel,
)
from ..models.CreateCouponRequest import CreateCouponRequest as CreateCouponRequestModel
from ..models.CreateCouponRequest import (
    CreateCouponRequestGuard as CreateCouponRequestGuardModel,
)
from ..models.CreateCoupon200Response import (
    CreateCoupon200Response as CreateCoupon200ResponseModel,
)
from ..models.RetrieveCoupon200Response import (
    RetrieveCoupon200Response as RetrieveCoupon200ResponseModel,
)
from ..models.Coupon import Coupon as CouponModel
from ..models.UpdateCoupon200Response import (
    UpdateCoupon200Response as UpdateCoupon200ResponseModel,
)
from ..models.DeleteCoupon200Response import (
    DeleteCoupon200Response as DeleteCoupon200ResponseModel,
)
from ..models.GetHostedPagePayment200Response import (
    GetHostedPagePayment200Response as GetHostedPagePayment200ResponseModel,
)
from ..models.GenerateHostedPagePaymentRequest import (
    GenerateHostedPagePaymentRequest as GenerateHostedPagePaymentRequestModel,
)
from ..models.GenerateHostedPagePayment200Response import (
    GenerateHostedPagePayment200Response as GenerateHostedPagePayment200ResponseModel,
)
from ..models.ListCustomer200Response import (
    ListCustomer200Response as ListCustomer200ResponseModel,
)
from ..models.CreateCustomerRequest import (
    CreateCustomerRequest as CreateCustomerRequestModel,
)
from ..models.CreateCustomer200Response import (
    CreateCustomer200Response as CreateCustomer200ResponseModel,
)
from ..models.RetrieveCustomer200Response import (
    RetrieveCustomer200Response as RetrieveCustomer200ResponseModel,
)
from ..models.CustomerRequest import CustomerRequest as CustomerRequestModel
from ..models.UpdateCustomer200Response import (
    UpdateCustomer200Response as UpdateCustomer200ResponseModel,
)
from ..models.DeleteCustomer200Response import (
    DeleteCustomer200Response as DeleteCustomer200ResponseModel,
)
from ..models.DeleteCustomerDiscount200Response import (
    DeleteCustomerDiscount200Response as DeleteCustomerDiscount200ResponseModel,
)
from ..models.Category import Category as CategoryModel
from ..models.GetCustomerPaymentMethods200Response import (
    GetCustomerPaymentMethods200Response as GetCustomerPaymentMethods200ResponseModel,
)
from ..models.CreateCustomerPaymentMethodRequest import (
    CreateCustomerPaymentMethodRequest as CreateCustomerPaymentMethodRequestModel,
)
from ..models.CreateCustomerPaymentMethod200Response import (
    CreateCustomerPaymentMethod200Response as CreateCustomerPaymentMethod200ResponseModel,
)
from ..models.GetCustomerPaymentMethod200Response import (
    GetCustomerPaymentMethod200Response as GetCustomerPaymentMethod200ResponseModel,
)
from ..models.CustomerPaymentMethod import (
    CustomerPaymentMethod as CustomerPaymentMethodModel,
)
from ..models.CustomerPaymentMethod import (
    CustomerPaymentMethodGuard as CustomerPaymentMethodGuardModel,
)
from ..models.UpdateCustomerPaymentMethod200Response import (
    UpdateCustomerPaymentMethod200Response as UpdateCustomerPaymentMethod200ResponseModel,
)
from ..models.DeleteCustomerPaymentMethod200Response import (
    DeleteCustomerPaymentMethod200Response as DeleteCustomerPaymentMethod200ResponseModel,
)
from ..models.Status import Status as StatusModel
from ..models.GetDisputesListByOrgId200Response import (
    GetDisputesListByOrgId200Response as GetDisputesListByOrgId200ResponseModel,
)
from ..models.GetDispute200Response import (
    GetDispute200Response as GetDispute200ResponseModel,
)
from ..models.Customer import Customer as CustomerModel
from ..models.ListInvoices200Response import (
    ListInvoices200Response as ListInvoices200ResponseModel,
)
from ..models.RetrieveInvoice200Response import (
    RetrieveInvoice200Response as RetrieveInvoice200ResponseModel,
)
from ..models.UpdateInvoiceRequest import (
    UpdateInvoiceRequest as UpdateInvoiceRequestModel,
)
from ..models.UpdateInvoice200Response import (
    UpdateInvoice200Response as UpdateInvoice200ResponseModel,
)
from ..models.DeleteInvoice200Response import (
    DeleteInvoice200Response as DeleteInvoice200ResponseModel,
)
from ..models.FinalizeInvoice200Response import (
    FinalizeInvoice200Response as FinalizeInvoice200ResponseModel,
)
from ..models.PayInvoiceRequest import PayInvoiceRequest as PayInvoiceRequestModel
from ..models.PayInvoice200Response import (
    PayInvoice200Response as PayInvoice200ResponseModel,
)
from ..models.ListOrder200Response import (
    ListOrder200Response as ListOrder200ResponseModel,
)
from ..models.CreateOrderRequest import CreateOrderRequest as CreateOrderRequestModel
from ..models.CreateOrder200Response import (
    CreateOrder200Response as CreateOrder200ResponseModel,
)
from ..models.RetrieveOrder200Response import (
    RetrieveOrder200Response as RetrieveOrder200ResponseModel,
)
from ..models.UpdateOrderRequest import UpdateOrderRequest as UpdateOrderRequestModel
from ..models.UpdateOrder200Response import (
    UpdateOrder200Response as UpdateOrder200ResponseModel,
)
from ..models.ReturnsOrderRequest import ReturnsOrderRequest as ReturnsOrderRequestModel
from ..models.ReturnsOrder200Response import (
    ReturnsOrder200Response as ReturnsOrder200ResponseModel,
)
from ..models.PayOrderRequest import PayOrderRequest as PayOrderRequestModel
from ..models.PayOrder200Response import PayOrder200Response as PayOrder200ResponseModel
from ..models.ListOrderReturn200Response import (
    ListOrderReturn200Response as ListOrderReturn200ResponseModel,
)
from ..models.RetrieveOrderReturn200Response import (
    RetrieveOrderReturn200Response as RetrieveOrderReturn200ResponseModel,
)
from ..models.GetPaymentMethodsTypesByCountry200Response import (
    GetPaymentMethodsTypesByCountry200Response as GetPaymentMethodsTypesByCountry200ResponseModel,
)
from ..models.GetPaymentMethodTypeRequiredFields200Response import (
    GetPaymentMethodTypeRequiredFields200Response as GetPaymentMethodTypeRequiredFields200ResponseModel,
)
from ..models.ListPayments200Response import (
    ListPayments200Response as ListPayments200ResponseModel,
)
from ..models.CreatePaymentRequest import (
    CreatePaymentRequest as CreatePaymentRequestModel,
)
from ..models.CreatePaymentRequest import (
    CreatePaymentRequestGuard as CreatePaymentRequestGuardModel,
)
from ..models.CreatePayment200Response import (
    CreatePayment200Response as CreatePayment200ResponseModel,
)
from ..models.RetrievePayment200Response import (
    RetrievePayment200Response as RetrievePayment200ResponseModel,
)
from ..models.UpdatePaymentRequest import (
    UpdatePaymentRequest as UpdatePaymentRequestModel,
)
from ..models.UpdatePayment200Response import (
    UpdatePayment200Response as UpdatePayment200ResponseModel,
)
from ..models.CancelPayment200Response import (
    CancelPayment200Response as CancelPayment200ResponseModel,
)
from ..models.GetSubscriptionList200Response import (
    GetSubscriptionList200Response as GetSubscriptionList200ResponseModel,
)
from ..models.CreateSubscriptionRequest import (
    CreateSubscriptionRequest as CreateSubscriptionRequestModel,
)
from ..models.CreateSubscription200Response import (
    CreateSubscription200Response as CreateSubscription200ResponseModel,
)
from ..models.GetSubscription200Response import (
    GetSubscription200Response as GetSubscription200ResponseModel,
)
from ..models.UpdateSubscriptionRequest import (
    UpdateSubscriptionRequest as UpdateSubscriptionRequestModel,
)
from ..models.UpdateSubscription200Response import (
    UpdateSubscription200Response as UpdateSubscription200ResponseModel,
)
from ..models.CancelSubscription200Response import (
    CancelSubscription200Response as CancelSubscription200ResponseModel,
)
from ..models.DeleteSubscriptionDiscount200Response import (
    DeleteSubscriptionDiscount200Response as DeleteSubscriptionDiscount200ResponseModel,
)
from ..models.ListPlans200Response import (
    ListPlans200Response as ListPlans200ResponseModel,
)
from ..models.CreatePlanRequest import CreatePlanRequest as CreatePlanRequestModel
from ..models.CreatePlan200Response import (
    CreatePlan200Response as CreatePlan200ResponseModel,
)
from ..models.RetrievePlan200Response import (
    RetrievePlan200Response as RetrievePlan200ResponseModel,
)
from ..models.UpdatePlanRequest import UpdatePlanRequest as UpdatePlanRequestModel
from ..models.UpdatePlan200Response import (
    UpdatePlan200Response as UpdatePlan200ResponseModel,
)
from ..models.DeletePlan200Response import (
    DeletePlan200Response as DeletePlan200ResponseModel,
)
from ..models.GetProductsList200Response import (
    GetProductsList200Response as GetProductsList200ResponseModel,
)
from ..models.CreateProductRequest import (
    CreateProductRequest as CreateProductRequestModel,
)
from ..models.CreateProduct200Response import (
    CreateProduct200Response as CreateProduct200ResponseModel,
)
from ..models.GetProduct200Response import (
    GetProduct200Response as GetProduct200ResponseModel,
)
from ..models.UpdateProductRequest import (
    UpdateProductRequest as UpdateProductRequestModel,
)
from ..models.UpdateProduct200Response import (
    UpdateProduct200Response as UpdateProduct200ResponseModel,
)
from ..models.DeleteProduct200Response import (
    DeleteProduct200Response as DeleteProduct200ResponseModel,
)
from ..models.AllRefunds200Response import (
    AllRefunds200Response as AllRefunds200ResponseModel,
)
from ..models.RequestTotalCreateRefundRequest import (
    RequestTotalCreateRefundRequest as RequestTotalCreateRefundRequestModel,
)
from ..models.RequestTotalCreateRefund200Response import (
    RequestTotalCreateRefund200Response as RequestTotalCreateRefund200ResponseModel,
)
from ..models.SimulateCompleteRefundRequest import (
    SimulateCompleteRefundRequest as SimulateCompleteRefundRequestModel,
)
from ..models.SimulateCompleteRefund200Response import (
    SimulateCompleteRefund200Response as SimulateCompleteRefund200ResponseModel,
)
from ..models.RefundGroupPaymentRequest import (
    RefundGroupPaymentRequest as RefundGroupPaymentRequestModel,
)
from ..models.RefundGroupPayment200Response import (
    RefundGroupPayment200Response as RefundGroupPayment200ResponseModel,
)
from ..models.RefundByToken200Response import (
    RefundByToken200Response as RefundByToken200ResponseModel,
)
from ..models.UpdateRefundRequest import UpdateRefundRequest as UpdateRefundRequestModel
from ..models.UpdateRefund200Response import (
    UpdateRefund200Response as UpdateRefund200ResponseModel,
)
from ..models.ListSubscriptionItem200Response import (
    ListSubscriptionItem200Response as ListSubscriptionItem200ResponseModel,
)
from ..models.CreateSubscriptionItemRequest import (
    CreateSubscriptionItemRequest as CreateSubscriptionItemRequestModel,
)
from ..models.CreateSubscriptionItem200Response import (
    CreateSubscriptionItem200Response as CreateSubscriptionItem200ResponseModel,
)
from ..models.RetrieveSubscriptionItem200Response import (
    RetrieveSubscriptionItem200Response as RetrieveSubscriptionItem200ResponseModel,
)
from ..models.UpdateSubscriptionItemRequest import (
    UpdateSubscriptionItemRequest as UpdateSubscriptionItemRequestModel,
)
from ..models.UpdateSubscriptionItem200Response import (
    UpdateSubscriptionItem200Response as UpdateSubscriptionItem200ResponseModel,
)
from ..models.DeleteSubscriptionItem200Response import (
    DeleteSubscriptionItem200Response as DeleteSubscriptionItem200ResponseModel,
)
from ..models.UsageRecordSummaries200Response import (
    UsageRecordSummaries200Response as UsageRecordSummaries200ResponseModel,
)
from ..models.CreateSubscriptionItemUsageRecordRequest import (
    CreateSubscriptionItemUsageRecordRequest as CreateSubscriptionItemUsageRecordRequestModel,
)
from ..models.CreateSubscriptionItemUsageRecord200Response import (
    CreateSubscriptionItemUsageRecord200Response as CreateSubscriptionItemUsageRecord200ResponseModel,
)
from ..models.GetSubscriptionDiscountById200Response import (
    GetSubscriptionDiscountById200Response as GetSubscriptionDiscountById200ResponseModel,
)
from ..models.RetrieveSku200Response import (
    RetrieveSku200Response as RetrieveSku200ResponseModel,
)
from ..models.UpdateSkuRequest import UpdateSkuRequest as UpdateSkuRequestModel
from ..models.UpdateSku200Response import (
    UpdateSku200Response as UpdateSku200ResponseModel,
)
from ..models.DeleteSku200Response import (
    DeleteSku200Response as DeleteSku200ResponseModel,
)
from ..models.ListSku200Response import ListSku200Response as ListSku200ResponseModel
from ..models.CreateSkuRequest import CreateSkuRequest as CreateSkuRequestModel
from ..models.CreateSku200Response import (
    CreateSku200Response as CreateSku200ResponseModel,
)


class Collect(BaseService):
    def create_address(
        self, request_input: CreateAddressRequestModel
    ) -> CreateAddress200ResponseModel:
        """
        Create an address
        """

        if isinstance(request_input, dict):
            request_input = CreateAddressRequestModel(**request_input)
        url_endpoint = "/v1/addresses"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateAddress200ResponseModel._unmap(res)
        return res

    def retrieve_address(self, addresses_id: str) -> RetrieveAddress200ResponseModel:
        """
        Retrieve an address
        Parameters:
        ----------
            addresses_id: str
                address Id
        """

        url_endpoint = "/v1/addresses/{addresses_id}"
        headers = {}
        self._add_required_headers(headers)
        if not addresses_id:
            raise ValueError(
                "Parameter addresses_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{addresses_id}",
            quote(
                str(
                    query_serializer.serialize_path("simple", False, addresses_id, None)
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrieveAddress200ResponseModel._unmap(res)
        return res

    def update_address(
        self, addresses_id: str, request_input: AddressRequestModel = None
    ) -> UpdateAddress200ResponseModel:
        """
        Update an address
        Parameters:
        ----------
            addresses_id: str
                address Id
        """

        if isinstance(request_input, dict):
            request_input = AddressRequestModel(**request_input)
        url_endpoint = "/v1/addresses/{addresses_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not addresses_id:
            raise ValueError(
                "Parameter addresses_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{addresses_id}",
            quote(
                str(
                    query_serializer.serialize_path("simple", False, addresses_id, None)
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateAddress200ResponseModel._unmap(res)
        return res

    def list_coupon(
        self, starting_after: str = None, ending_before: str = None, limit: str = None
    ) -> ListCoupon200ResponseModel:
        """
        Retrieve list of coupons
        Parameters:
        ----------
            starting_after: str
                The ID of the coupon created before the first coupon you want to retrieve
            ending_before: str
                The ID of the coupon created after the last coupon you want to retrieve
            limit: str
                The maximum number of coupons to return. Range is 1-100. Default is 10
        """

        url_endpoint = "/v1/coupons"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if limit:
            validated_limit = self._pattern_matching(
                limit, "([1-9]|[1-9]\d|100)", "limit"
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "limit", validated_limit
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListCoupon200ResponseModel._unmap(res)
        return res

    def create_coupon(
        self, request_input: CreateCouponRequestModel
    ) -> CreateCoupon200ResponseModel:
        """
        Create new coupon
        """

        if isinstance(request_input, dict):
            request_input = CreateCouponRequestGuardModel.return_one_of(request_input)
        url_endpoint = "/v1/coupons"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateCoupon200ResponseModel._unmap(res)
        return res

    def retrieve_coupon(self, coupon_id: str) -> RetrieveCoupon200ResponseModel:
        """
        Retrieve an coupon
        Parameters:
        ----------
            coupon_id: str
                coupon Id. String starting with coupon_.
        """

        url_endpoint = "/v1/coupons/{coupon_id}"
        headers = {}
        self._add_required_headers(headers)
        if not coupon_id:
            raise ValueError(
                "Parameter coupon_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{coupon_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, coupon_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrieveCoupon200ResponseModel._unmap(res)
        return res

    def update_coupon(
        self, request_input: CouponModel, coupon_id: str
    ) -> UpdateCoupon200ResponseModel:
        """
        Update a coupon
        Parameters:
        ----------
            coupon_id: str
                coupon Id. String starting with coupon_.
        """

        if isinstance(request_input, dict):
            request_input = CouponModel(**request_input)
        url_endpoint = "/v1/coupons/{coupon_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not coupon_id:
            raise ValueError(
                "Parameter coupon_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{coupon_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, coupon_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateCoupon200ResponseModel._unmap(res)
        return res

    def delete_coupon(self, coupon_id: str) -> DeleteCoupon200ResponseModel:
        """
        Delete a coupon from the Rapyd platform
        Parameters:
        ----------
            coupon_id: str
                coupon Id. String starting with coupon_.
        """

        url_endpoint = "/v1/coupons/{coupon_id}"
        headers = {}
        self._add_required_headers(headers)
        if not coupon_id:
            raise ValueError(
                "Parameter coupon_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{coupon_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, coupon_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteCoupon200ResponseModel._unmap(res)
        return res

    def get_hosted_page_payment(
        self, checkout_token: str
    ) -> GetHostedPagePayment200ResponseModel:
        """
        Retrieve a checkout page.
        Parameters:
        ----------
            checkout_token: str
                ID of the checkout page. String starting with checkout_.
        """

        url_endpoint = "/v1/checkout/{checkout_token}"
        headers = {}
        self._add_required_headers(headers)
        if not checkout_token:
            raise ValueError(
                "Parameter checkout_token is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{checkout_token}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, checkout_token, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetHostedPagePayment200ResponseModel._unmap(res)
        return res

    def generate_hosted_page_payment(
        self, request_input: GenerateHostedPagePaymentRequestModel = None
    ) -> GenerateHostedPagePayment200ResponseModel:
        """
        Create checkout page
        """

        if isinstance(request_input, dict):
            request_input = GenerateHostedPagePaymentRequestModel(**request_input)
        url_endpoint = "/v1/checkout"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return GenerateHostedPagePayment200ResponseModel._unmap(res)
        return res

    def list_customer(
        self, starting_after: str = None, ending_before: str = None, limit: str = None
    ) -> ListCustomer200ResponseModel:
        """
        Retrieve list of customers
        Parameters:
        ----------
            starting_after: str
                The ID of the customer created before the first customer you want to retrieve
            ending_before: str
                The ID of the customer created after the last customer you want to retrieve
            limit: str
                The maximum number of customers to return. Range is 1-100. Default is 10
        """

        url_endpoint = "/v1/customers"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if limit:
            validated_limit = self._pattern_matching(
                limit, "([1-9]|[1-9]\d|100)", "limit"
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "limit", validated_limit
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListCustomer200ResponseModel._unmap(res)
        return res

    def create_customer(
        self, request_input: CreateCustomerRequestModel
    ) -> CreateCustomer200ResponseModel:
        """
        Create a customer
        """

        if isinstance(request_input, dict):
            request_input = CreateCustomerRequestModel(**request_input)
        url_endpoint = "/v1/customers"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateCustomer200ResponseModel._unmap(res)
        return res

    def retrieve_customer(self, customer_id: str) -> RetrieveCustomer200ResponseModel:
        """
        Retrieve a customer details
        Parameters:
        ----------
            customer_id: str
                customer Id
        """

        url_endpoint = "/v1/customers/{customer_id}"
        headers = {}
        self._add_required_headers(headers)
        if not customer_id:
            raise ValueError(
                "Parameter customer_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{customer_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, customer_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrieveCustomer200ResponseModel._unmap(res)
        return res

    def update_customer(
        self, customer_id: str, request_input: CustomerRequestModel = None
    ) -> UpdateCustomer200ResponseModel:
        """
        Update customer
        Parameters:
        ----------
            customer_id: str
                customer Id
        """

        if isinstance(request_input, dict):
            request_input = CustomerRequestModel(**request_input)
        url_endpoint = "/v1/customers/{customer_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not customer_id:
            raise ValueError(
                "Parameter customer_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{customer_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, customer_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateCustomer200ResponseModel._unmap(res)
        return res

    def delete_customer(self, customer_id: str) -> DeleteCustomer200ResponseModel:
        """
        Delete a customer from the Rapyd platform
        Parameters:
        ----------
            customer_id: str
                customer Id
        """

        url_endpoint = "/v1/customers/{customer_id}"
        headers = {}
        self._add_required_headers(headers)
        if not customer_id:
            raise ValueError(
                "Parameter customer_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{customer_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, customer_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteCustomer200ResponseModel._unmap(res)
        return res

    def delete_customer_discount(
        self, customer_id: str
    ) -> DeleteCustomerDiscount200ResponseModel:
        """
        Delete the discount that has been assigned to a customer
        Parameters:
        ----------
            customer_id: str
                customer Id
        """

        url_endpoint = "/v1/customers/{customer_id}/discount"
        headers = {}
        self._add_required_headers(headers)
        if not customer_id:
            raise ValueError(
                "Parameter customer_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{customer_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, customer_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteCustomerDiscount200ResponseModel._unmap(res)
        return res

    def get_customer_payment_methods(
        self,
        customer_id: str,
        category: CategoryModel = None,
        starting_after: str = None,
        ending_before: str = None,
        limit: str = None,
        type_: str = None,
    ) -> GetCustomerPaymentMethods200ResponseModel:
        """
        Retrieve payment methods for a customer
        Parameters:
        ----------
            customer_id: str
                customer Id
            category: Category
            starting_after: str
                The ID of the coupon created before the first coupon you want to retrieve
            ending_before: str
                The ID of the coupon created after the last coupon you want to retrieve
            limit: str
                The maximum number of coupons to return. Range is 1-100. Default is 10
            type_: str
                The type of payment method to find.
        """

        if isinstance(category, dict):
            category = CategoryModel(**category)
        url_endpoint = "/v1/customers/{customer_id}/payment_methods"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not customer_id:
            raise ValueError(
                "Parameter customer_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{customer_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, customer_id, None))
            ),
        )
        if category:
            validated_category = self._enum_matching(
                category, CategoryModel.list(), "category"
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "category", validated_category
                )
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        if type_:
            query_params.append(
                query_serializer.serialize_query("form", False, "type", type_)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetCustomerPaymentMethods200ResponseModel._unmap(res)
        return res

    def create_customer_payment_method(
        self, request_input: CreateCustomerPaymentMethodRequestModel, customer_id: str
    ) -> CreateCustomerPaymentMethod200ResponseModel:
        """
        Add a payment method to a customer profile
        Parameters:
        ----------
            customer_id: str
                customer Id
        """

        if isinstance(request_input, dict):
            request_input = CreateCustomerPaymentMethodRequestModel(**request_input)
        url_endpoint = "/v1/customers/{customer_id}/payment_methods"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not customer_id:
            raise ValueError(
                "Parameter customer_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{customer_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, customer_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateCustomerPaymentMethod200ResponseModel._unmap(res)
        return res

    def get_customer_payment_method(
        self, pmt_id: str, customer_id: str
    ) -> GetCustomerPaymentMethod200ResponseModel:
        """
        Retrieve a payment method for a specific customer
        Parameters:
        ----------
            customer_id: str
                customer Id
            pmt_id: str
                Pmt Id
        """

        url_endpoint = "/v1/customers/{customer_id}/payment_methods/{pmt_id}"
        headers = {}
        self._add_required_headers(headers)
        if not customer_id:
            raise ValueError(
                "Parameter customer_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{customer_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, customer_id, None))
            ),
        )
        if not pmt_id:
            raise ValueError("Parameter pmt_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{pmt_id}",
            quote(str(query_serializer.serialize_path("simple", False, pmt_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetCustomerPaymentMethod200ResponseModel._unmap(res)
        return res

    def update_customer_payment_method(
        self, request_input: CustomerPaymentMethodModel, pmt_id: str, customer_id: str
    ) -> UpdateCustomerPaymentMethod200ResponseModel:
        """
        Update payment method for customer
        Parameters:
        ----------
            customer_id: str
                customer Id
            pmt_id: str
                Pmt Id
        """

        if isinstance(request_input, dict):
            request_input = CustomerPaymentMethodGuardModel.return_one_of(request_input)
        url_endpoint = "/v1/customers/{customer_id}/payment_methods/{pmt_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not customer_id:
            raise ValueError(
                "Parameter customer_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{customer_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, customer_id, None))
            ),
        )
        if not pmt_id:
            raise ValueError("Parameter pmt_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{pmt_id}",
            quote(str(query_serializer.serialize_path("simple", False, pmt_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateCustomerPaymentMethod200ResponseModel._unmap(res)
        return res

    def delete_customer_payment_method(
        self, pmt_id: str, customer_id: str
    ) -> DeleteCustomerPaymentMethod200ResponseModel:
        """
        Delete a payment method type from customer
        Parameters:
        ----------
            customer_id: str
                customer Id
            pmt_id: str
                Pmt Id
        """

        url_endpoint = "/v1/customers/{customer_id}/payment_methods/{pmt_id}"
        headers = {}
        self._add_required_headers(headers)
        if not customer_id:
            raise ValueError(
                "Parameter customer_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{customer_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, customer_id, None))
            ),
        )
        if not pmt_id:
            raise ValueError("Parameter pmt_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{pmt_id}",
            quote(str(query_serializer.serialize_path("simple", False, pmt_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteCustomerPaymentMethod200ResponseModel._unmap(res)
        return res

    def get_disputes_list_by_org_id(
        self,
        starting_after: str = None,
        ending_before: str = None,
        limit: str = None,
        status: StatusModel = None,
        payment: str = None,
    ) -> GetDisputesListByOrgId200ResponseModel:
        """
        Retrieve list of disputes
        Parameters:
        ----------
            starting_after: str
                The ID of the dispute created before the first dispute you want to retrieve. String starting with dispute_.
            ending_before: str
                The ID of the dispute created after the last dispute you want to retrieve. String starting with dispute_.
            limit: str
                The maximum number of disputes to return. Range is 1-100. Default is 10.
            status: Status
                Filters the list for disputes with the specified dispute status.
            payment: str
                The ID of the payment that is linked to the dispute. String starting with payment_.
        """

        if isinstance(status, dict):
            status = StatusModel(**status)
        url_endpoint = "/v1/disputes"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if limit:
            validated_limit = self._pattern_matching(
                limit, "([1-9]|[1-9]\d|100)", "limit"
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "limit", validated_limit
                )
            )
        if status:
            query_params.append(
                query_serializer.serialize_query("form", False, "status", status)
            )
        if payment:
            query_params.append(
                query_serializer.serialize_query("form", False, "payment", payment)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetDisputesListByOrgId200ResponseModel._unmap(res)
        return res

    def get_dispute(self, dispute_id: str) -> GetDispute200ResponseModel:
        """
        Retrieve an dispute.
        Parameters:
        ----------
            dispute_id: str
                ID of the dispute you want to retrieve. String starting with dispute_.
        """

        url_endpoint = "/v1/disputes/{dispute_id}"
        headers = {}
        self._add_required_headers(headers)
        if not dispute_id:
            raise ValueError(
                "Parameter dispute_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{dispute_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, dispute_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetDispute200ResponseModel._unmap(res)
        return res

    def list_invoices(
        self,
        customer: CustomerModel = None,
        date_: str = None,
        due_date: str = None,
        ending_before: str = None,
        limit: str = None,
        starting_after: str = None,
        subscription: bool = None,
    ) -> ListInvoices200ResponseModel:
        """
        List Invoices
        Parameters:
        ----------
            customer: Customer
                ID of the customer. String starting with cus_.
            date_: str
                Date that the invoice was created.
            due_date: str
                The date payment is due on this invoice. This value is calculated from the date the invoice is created, plus the number of days specified in the days_until_due field. Format is in Unix time.
            ending_before: str
                The ID of the invoice created after the last invoice you want to retrieve. card.
            limit: str
                The maximum number of invoices to return. Range 1-100. Default is 10.
            starting_after: str
                The ID of the invoice created before the first invoice you want to retrieve.
            subscription: bool
                ID of the subscription. String starting with sub_.
        """

        if isinstance(customer, dict):
            customer = CustomerModel(**customer)
        url_endpoint = "/v1/invoices"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if customer:
            query_params.append(
                query_serializer.serialize_query("form", True, "customer", customer)
            )
        if date_:
            query_params.append(
                query_serializer.serialize_query("form", True, "date", date_)
            )
        if due_date:
            query_params.append(
                query_serializer.serialize_query("form", True, "due_date", due_date)
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "ending_before", ending_before
                )
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", True, "limit", limit)
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "starting_after", starting_after
                )
            )
        if subscription:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "subscription", subscription
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListInvoices200ResponseModel._unmap(res)
        return res

    def retrieve_invoice(self, invoice_id: str) -> RetrieveInvoice200ResponseModel:
        """
        Retrieve Invoice
        Parameters:
        ----------
            invoice_id: str
                The ID of the invoice that you want to retrieve.
        """

        url_endpoint = "/v1/invoices/{invoice_id}"
        headers = {}
        self._add_required_headers(headers)
        if not invoice_id:
            raise ValueError(
                "Parameter invoice_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{invoice_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, invoice_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrieveInvoice200ResponseModel._unmap(res)
        return res

    def update_invoice(
        self, invoice_id: str, request_input: UpdateInvoiceRequestModel = None
    ) -> UpdateInvoice200ResponseModel:
        """
        Update Invoice
        Parameters:
        ----------
            invoice_id: str
                The ID of the invoice that you want to updated.
        """

        if isinstance(request_input, dict):
            request_input = UpdateInvoiceRequestModel(**request_input)
        url_endpoint = "/v1/invoices/{invoice_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not invoice_id:
            raise ValueError(
                "Parameter invoice_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{invoice_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, invoice_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateInvoice200ResponseModel._unmap(res)
        return res

    def delete_invoice(self, invoice_id: str) -> DeleteInvoice200ResponseModel:
        """
        Delete Invoice
        Parameters:
        ----------
            invoice_id: str
                The ID of the invoice that you want to delete.
        """

        url_endpoint = "/v1/invoices/{invoice_id}"
        headers = {}
        self._add_required_headers(headers)
        if not invoice_id:
            raise ValueError(
                "Parameter invoice_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{invoice_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, invoice_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteInvoice200ResponseModel._unmap(res)
        return res

    def finalize_invoice(self, invoice_id: str) -> FinalizeInvoice200ResponseModel:
        """
        Finalize Invoice
        Parameters:
        ----------
            invoice_id: str
                ID of the invoice you want to pay.
        """

        url_endpoint = "/v1/invoices/{invoice_id}/finalize"
        headers = {}
        self._add_required_headers(headers)
        if not invoice_id:
            raise ValueError(
                "Parameter invoice_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{invoice_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, invoice_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return FinalizeInvoice200ResponseModel._unmap(res)
        return res

    def pay_invoice(
        self, invoice_id: str, request_input: PayInvoiceRequestModel = None
    ) -> PayInvoice200ResponseModel:
        """
        payInvoice
        Parameters:
        ----------
            invoice_id: str
                ID of the invoice you want to pay.
        """

        if isinstance(request_input, dict):
            request_input = PayInvoiceRequestModel(**request_input)
        url_endpoint = "/v1/invoices/{invoice_id}/pay"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not invoice_id:
            raise ValueError(
                "Parameter invoice_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{invoice_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, invoice_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return PayInvoice200ResponseModel._unmap(res)
        return res

    def list_order(
        self, limit: str = None, ending_before: str = None, starting_after: str = None
    ) -> ListOrder200ResponseModel:
        """
        List Orders
        Parameters:
        ----------
            limit: str
                The maximum number of orders to return. Range - 1-100. Default is 10.
            ending_before: str
                The ID of the order created after the last order you want to retrieve.
            starting_after: str
                The ID of the order created before the first order you want to retrieve.
        """

        url_endpoint = "/v1/orders"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListOrder200ResponseModel._unmap(res)
        return res

    def create_order(
        self, request_input: CreateOrderRequestModel = None
    ) -> CreateOrder200ResponseModel:
        """
        Create an Order
        """

        if isinstance(request_input, dict):
            request_input = CreateOrderRequestModel(**request_input)
        url_endpoint = "/v1/orders"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateOrder200ResponseModel._unmap(res)
        return res

    def retrieve_order(self, order_id: str) -> RetrieveOrder200ResponseModel:
        """
        Retrieve an Order
        Parameters:
        ----------
            order_id: str
                ID of the order. String starting with order_.
        """

        url_endpoint = "/v1/orders/{order_id}"
        headers = {}
        self._add_required_headers(headers)
        if not order_id:
            raise ValueError(
                "Parameter order_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{order_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, order_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrieveOrder200ResponseModel._unmap(res)
        return res

    def update_order(
        self, request_input: UpdateOrderRequestModel, order_id: str
    ) -> UpdateOrder200ResponseModel:
        """
        Update an Order
        Parameters:
        ----------
            order_id: str
                ID of the order. String starting with order_.
        """

        if isinstance(request_input, dict):
            request_input = UpdateOrderRequestModel(**request_input)
        url_endpoint = "/v1/orders/{order_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not order_id:
            raise ValueError(
                "Parameter order_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{order_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, order_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateOrder200ResponseModel._unmap(res)
        return res

    def returns_order(
        self, request_input: ReturnsOrderRequestModel, order_id: str
    ) -> ReturnsOrder200ResponseModel:
        """
        Create a Return Against an Order
        Parameters:
        ----------
            order_id: str
                ID of the order. String starting with order_.
        """

        if isinstance(request_input, dict):
            request_input = ReturnsOrderRequestModel(**request_input)
        url_endpoint = "/v1/orders/{order_id}/returns"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not order_id:
            raise ValueError(
                "Parameter order_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{order_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, order_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ReturnsOrder200ResponseModel._unmap(res)
        return res

    def pay_order(
        self, request_input: PayOrderRequestModel, order_id: str
    ) -> PayOrder200ResponseModel:
        """
        Pay an order.
        Parameters:
        ----------
            order_id: str
                ID of the order. String starting with order_.
        """

        if isinstance(request_input, dict):
            request_input = PayOrderRequestModel(**request_input)
        url_endpoint = "/v1/orders/{order_id}/pay"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not order_id:
            raise ValueError(
                "Parameter order_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{order_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, order_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return PayOrder200ResponseModel._unmap(res)
        return res

    def list_order_return(
        self,
        limit: str = None,
        ending_before: str = None,
        starting_after: str = None,
        tokens: List[str] = None,
    ) -> ListOrderReturn200ResponseModel:
        """
        List Returns
        Parameters:
        ----------
            limit: str
                The maximum number of returns to list. Range - 1-100. Default is 10.
            ending_before: str
                The ID of the order created after the last order you want to retrieve a return from.
            starting_after: str
                The ID of the order created before the first order you want to retrieve a return from.
            tokens: list of str
                Filters the list for orders related to the specified order.
        """

        url_endpoint = "/v1/order_returns"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        if tokens:
            query_params.append(
                query_serializer.serialize_query("form", False, "tokens", tokens)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListOrderReturn200ResponseModel._unmap(res)
        return res

    def retrieve_order_return(
        self, order_returns_id: str
    ) -> RetrieveOrderReturn200ResponseModel:
        """
        Retrieve a Return
        Parameters:
        ----------
            order_returns_id: str
                ID of the return. String starting with orre_.
        """

        url_endpoint = "/v1/order_returns/{order_returns_id}"
        headers = {}
        self._add_required_headers(headers)
        if not order_returns_id:
            raise ValueError(
                "Parameter order_returns_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{order_returns_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, order_returns_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrieveOrderReturn200ResponseModel._unmap(res)
        return res

    def get_payment_methods_types_by_country(
        self, country_id: str, currency: str = None
    ) -> GetPaymentMethodsTypesByCountry200ResponseModel:
        """
        Retrieve a list of all payment methods available for a country
        Parameters:
        ----------
            country_id: str
                Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase.
            currency: str
                currency
        """

        url_endpoint = "/v1/payment_methods/countries/{country_id}"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not country_id:
            raise ValueError(
                "Parameter country_id is required, cannot be empty or blank."
            )
        validated_country_id = self._pattern_matching(
            country_id,
            "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
            "country_id",
        )
        url_endpoint = url_endpoint.replace(
            "{country_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, validated_country_id, None
                    )
                )
            ),
        )
        if currency:
            validated_currency = self._pattern_matching(
                currency,
                "^AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|BTN|BWP|BYR|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GGP|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|IMP|INR|IQD|IRR|ISK|JEP|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRO|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SPL|SRD|STD|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TVD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XDR|XOF|XPF|YER|ZAR|ZMW|ZWD$",
                "currency",
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "currency", validated_currency
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetPaymentMethodsTypesByCountry200ResponseModel._unmap(res)
        return res

    def get_payment_method_type_required_fields(
        self, pmt_id: str
    ) -> GetPaymentMethodTypeRequiredFields200ResponseModel:
        """
        Retrieve the required fields for a payment method
        Parameters:
        ----------
            pmt_id: str
                The type of the payment method.
        """

        url_endpoint = "/v1/payment_methods/{pmt_id}/required_fields"
        headers = {}
        self._add_required_headers(headers)
        if not pmt_id:
            raise ValueError("Parameter pmt_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{pmt_id}",
            quote(str(query_serializer.serialize_path("simple", False, pmt_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetPaymentMethodTypeRequiredFields200ResponseModel._unmap(res)
        return res

    def list_payments(
        self,
        created_after: str = None,
        created_before: str = None,
        customer: CustomerModel = None,
        destination_card: str = None,
        ending_before: str = None,
        ewallet: str = None,
        group: bool = None,
        invoice: str = None,
        limit: str = None,
        payment_method: str = None,
        order: str = None,
        starting_after: str = None,
        subscription: str = None,
        merchant_reference_id: str = None,
    ) -> ListPayments200ResponseModel:
        """
        List Payments
        Parameters:
        ----------
            created_after: str
                The ID of the payment created before the first payment you want to retrieve. String starting with payment_.
            created_before: str
                The ID of the payment created after the last payment you want to retrieve. String starting with payment_.
            customer: Customer
                Filters the list for payments related to the specified customer.
            destination_card: str
                Filters the list for payments related to the specified destination card.
            ending_before: str
                The ID of the payment created after the last payment you want to retrieve. String starting with payment_. Deprecated.
            ewallet: str
                Filters the list for payments related to the specified wallet.
            group: bool
                When true, includes only group payments in the response. When false, excludes group payments from the response. Default is false.
            invoice: str
                Filters according to the invoice. String starting with invoice_.
            limit: str
                The maximum number of payments to return. Range, 1-100. Default is 10.
            payment_method: str
                Filters the list for payments related to the specified payment method.
            order: str
                Filters the list for payments related to the specified order.
            starting_after: str
                The ID of a payment in the list. The list begins with the payment that was created next after the payment with this ID. Use this filter to get the next page of results. Relevant when ending_before is not used. String starting with payment_.
            subscription: str
                Filters the list for payments related to the specified subscription.
            merchant_reference_id: str
                Merchant-defined ID.
        """

        if isinstance(customer, dict):
            customer = CustomerModel(**customer)
        url_endpoint = "/v1/payments"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if created_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "created_after", created_after
                )
            )
        if created_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "created_before", created_before
                )
            )
        if customer:
            query_params.append(
                query_serializer.serialize_query("form", True, "customer", customer)
            )
        if destination_card:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "destination_card", destination_card
                )
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "ending_before", ending_before
                )
            )
        if ewallet:
            query_params.append(
                query_serializer.serialize_query("form", True, "ewallet", ewallet)
            )
        if group:
            query_params.append(
                query_serializer.serialize_query("form", True, "group", group)
            )
        if invoice:
            query_params.append(
                query_serializer.serialize_query("form", True, "invoice", invoice)
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", True, "limit", limit)
            )
        if payment_method:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "payment_method", payment_method
                )
            )
        if order:
            query_params.append(
                query_serializer.serialize_query("form", True, "order", order)
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "starting_after", starting_after
                )
            )
        if subscription:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "subscription", subscription
                )
            )
        if merchant_reference_id:
            query_params.append(
                query_serializer.serialize_query(
                    "form", True, "merchant_reference_id", merchant_reference_id
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListPayments200ResponseModel._unmap(res)
        return res

    def create_payment(
        self, request_input: CreatePaymentRequestModel
    ) -> CreatePayment200ResponseModel:
        """
        Create a payment
        """

        if isinstance(request_input, dict):
            request_input = CreatePaymentRequestGuardModel.return_one_of(request_input)
        url_endpoint = "/v1/payments"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreatePayment200ResponseModel._unmap(res)
        return res

    def retrieve_payment(self, payment_id: str) -> RetrievePayment200ResponseModel:
        """
        Retrieve Payment
        Parameters:
        ----------
            payment_id: str
                ID of the payment. String starting with 'payment_'.
        """

        url_endpoint = "/v1/payments/{payment_id}"
        headers = {}
        self._add_required_headers(headers)
        if not payment_id:
            raise ValueError(
                "Parameter payment_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{payment_id}",
            quote(
                str(query_serializer.serialize_path("simple", True, payment_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrievePayment200ResponseModel._unmap(res)
        return res

    def update_payment(
        self, request_input: UpdatePaymentRequestModel, payment_id: str
    ) -> UpdatePayment200ResponseModel:
        """
        Update Payment
        Parameters:
        ----------
            payment_id: str
                ID of the payment. String starting with payment_.
        """

        if isinstance(request_input, dict):
            request_input = UpdatePaymentRequestModel(**request_input)
        url_endpoint = "/v1/payments/{payment_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not payment_id:
            raise ValueError(
                "Parameter payment_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{payment_id}",
            quote(
                str(query_serializer.serialize_path("simple", True, payment_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdatePayment200ResponseModel._unmap(res)
        return res

    def cancel_payment(self, payment_id: str) -> CancelPayment200ResponseModel:
        """
        Cancel Payment
        Parameters:
        ----------
            payment_id: str
                ID of the payment. String starting with payment_.
        """

        url_endpoint = "/v1/payments/{payment_id}"
        headers = {}
        self._add_required_headers(headers)
        if not payment_id:
            raise ValueError(
                "Parameter payment_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{payment_id}",
            quote(
                str(query_serializer.serialize_path("simple", True, payment_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return CancelPayment200ResponseModel._unmap(res)
        return res

    def get_subscription_list(
        self,
        starting_after: str,
        billing: str = None,
        customer: str = None,
        status: str = None,
        product: str = None,
        ending_before: str = None,
        limit: str = None,
    ) -> GetSubscriptionList200ResponseModel:
        """
        List Subscriptions
        Parameters:
        ----------
            billing: str
                Method of billing. One of the following, pay_automatically, send_invoice.
            customer: str
                ID of the customer. String starting with cus_
            status: str
                Status of the subscription. One of the following, active, canceled, trialing
            product: str
                ID of a 'product' object. The product must have type set to service. String starting with product_. Filter for one product at a time.
            starting_after: str
                The ID of a record in the list. The list begins with the record that was created next after the record with this ID. Use this filter to get the next page of results. Relevant when ending_before is not used.
            ending_before: str
                The ID of a record in the list. The list ends with the last record that was created before the record with this ID. Use this filter to get the previous page of results.
            limit: str
                The maximum number of subscriptions to return. Range, 1-100. Default is 10.
        """

        url_endpoint = "/v1/payments/subscriptions"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if billing:
            query_params.append(
                query_serializer.serialize_query("form", False, "billing", billing)
            )
        if customer:
            query_params.append(
                query_serializer.serialize_query("form", False, "customer", customer)
            )
        if status:
            query_params.append(
                query_serializer.serialize_query("form", False, "status", status)
            )
        if product:
            query_params.append(
                query_serializer.serialize_query("form", False, "product", product)
            )
        if not starting_after:
            raise ValueError(
                "Parameter starting_after is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "starting_after", starting_after
            )
        )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetSubscriptionList200ResponseModel._unmap(res)
        return res

    def create_subscription(
        self, request_input: CreateSubscriptionRequestModel
    ) -> CreateSubscription200ResponseModel:
        """
        Create Subscription
        """

        if isinstance(request_input, dict):
            request_input = CreateSubscriptionRequestModel(**request_input)
        url_endpoint = "/v1/payments/subscriptions"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateSubscription200ResponseModel._unmap(res)
        return res

    def get_subscription(self, subscription_id: str) -> GetSubscription200ResponseModel:
        """
        Retrieve Subscription
        Parameters:
        ----------
            subscription_id: str
                ID of the subscription. String starting with sub_.
        """

        url_endpoint = "/v1/payments/subscriptions/{subscription_id}"
        headers = {}
        self._add_required_headers(headers)
        if not subscription_id:
            raise ValueError(
                "Parameter subscription_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{subscription_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, subscription_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetSubscription200ResponseModel._unmap(res)
        return res

    def update_subscription(
        self, request_input: UpdateSubscriptionRequestModel, subscription_id: str
    ) -> UpdateSubscription200ResponseModel:
        """
        Update Subscription
        Parameters:
        ----------
            subscription_id: str
                ID of the subscription. String starting with sub_.
        """

        if isinstance(request_input, dict):
            request_input = UpdateSubscriptionRequestModel(**request_input)
        url_endpoint = "/v1/payments/subscriptions/{subscription_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not subscription_id:
            raise ValueError(
                "Parameter subscription_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{subscription_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, subscription_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateSubscription200ResponseModel._unmap(res)
        return res

    def cancel_subscription(
        self, subscription_id: str, cancel_at_period_end: bool = None
    ) -> CancelSubscription200ResponseModel:
        """
        Cancel Subscription
        Parameters:
        ----------
            subscription_id: str
                ID of the subscription. String starting with sub_.
            cancel_at_period_end: bool
                < Determines when the subscription is canceled. true - Cancels the subscription at the end of the current period. false - Cancels the subscription immediately.
        """

        url_endpoint = "/v1/payments/subscriptions/{subscription_id}"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not subscription_id:
            raise ValueError(
                "Parameter subscription_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{subscription_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, subscription_id, None
                    )
                )
            ),
        )
        if cancel_at_period_end:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "cancel_at_period_end", cancel_at_period_end
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return CancelSubscription200ResponseModel._unmap(res)
        return res

    def delete_subscription_discount(
        self, subscription_id: str
    ) -> DeleteSubscriptionDiscount200ResponseModel:
        """
        Delete Discount from Subscription
        Parameters:
        ----------
            subscription_id: str
                ID of the subscription. String starting with sub_
        """

        url_endpoint = "/v1/payments/subscriptions/{subscription_id}/discount"
        headers = {}
        self._add_required_headers(headers)
        if not subscription_id:
            raise ValueError(
                "Parameter subscription_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{subscription_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, subscription_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteSubscriptionDiscount200ResponseModel._unmap(res)
        return res

    def list_plans(
        self,
        ending_before: float = None,
        limit: float = None,
        starting_after: str = None,
    ) -> ListPlans200ResponseModel:
        """
        List Plans
        Parameters:
        ----------
            ending_before: float
                The ID of the plan created after the last plan you want to retrieve.
            limit: float
                The maximum number of plans to return. Range 1-100. Default is 10.
            starting_after: str
                The ID of the plan created before the first plan you want to retrieve.
        """

        url_endpoint = "/v1/plans"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListPlans200ResponseModel._unmap(res)
        return res

    def create_plan(
        self, request_input: CreatePlanRequestModel
    ) -> CreatePlan200ResponseModel:
        """
        Create Plan Item
        """

        if isinstance(request_input, dict):
            request_input = CreatePlanRequestModel(**request_input)
        url_endpoint = "/v1/plans"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreatePlan200ResponseModel._unmap(res)
        return res

    def retrieve_plan(self, plan_id: str) -> RetrievePlan200ResponseModel:
        """
        Retrieve plan
        Parameters:
        ----------
            plan_id: str
                ID of the plan.
        """

        url_endpoint = "/v1/plans/{plan_id}"
        headers = {}
        self._add_required_headers(headers)
        if not plan_id:
            raise ValueError("Parameter plan_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{plan_id}",
            quote(str(query_serializer.serialize_path("simple", False, plan_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrievePlan200ResponseModel._unmap(res)
        return res

    def update_plan(
        self, request_input: UpdatePlanRequestModel, plan_id: str
    ) -> UpdatePlan200ResponseModel:
        """
        Update Plan
        Parameters:
        ----------
            plan_id: str
                ID of the plan.
        """

        if isinstance(request_input, dict):
            request_input = UpdatePlanRequestModel(**request_input)
        url_endpoint = "/v1/plans/{plan_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not plan_id:
            raise ValueError("Parameter plan_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{plan_id}",
            quote(str(query_serializer.serialize_path("simple", False, plan_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdatePlan200ResponseModel._unmap(res)
        return res

    def delete_plan(self, plan_id: str) -> DeletePlan200ResponseModel:
        """
        Delete Plan
        Parameters:
        ----------
            plan_id: str
                ID of the plan.
        """

        url_endpoint = "/v1/plans/{plan_id}"
        headers = {}
        self._add_required_headers(headers)
        if not plan_id:
            raise ValueError("Parameter plan_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{plan_id}",
            quote(str(query_serializer.serialize_path("simple", False, plan_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeletePlan200ResponseModel._unmap(res)
        return res

    def get_products_list(
        self,
        ending_before: float = None,
        limit: float = None,
        starting_after: str = None,
    ) -> GetProductsList200ResponseModel:
        """
        List Products
        Parameters:
        ----------
            ending_before: float
                The ID of the products created after the last product you want to retrieve.
            limit: float
                The maximum number of products to return. Range 1-100. Default is 10.
            starting_after: str
                The ID of the product created before the first products you want to retrieve.
        """

        url_endpoint = "/v1/products"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetProductsList200ResponseModel._unmap(res)
        return res

    def create_product(
        self, request_input: CreateProductRequestModel
    ) -> CreateProduct200ResponseModel:
        """
        Create Product
        """

        if isinstance(request_input, dict):
            request_input = CreateProductRequestModel(**request_input)
        url_endpoint = "/v1/products"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateProduct200ResponseModel._unmap(res)
        return res

    def get_product(self, products_id: str) -> GetProduct200ResponseModel:
        """
        Retrieve Product
        Parameters:
        ----------
            products_id: str
                ID of the product.
        """

        url_endpoint = "/v1/products/{products_id}"
        headers = {}
        self._add_required_headers(headers)
        if not products_id:
            raise ValueError(
                "Parameter products_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{products_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, products_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetProduct200ResponseModel._unmap(res)
        return res

    def update_product(
        self, products_id: str, request_input: UpdateProductRequestModel = None
    ) -> UpdateProduct200ResponseModel:
        """
        Update Product
        Parameters:
        ----------
            products_id: str
                ID of the product.
        """

        if isinstance(request_input, dict):
            request_input = UpdateProductRequestModel(**request_input)
        url_endpoint = "/v1/products/{products_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not products_id:
            raise ValueError(
                "Parameter products_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{products_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, products_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateProduct200ResponseModel._unmap(res)
        return res

    def delete_product(self, products_id: str) -> DeleteProduct200ResponseModel:
        """
        Delete Product
        Parameters:
        ----------
            products_id: str
                ID of the product.
        """

        url_endpoint = "/v1/products/{products_id}"
        headers = {}
        self._add_required_headers(headers)
        if not products_id:
            raise ValueError(
                "Parameter products_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{products_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, products_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteProduct200ResponseModel._unmap(res)
        return res

    def all_refunds(
        self, ending_before: str = None, limit: str = None, starting_after: str = None
    ) -> AllRefunds200ResponseModel:
        """
        List Refunds
        Parameters:
        ----------
            ending_before: str
                The ID of the refund created after the last refund you want to retrieve. String starting with refund_.
            limit: str
                The maximum number of refunds to return. Range, 1-100. Default is 10.
            starting_after: str
                The ID of the refund created before the first refund you want to retrieve. String starting with refund_.
        """

        url_endpoint = "/v1/refunds"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return AllRefunds200ResponseModel._unmap(res)
        return res

    def request_total_create_refund(
        self, request_input: RequestTotalCreateRefundRequestModel
    ) -> RequestTotalCreateRefund200ResponseModel:
        """
        Create Refund
        """

        if isinstance(request_input, dict):
            request_input = RequestTotalCreateRefundRequestModel(**request_input)
        url_endpoint = "/v1/refunds"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return RequestTotalCreateRefund200ResponseModel._unmap(res)
        return res

    def simulate_complete_refund(
        self, request_input: SimulateCompleteRefundRequestModel
    ) -> SimulateCompleteRefund200ResponseModel:
        """
        Complete Refund
        """

        if isinstance(request_input, dict):
            request_input = SimulateCompleteRefundRequestModel(**request_input)
        url_endpoint = "/v1/refunds/complete"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return SimulateCompleteRefund200ResponseModel._unmap(res)
        return res

    def refund_group_payment(
        self, request_input: RefundGroupPaymentRequestModel
    ) -> RefundGroupPayment200ResponseModel:
        """
        Create Group Refund
        """

        if isinstance(request_input, dict):
            request_input = RefundGroupPaymentRequestModel(**request_input)
        url_endpoint = "/v1/refunds/group_payments"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return RefundGroupPayment200ResponseModel._unmap(res)
        return res

    def refund_by_token(self, refund_id: str) -> RefundByToken200ResponseModel:
        """
        Retrieve Refund
        Parameters:
        ----------
            refund_id: str
                ID of the 'refund' object you want to retrieve. String starting with refund_.
        """

        url_endpoint = "/v1/refunds/{refund_id}"
        headers = {}
        self._add_required_headers(headers)
        if not refund_id:
            raise ValueError(
                "Parameter refund_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{refund_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, refund_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RefundByToken200ResponseModel._unmap(res)
        return res

    def update_refund(
        self, request_input: UpdateRefundRequestModel, refund_id: str
    ) -> UpdateRefund200ResponseModel:
        """
        Update Refund
        Parameters:
        ----------
            refund_id: str
                ID of the 'refund' object you want to retrieve. String starting with refund_.
        """

        if isinstance(request_input, dict):
            request_input = UpdateRefundRequestModel(**request_input)
        url_endpoint = "/v1/refunds/{refund_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not refund_id:
            raise ValueError(
                "Parameter refund_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{refund_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, refund_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateRefund200ResponseModel._unmap(res)
        return res

    def list_subscription_item(
        self,
        ending_before: float = None,
        limit: float = None,
        starting_after: str = None,
        subscription: str = None,
    ) -> ListSubscriptionItem200ResponseModel:
        """
        List Subscription Items
        Parameters:
        ----------
            ending_before: float
                The ID of the subscription item created after the last subscription item you want to retrieve.
            limit: float
                The maximum number of subscription items to return. Range 1-100. Default is 10.
            starting_after: str
                The ID of the subscription item created before the first subscription item you want to retrieve.
            subscription: str
                ID of the subscription.
        """

        url_endpoint = "/v1/subscription_items"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        if subscription:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "subscription", subscription
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListSubscriptionItem200ResponseModel._unmap(res)
        return res

    def create_subscription_item(
        self, request_input: CreateSubscriptionItemRequestModel
    ) -> CreateSubscriptionItem200ResponseModel:
        """
        Create Subscription Item
        """

        if isinstance(request_input, dict):
            request_input = CreateSubscriptionItemRequestModel(**request_input)
        url_endpoint = "/v1/subscription_items"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateSubscriptionItem200ResponseModel._unmap(res)
        return res

    def retrieve_subscription_item(
        self, subscription_item_id: str
    ) -> RetrieveSubscriptionItem200ResponseModel:
        """
        Retrieve Subscription Item
        Parameters:
        ----------
            subscription_item_id: str
                ID of the subscription item. String starting with subi_.
        """

        url_endpoint = "/v1/subscription_items/{subscription_item_id}"
        headers = {}
        self._add_required_headers(headers)
        if not subscription_item_id:
            raise ValueError(
                "Parameter subscription_item_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{subscription_item_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, subscription_item_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrieveSubscriptionItem200ResponseModel._unmap(res)
        return res

    def update_subscription_item(
        self,
        request_input: UpdateSubscriptionItemRequestModel,
        subscription_item_id: str,
    ) -> UpdateSubscriptionItem200ResponseModel:
        """
        Update Subscription Item
        Parameters:
        ----------
            subscription_item_id: str
                ID of the subscription item. String starting with subi_.
        """

        if isinstance(request_input, dict):
            request_input = UpdateSubscriptionItemRequestModel(**request_input)
        url_endpoint = "/v1/subscription_items/{subscription_item_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not subscription_item_id:
            raise ValueError(
                "Parameter subscription_item_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{subscription_item_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, subscription_item_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateSubscriptionItem200ResponseModel._unmap(res)
        return res

    def delete_subscription_item(
        self, subscription_item_id: str
    ) -> DeleteSubscriptionItem200ResponseModel:
        """
        Delete Subscription Item
        Parameters:
        ----------
            subscription_item_id: str
                ID of the subscription item. String starting with subi_.
        """

        url_endpoint = "/v1/subscription_items/{subscription_item_id}"
        headers = {}
        self._add_required_headers(headers)
        if not subscription_item_id:
            raise ValueError(
                "Parameter subscription_item_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{subscription_item_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, subscription_item_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteSubscriptionItem200ResponseModel._unmap(res)
        return res

    def usage_record_summaries(
        self,
        subscription_item_id: str,
        limit: float = None,
        ending_before: float = None,
        starting_after: float = None,
    ) -> UsageRecordSummaries200ResponseModel:
        """
        Create Usage Record
        Parameters:
        ----------
            subscription_item_id: str
                ID of the subscription item. String starting with subi_.
            limit: float
                The maximum number of usage records that are returned. Range is 1-100. Default is 10.
            ending_before: float
                The latest date and time of the returned usage records. Format is in Unix time.
            starting_after: float
                The earliest date and time of the returned usage records. Format is in Unix time.
        """

        url_endpoint = (
            "/v1/subscription_items/{subscription_item_id}/usage_record_summaries"
        )
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not subscription_item_id:
            raise ValueError(
                "Parameter subscription_item_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{subscription_item_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, subscription_item_id, None
                    )
                )
            ),
        )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return UsageRecordSummaries200ResponseModel._unmap(res)
        return res

    def create_subscription_item_usage_record(
        self,
        request_input: CreateSubscriptionItemUsageRecordRequestModel,
        subscription_item_id: str,
    ) -> CreateSubscriptionItemUsageRecord200ResponseModel:
        """
        Create Usage Record
        Parameters:
        ----------
            subscription_item_id: str
                ID of the subscription item. String starting with subi_.
        """

        if isinstance(request_input, dict):
            request_input = CreateSubscriptionItemUsageRecordRequestModel(
                **request_input
            )
        url_endpoint = "/v1/subscription_items/{subscription_item_id}/usage_records"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not subscription_item_id:
            raise ValueError(
                "Parameter subscription_item_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{subscription_item_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, subscription_item_id, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateSubscriptionItemUsageRecord200ResponseModel._unmap(res)
        return res

    def get_subscription_discount_by_id(
        self, discount_id: str
    ) -> GetSubscriptionDiscountById200ResponseModel:
        """
        Retrieve an discount
        Parameters:
        ----------
            discount_id: str
                discount Id
        """

        url_endpoint = "/v1/subscriptions/discount/{discount_id}"
        headers = {}
        self._add_required_headers(headers)
        if not discount_id:
            raise ValueError(
                "Parameter discount_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{discount_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, discount_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetSubscriptionDiscountById200ResponseModel._unmap(res)
        return res

    def retrieve_sku(self, sku_id: str) -> RetrieveSku200ResponseModel:
        """
        Retrieve SKU.
        Parameters:
        ----------
            sku_id: str
                ID of the 'sku' object. String starting with sku_.
        """

        url_endpoint = "/v1/skus/{sku_id}"
        headers = {}
        self._add_required_headers(headers)
        if not sku_id:
            raise ValueError("Parameter sku_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{sku_id}",
            quote(str(query_serializer.serialize_path("simple", False, sku_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrieveSku200ResponseModel._unmap(res)
        return res

    def update_sku(
        self, sku_id: str, request_input: UpdateSkuRequestModel = None
    ) -> UpdateSku200ResponseModel:
        """
        Retrieve SKU.
        Parameters:
        ----------
            sku_id: str
                ID of the 'sku' object. String starting with sku_.
        """

        if isinstance(request_input, dict):
            request_input = UpdateSkuRequestModel(**request_input)
        url_endpoint = "/v1/skus/{sku_id}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not sku_id:
            raise ValueError("Parameter sku_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{sku_id}",
            quote(str(query_serializer.serialize_path("simple", False, sku_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateSku200ResponseModel._unmap(res)
        return res

    def delete_sku(self, sku_id: str) -> DeleteSku200ResponseModel:
        """
        Delete SKU.
        Parameters:
        ----------
            sku_id: str
                ID of the 'sku' object. String starting with sku_.
        """

        url_endpoint = "/v1/skus/{sku_id}"
        headers = {}
        self._add_required_headers(headers)
        if not sku_id:
            raise ValueError("Parameter sku_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{sku_id}",
            quote(str(query_serializer.serialize_path("simple", False, sku_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteSku200ResponseModel._unmap(res)
        return res

    def list_sku(
        self,
        active: bool = None,
        starting_after: float = None,
        ending_before: float = None,
        limit: float = None,
    ) -> ListSku200ResponseModel:
        """
        List SKUs.
        Parameters:
        ----------
            active: bool
                Determines whether the query returns active SKUs or inactive SKUs. Default is true.
            starting_after: float
                The ID of the SKU created before the first SKU you want to retrieve.
            ending_before: float
                The ID of the SKU created after the last SKU you want to retrieve.
            limit: float
                The maximum number of SKUs to return. Range 1-100. Default is 10.
        """

        url_endpoint = "/v1/skus"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if active:
            query_params.append(
                query_serializer.serialize_query("form", False, "active", active)
            )
        if starting_after:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "starting_after", starting_after
                )
            )
        if ending_before:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "ending_before", ending_before
                )
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListSku200ResponseModel._unmap(res)
        return res

    def create_sku(
        self, request_input: CreateSkuRequestModel = None
    ) -> CreateSku200ResponseModel:
        """
        Create SKU
        """

        if isinstance(request_input, dict):
            request_input = CreateSkuRequestModel(**request_input)
        url_endpoint = "/v1/skus"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateSku200ResponseModel._unmap(res)
        return res
