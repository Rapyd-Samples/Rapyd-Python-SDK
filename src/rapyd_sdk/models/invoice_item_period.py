from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class InvoiceItemPeriod(BaseModel):
    """InvoiceItemPeriod

    :param start: First date in the period covered by the invoice, in Unix time. Response only., defaults to None
    :type start: str, optional
    :param end: Last date in the period covered by the invoice, in Unix time. Response only., defaults to None
    :type end: str, optional
    """

    def __init__(self, start: str = None, end: str = None):
        """InvoiceItemPeriod

        :param start: First date in the period covered by the invoice, in Unix time. Response only., defaults to None
        :type start: str, optional
        :param end: Last date in the period covered by the invoice, in Unix time. Response only., defaults to None
        :type end: str, optional
        """
        self.start = self._define_str("start", start, nullable=True)
        self.end = self._define_str("end", end, nullable=True)
