from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class AddressResponse(BaseModel):
    """AddressResponse

    :param canton: Name of the canton administrative subdivision, as used in banking., defaults to None
    :type canton: str, optional
    :param city: City portion of the address., defaults to None
    :type city: str, optional
    :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country., defaults to None
    :type country: str, optional
    :param created_at: Time of creation of the object, in Unix time., defaults to None
    :type created_at: float, optional
    :param district: Name of the district administrative subdivision, as used in banking., defaults to None
    :type district: str, optional
    :param id_: ID of the `address` object., defaults to None
    :type id_: str, optional
    :param line_1: Line 1 of the address, such as a building number and street name., defaults to None
    :type line_1: str, optional
    :param line_2: Line 2 of the address, such as a suite or apartment number, or the name of a named building., defaults to None
    :type line_2: str, optional
    :param line_3: Line 2 of the address, such as a suite or apartment number, or the name of a named building., defaults to None
    :type line_3: str, optional
    :param metadata: A JSON object defined by the client., defaults to None
    :type metadata: any, optional
    :param name: The name of a contact person or an 'in care of' person at this address. For a **personal** wallet contact type, alphabetic characters and spaces.A JSON object defined by the client., defaults to None
    :type name: str, optional
    :param phone_number: Phone number associated with this specific address in E.164 format. Must be unique., defaults to None
    :type phone_number: str, optional
    :param state: State or province portion of the address., defaults to None
    :type state: str, optional
    :param zip: Postal code portion of the address., defaults to None
    :type zip: str, optional
    """

    def __init__(
        self,
        canton: str = None,
        city: str = None,
        country: str = None,
        created_at: float = None,
        district: str = None,
        id_: str = None,
        line_1: str = None,
        line_2: str = None,
        line_3: str = None,
        metadata: any = None,
        name: str = None,
        phone_number: str = None,
        state: str = None,
        zip: str = None,
    ):
        """AddressResponse

        :param canton: Name of the canton administrative subdivision, as used in banking., defaults to None
        :type canton: str, optional
        :param city: City portion of the address., defaults to None
        :type city: str, optional
        :param country: The two-letter ISO 3166-1 ALPHA-2 code for the country., defaults to None
        :type country: str, optional
        :param created_at: Time of creation of the object, in Unix time., defaults to None
        :type created_at: float, optional
        :param district: Name of the district administrative subdivision, as used in banking., defaults to None
        :type district: str, optional
        :param id_: ID of the `address` object., defaults to None
        :type id_: str, optional
        :param line_1: Line 1 of the address, such as a building number and street name., defaults to None
        :type line_1: str, optional
        :param line_2: Line 2 of the address, such as a suite or apartment number, or the name of a named building., defaults to None
        :type line_2: str, optional
        :param line_3: Line 2 of the address, such as a suite or apartment number, or the name of a named building., defaults to None
        :type line_3: str, optional
        :param metadata: A JSON object defined by the client., defaults to None
        :type metadata: any, optional
        :param name: The name of a contact person or an 'in care of' person at this address. For a **personal** wallet contact type, alphabetic characters and spaces.A JSON object defined by the client., defaults to None
        :type name: str, optional
        :param phone_number: Phone number associated with this specific address in E.164 format. Must be unique., defaults to None
        :type phone_number: str, optional
        :param state: State or province portion of the address., defaults to None
        :type state: str, optional
        :param zip: Postal code portion of the address., defaults to None
        :type zip: str, optional
        """
        self.canton = self._define_str("canton", canton, nullable=True)
        self.city = self._define_str("city", city, nullable=True)
        self.country = self._define_str("country", country, nullable=True)
        self.created_at = self._define_number("created_at", created_at, nullable=True)
        self.district = self._define_str("district", district, nullable=True)
        self.id_ = self._define_str("id_", id_, nullable=True)
        self.line_1 = self._define_str("line_1", line_1, nullable=True)
        self.line_2 = self._define_str("line_2", line_2, nullable=True)
        self.line_3 = self._define_str("line_3", line_3, nullable=True)
        self.metadata = metadata
        self.name = self._define_str("name", name, nullable=True)
        self.phone_number = self._define_str(
            "phone_number", phone_number, nullable=True
        )
        self.state = self._define_str("state", state, nullable=True)
        self.zip = self._define_str("zip", zip, nullable=True)
