from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import (
    InlineResponse200_69,
    InlineResponse200_70,
    InlineResponse200_71,
    PlansPlanIdBody,
    V1PlansBody,
)


class SubscriptionPlanService(BaseService):

    @cast_models
    def list_plans(
        self, ending_before: str = None, limit: str = None, starting_after: str = None
    ) -> InlineResponse200_69:
        """Retrieve a list of all plans. Use the optional query parameters to filter the results. You can filter the results further by specifying one or more Plan fields as additional query parameters.

        :param ending_before: The ID of the plan created after the last plan you want to retrieve., defaults to None
        :type ending_before: str, optional
        :param limit: The maximum number of plans to return. Range 1-100. Default is 10., defaults to None
        :type limit: str, optional
        :param starting_after: The ID of the plan created before the first plan you want to retrieve., defaults to None
        :type starting_after: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of plans
        :rtype: InlineResponse200_69
        """

        Validator(str).is_optional().validate(ending_before)
        Validator(str).is_optional().validate(limit)
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
        return InlineResponse200_69._unmap(response)

    @cast_models
    def create_plan(self, request_body: V1PlansBody) -> InlineResponse200_70:
        """Create a pricing plan for services.

        :param request_body: The request body.
        :type request_body: V1PlansBody
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The created plan
        :rtype: InlineResponse200_70
        """

        Validator(V1PlansBody).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/plans", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_70._unmap(response)

    @cast_models
    def retrieve_plan(self, plan_id: str) -> InlineResponse200_70:
        """Retrieve the details of a pricing plan for services.

        :param plan_id: ID of the plan.
        :type plan_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The Plan
        :rtype: InlineResponse200_70
        """

        Validator(str).validate(plan_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/plans/{{planId}}", self.get_default_headers()
            )
            .add_path("planId", plan_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_70._unmap(response)

    @cast_models
    def update_plan(
        self, request_body: PlansPlanIdBody, plan_id: str
    ) -> InlineResponse200_70:
        """Change or modify a pricing plan for services. You can update a plan's nickname or metadata.

        :param request_body: The request body.
        :type request_body: PlansPlanIdBody
        :param plan_id: ID of the plan.
        :type plan_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The Plan after updated
        :rtype: InlineResponse200_70
        """

        Validator(PlansPlanIdBody).validate(request_body)
        Validator(str).validate(plan_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/plans/{{planId}}", self.get_default_headers()
            )
            .add_path("planId", plan_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_70._unmap(response)

    @cast_models
    def delete_plan(self, plan_id: str) -> InlineResponse200_71:
        """Delete a pricing plan for services.

        :param plan_id: ID of the plan.
        :type plan_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Rapyd response with operation result, and plan id
        :rtype: InlineResponse200_71
        """

        Validator(str).validate(plan_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/plans/{{planId}}", self.get_default_headers()
            )
            .add_path("planId", plan_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return InlineResponse200_71._unmap(response)
