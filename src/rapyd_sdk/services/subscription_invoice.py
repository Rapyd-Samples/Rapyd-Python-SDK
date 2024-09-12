from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.invoices_invoice_id_body import InvoicesInvoiceIdBody
from ..models.invoice_id_pay_body import InvoiceIdPayBody
from ..models.inline_response_200_45 import InlineResponse200_45
from ..models.inline_response_200_44 import InlineResponse200_44
from ..models.inline_response_200_43 import InlineResponse200_43
from ..models.inline_response_200_36 import InlineResponse200_36
from ..models.customer import Customer


class SubscriptionInvoiceService(BaseService):

    @cast_models
    def list_invoices(
        self,
        customer: Customer = None,
        date_: str = None,
        due_date: str = None,
        ending_before: str = None,
        limit: str = None,
        starting_after: str = None,
        subscription: bool = None,
    ) -> InlineResponse200_43:
        """Retrieve the basic data of an invoice, with individual invoice lines.

        :param customer: ID of the customer. String starting with cus_., defaults to None
        :type customer: Customer, optional
        :param date_: Date that the invoice was created., defaults to None
        :type date_: str, optional
        :param due_date: The date payment is due on this invoice. This value is calculated from the date the invoice is created, plus the number of days specified in the days_until_due field. Format is in Unix time., defaults to None
        :type due_date: str, optional
        :param ending_before: The ID of the invoice created after the last invoice you want to retrieve. card., defaults to None
        :type ending_before: str, optional
        :param limit: The maximum number of invoices to return. Range 1-100. Default is 10., defaults to None
        :type limit: str, optional
        :param starting_after: The ID of the invoice created before the first invoice you want to retrieve., defaults to None
        :type starting_after: str, optional
        :param subscription: ID of the subscription. String starting with sub_., defaults to None
        :type subscription: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Invoices Fetched successfully
        :rtype: InlineResponse200_43
        """

        Validator(Customer).is_optional().validate(customer)
        Validator(str).is_optional().validate(date_)
        Validator(str).is_optional().validate(due_date)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(limit)
        Validator(str).is_optional().validate(starting_after)
        Validator(bool).is_optional().validate(subscription)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/invoices", self.get_default_headers())
            .add_query("customer", customer)
            .add_query("date", date_)
            .add_query("due_date", due_date)
            .add_query("ending_before", ending_before)
            .add_query("limit", limit)
            .add_query("starting_after", starting_after)
            .add_query("subscription", subscription)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_43._unmap(response)

    @cast_models
    def retrieve_invoice(self, invoice_id: str) -> InlineResponse200_44:
        """Retrieve the basic data of an invoice, with individual invoice lines.

        :param invoice_id: The ID of the invoice that you want to retrieve.
        :type invoice_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Invoice Fetched successfully
        :rtype: InlineResponse200_44
        """

        Validator(str).validate(invoice_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/invoices/{{invoiceId}}", self.get_default_headers()
            )
            .add_path("invoiceId", invoice_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_44._unmap(response)

    @cast_models
    def update_invoice(
        self, invoice_id: str, request_body: InvoicesInvoiceIdBody = None
    ) -> InlineResponse200_43:
        """Change or modify an invoice. You can modify the invoice when its status is draft.

        :param request_body: The request body., defaults to None
        :type request_body: InvoicesInvoiceIdBody, optional
        :param invoice_id: The ID of the invoice that you want to updated.
        :type invoice_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Invoice updated successfully
        :rtype: InlineResponse200_43
        """

        Validator(InvoicesInvoiceIdBody).is_optional().validate(request_body)
        Validator(str).validate(invoice_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/invoices/{{invoiceId}}", self.get_default_headers()
            )
            .add_path("invoiceId", invoice_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_43._unmap(response)

    @cast_models
    def delete_invoice(self, invoice_id: str) -> InlineResponse200_36:
        """Delete an invoice. You can delete an invoice when status is draft.

        :param invoice_id: The ID of the invoice that you want to delete.
        :type invoice_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Invoice deleted successfully
        :rtype: InlineResponse200_36
        """

        Validator(str).validate(invoice_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/invoices/{{invoiceId}}", self.get_default_headers()
            )
            .add_path("invoiceId", invoice_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_36._unmap(response)

    @cast_models
    def finalize_invoice(self, invoice_id: str) -> InlineResponse200_45:
        """Finalize an invoice.Invoices are initially created with a draft status, and this is the only state in which an invoice can be finalized. When an invoice is ready to be paid, finalize it. This sets its status to open. Subscriptions automatically create draft invoices during each billing cycle, which are then automatically finalized. When an invoice is finalized, it can no longer be deleted and its final status can be one of the following - Paid Uncollectible* Void. An invoice can be finalized only one time.

        :param invoice_id: ID of the invoice you want to pay.
        :type invoice_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Finalized Invoice,
        :rtype: InlineResponse200_45
        """

        Validator(str).validate(invoice_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/invoices/{{invoiceId}}/finalize",
                self.get_default_headers(),
            )
            .add_path("invoiceId", invoice_id)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_45._unmap(response)

    @cast_models
    def pay_invoice(
        self, invoice_id: str, request_body: InvoiceIdPayBody = None
    ) -> InlineResponse200_44:
        """Make a payment against an invoice.

        :param request_body: The request body., defaults to None
        :type request_body: InvoiceIdPayBody, optional
        :param invoice_id: ID of the invoice you want to pay.
        :type invoice_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The Invoice
        :rtype: InlineResponse200_44
        """

        Validator(InvoiceIdPayBody).is_optional().validate(request_body)
        Validator(str).validate(invoice_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/invoices/{{invoiceId}}/pay",
                self.get_default_headers(),
            )
            .add_path("invoiceId", invoice_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_44._unmap(response)
