from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"type_": "type"})
class BinDetails(BaseModel):
    """Bank Identification Number (BIN) details. Read-only. Object containing the following fields - * bin_number - BIN number * country - The two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase. * funding - Type of card funding. One of the following [credit, debit, prepaid, unknown] * bank - Name of the issuing bank. Relevant to cards

    :param brand: brand, defaults to None
    :type brand: str, optional
    :param bin_number: bin_number, defaults to None
    :type bin_number: str, optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    :param issuer: issuer, defaults to None
    :type issuer: str, optional
    :param country: country, defaults to None
    :type country: str, optional
    :param level: level, defaults to None
    :type level: str, optional
    """

    def __init__(
        self,
        brand: str = None,
        bin_number: str = None,
        type_: str = None,
        issuer: str = None,
        country: str = None,
        level: str = None,
    ):
        """Bank Identification Number (BIN) details. Read-only. Object containing the following fields - * bin_number - BIN number * country - The two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase. * funding - Type of card funding. One of the following [credit, debit, prepaid, unknown] * bank - Name of the issuing bank. Relevant to cards

        :param brand: brand, defaults to None
        :type brand: str, optional
        :param bin_number: bin_number, defaults to None
        :type bin_number: str, optional
        :param type_: type_, defaults to None
        :type type_: str, optional
        :param issuer: issuer, defaults to None
        :type issuer: str, optional
        :param country: country, defaults to None
        :type country: str, optional
        :param level: level, defaults to None
        :type level: str, optional
        """
        self.brand = self._define_str("brand", brand, nullable=True)
        self.bin_number = self._define_str("bin_number", bin_number, nullable=True)
        self.type_ = self._define_str("type_", type_, nullable=True)
        self.issuer = self._define_str("issuer", issuer, nullable=True)
        self.country = self._define_str(
            "country",
            country,
            nullable=True,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.level = self._define_str("level", level, nullable=True)
