from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.v1_plans_body import V1PlansBody
from ..models.utils.cast_models import cast_models
from ..models.plans_plan_id_body import PlansPlanIdBody
from ..models.inline_response_200_60 import InlineResponse200_60
from ..models.inline_response_200_59 import InlineResponse200_59
from ..models.inline_response_200_58 import InlineResponse200_58


class SubscriptionPlanService(BaseService):

    @cast_models
    def list_plans(
        self,
        ending_before: float = None,
        limit: float = None,
        starting_after: str = None,
    ) -> InlineResponse200_58:
        """Retrieve a list of all plans. Use the optional query parameters to filter the results. You can filter the results further by specifying one or more Plan fields as additional query parameters.

        :param ending_before: The ID of the plan created after the last plan you want to retrieve., defaults to None
        :type ending_before: float, optional
        :param limit: The maximum number of plans to return. Range 1-100. Default is 10., defaults to None
        :type limit: float, optional
        :param starting_after: The ID of the plan created before the first plan you want to retrieve., defaults to None
        :type starting_after: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of plans
        :rtype: InlineResponse200_58
        """

        Validator(float).is_optional().validate(ending_before)
        Validator(float).is_optional().validate(limit)
        Validator(str).is_optional().validate(starting_after)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/plans", self.get_default_headers())
            .add_query("ending_before", ending_before, explode=False)
            .add_query("limit", limit, explode=False)
            .add_query("starting_after", starting_after, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_58._unmap(response)

    @cast_models
    def create_plan(self, request_body: V1PlansBody) -> InlineResponse200_59:
        """Create a pricing plan for services.

        :param request_body: The request body.
        :type request_body: V1PlansBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created plan
        :rtype: InlineResponse200_59
        """

        Validator(V1PlansBody).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/plans", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_59._unmap(response)

    @cast_models
    def retrieve_plan(self, plan_id: str) -> InlineResponse200_59:
        """Retrieve the details of a pricing plan for services.

        :param plan_id: ID of the plan.
        :type plan_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The Plan
        :rtype: InlineResponse200_59
        """

        Validator(str).validate(plan_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/plans/{{plan_id}}", self.get_default_headers()
            )
            .add_path("plan_id", plan_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_59._unmap(response)

    @cast_models
    def update_plan(
        self, request_body: PlansPlanIdBody, plan_id: str
    ) -> InlineResponse200_59:
        """Change or modify a pricing plan for services. You can update a plan's nickname or metadata.

        :param request_body: The request body.
        :type request_body: PlansPlanIdBody
        :param plan_id: ID of the plan.
        :type plan_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The Plan after updated
        :rtype: InlineResponse200_59
        """

        Validator(PlansPlanIdBody).validate(request_body)
        Validator(str).validate(plan_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/plans/{{plan_id}}", self.get_default_headers()
            )
            .add_path("plan_id", plan_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_59._unmap(response)

    @cast_models
    def delete_plan(self, plan_id: str) -> InlineResponse200_60:
        """Delete a pricing plan for services.

        :param plan_id: ID of the plan.
        :type plan_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Rapyd response with operation result, and plan id
        :rtype: InlineResponse200_60
        """

        Validator(str).validate(plan_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/plans/{{plan_id}}", self.get_default_headers()
            )
            .add_path("plan_id", plan_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_60._unmap(response)
