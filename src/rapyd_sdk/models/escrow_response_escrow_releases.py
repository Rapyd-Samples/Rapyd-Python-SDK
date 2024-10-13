from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .escrow_response_escrow_releases_data import EscrowResponseEscrowReleasesData


@JsonMap({})
class EscrowResponseEscrowReleases(BaseModel):
    """Array of objects that describe individual releases.

    :param data: Array of objects that describe individual escrow releases., defaults to None
    :type data: EscrowResponseEscrowReleasesData, optional
    :param has_more: Indicates that the number of escrow releases is greater than the number returned in the response., defaults to None
    :type has_more: bool, optional
    :param total_count: Number of escrow releases., defaults to None
    :type total_count: float, optional
    :param url: URL for the record of all escrow releases for this payment., defaults to None
    :type url: str, optional
    """

    def __init__(
        self,
        data: EscrowResponseEscrowReleasesData = None,
        has_more: bool = None,
        total_count: float = None,
        url: str = None,
    ):
        """Array of objects that describe individual releases.

        :param data: Array of objects that describe individual escrow releases., defaults to None
        :type data: EscrowResponseEscrowReleasesData, optional
        :param has_more: Indicates that the number of escrow releases is greater than the number returned in the response., defaults to None
        :type has_more: bool, optional
        :param total_count: Number of escrow releases., defaults to None
        :type total_count: float, optional
        :param url: URL for the record of all escrow releases for this payment., defaults to None
        :type url: str, optional
        """
        self.data = self._define_object(data, EscrowResponseEscrowReleasesData)
        self.has_more = has_more
        self.total_count = self._define_number(
            "total_count", total_count, nullable=True
        )
        self.url = self._define_str("url", url, nullable=True)
