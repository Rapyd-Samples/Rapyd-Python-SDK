from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class InlineResponse200_90DataRenewResult(BaseModel):
    """InlineResponse200_90DataRenewResult

    :param redirect_to_app_type_page: redirect_to_app_type_page, defaults to None
    :type redirect_to_app_type_page: bool, optional
    :param need_to_renew: need_to_renew, defaults to None
    :type need_to_renew: bool, optional
    """

    def __init__(
        self, redirect_to_app_type_page: bool = None, need_to_renew: bool = None
    ):
        """InlineResponse200_90DataRenewResult

        :param redirect_to_app_type_page: redirect_to_app_type_page, defaults to None
        :type redirect_to_app_type_page: bool, optional
        :param need_to_renew: need_to_renew, defaults to None
        :type need_to_renew: bool, optional
        """
        self.redirect_to_app_type_page = redirect_to_app_type_page
        self.need_to_renew = need_to_renew
