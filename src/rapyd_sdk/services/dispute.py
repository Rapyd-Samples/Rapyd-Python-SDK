from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.inline_response_200_42 import InlineResponse200_42
from ..models.inline_response_200_41 import InlineResponse200_41
from ..models.get_disputes_list_by_org_id_status import GetDisputesListByOrgIdStatus


class DisputeService(BaseService):

    @cast_models
    def get_disputes_list_by_org_id(
        self,
        starting_after: str = None,
        ending_before: str = None,
        limit: str = None,
        status: GetDisputesListByOrgIdStatus = None,
        payment: str = None,
    ) -> InlineResponse200_41:
        """Retrieve a detailed list of 'dispute' objects.

        :param starting_after: The ID of the dispute created before the first dispute you want to retrieve. String starting with dispute_., defaults to None
        :type starting_after: str, optional
        :param ending_before: The ID of the dispute created after the last dispute you want to retrieve. String starting with dispute_., defaults to None
        :type ending_before: str, optional
        :param limit: The maximum number of disputes to return. Range is 1-100. Default is 10., defaults to None
        :type limit: str, optional
        :param status: Filters the list for disputes with the specified dispute status., defaults to None
        :type status: GetDisputesListByOrgIdStatus, optional
        :param payment: The ID of the payment that is linked to the dispute. String starting with payment_., defaults to None
        :type payment: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: disputes fetched successfuly
        :rtype: InlineResponse200_41
        """

        Validator(str).is_optional().validate(starting_after)
        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().pattern("([1-9]|[1-9]\d|100)").validate(limit)
        Validator(GetDisputesListByOrgIdStatus).is_optional().validate(status)
        Validator(str).is_optional().validate(payment)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/disputes", self.get_default_headers())
            .add_query("starting_after", starting_after)
            .add_query("ending_before", ending_before)
            .add_query("limit", limit)
            .add_query("status", status)
            .add_query("payment", payment)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_41._unmap(response)

    @cast_models
    def get_dispute(self, dispute_id: str) -> InlineResponse200_42:
        """Retrieve the details of a dispute.

        :param dispute_id: ID of the dispute you want to retrieve. String starting with dispute_.
        :type dispute_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Get dispute details by dispute id
        :rtype: InlineResponse200_42
        """

        Validator(str).validate(dispute_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/disputes/{{disputeId}}", self.get_default_headers()
            )
            .add_path("disputeId", dispute_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_42._unmap(response)
