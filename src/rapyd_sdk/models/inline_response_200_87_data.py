from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .entity_type_verify import EntityTypeVerify


@JsonMap({})
class InlineResponse200_87Data(BaseModel):
    """InlineResponse200_87Data

    :param application_type: Code for the type of application. String starting with typ_., defaults to None
    :type application_type: str, optional
    :param country: country, defaults to None
    :type country: str, optional
    :param entity_type: entity_type, defaults to None
    :type entity_type: EntityTypeVerify, optional
    """

    def __init__(
        self,
        application_type: str = None,
        country: str = None,
        entity_type: EntityTypeVerify = None,
    ):
        """InlineResponse200_87Data

        :param application_type: Code for the type of application. String starting with typ_., defaults to None
        :type application_type: str, optional
        :param country: country, defaults to None
        :type country: str, optional
        :param entity_type: entity_type, defaults to None
        :type entity_type: EntityTypeVerify, optional
        """
        self.application_type = self._define_str(
            "application_type", application_type, nullable=True
        )
        self.country = self._define_str(
            "country",
            country,
            nullable=True,
            pattern="^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
        )
        self.entity_type = (
            self._enum_matching(entity_type, EntityTypeVerify.list(), "entity_type")
            if entity_type
            else None
        )
