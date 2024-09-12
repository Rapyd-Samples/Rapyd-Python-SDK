from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class OrderResponseStatusTransitions(BaseModel):
    """Indicates the last time in Unix time that the order transitioned to one of the following statuses. A zero value for a status indicates that the order has never transitioned to it.

    :param canceled: canceled, defaults to None
    :type canceled: float, optional
    :param fulfilled: fulfilled, defaults to None
    :type fulfilled: float, optional
    :param paid: paid, defaults to None
    :type paid: float, optional
    :param returned: returned, defaults to None
    :type returned: float, optional
    :param pending: pending, defaults to None
    :type pending: float, optional
    :param partial: partial, defaults to None
    :type partial: float, optional
    """

    def __init__(
        self,
        canceled: float = None,
        fulfilled: float = None,
        paid: float = None,
        returned: float = None,
        pending: float = None,
        partial: float = None,
    ):
        """Indicates the last time in Unix time that the order transitioned to one of the following statuses. A zero value for a status indicates that the order has never transitioned to it.

        :param canceled: canceled, defaults to None
        :type canceled: float, optional
        :param fulfilled: fulfilled, defaults to None
        :type fulfilled: float, optional
        :param paid: paid, defaults to None
        :type paid: float, optional
        :param returned: returned, defaults to None
        :type returned: float, optional
        :param pending: pending, defaults to None
        :type pending: float, optional
        :param partial: partial, defaults to None
        :type partial: float, optional
        """
        self.canceled = self._define_number("canceled", canceled, nullable=True)
        self.fulfilled = self._define_number("fulfilled", fulfilled, nullable=True)
        self.paid = self._define_number("paid", paid, nullable=True)
        self.returned = self._define_number("returned", returned, nullable=True)
        self.pending = self._define_number("pending", pending, nullable=True)
        self.partial = self._define_number("partial", partial, nullable=True)
