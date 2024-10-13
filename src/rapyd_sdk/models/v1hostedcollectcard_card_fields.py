from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class V1hostedcollectcardCardFields(BaseModel):
    """Contains details about the card.

    :param recurrence_type: Specifies the primary intended purpose of the saved payment method. See Saving a European Card While Creating a Payment. One of the following values: <BR> * **installment** - Regular payments for a defined number of payment cycles. <BR> * **recurring** - Regular payments for an indefinite period. <BR> * **unscheduled** - Individual unrelated payments., defaults to None
    :type recurrence_type: str, optional
    """

    def __init__(self, recurrence_type: str = None):
        """Contains details about the card.

        :param recurrence_type: Specifies the primary intended purpose of the saved payment method. See Saving a European Card While Creating a Payment. One of the following values: <BR> * **installment** - Regular payments for a defined number of payment cycles. <BR> * **recurring** - Regular payments for an indefinite period. <BR> * **unscheduled** - Individual unrelated payments., defaults to None
        :type recurrence_type: str, optional
        """
        self.recurrence_type = self._define_str(
            "recurrence_type", recurrence_type, nullable=True
        )
