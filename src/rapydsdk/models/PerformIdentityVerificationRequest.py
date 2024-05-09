from .utils.JsonMap import JsonMap
from .base import BaseModel


@JsonMap({})
class PerformIdentityVerificationRequest(BaseModel):
    def __init__(
        self,
        country: str,
        document_type: str,
        ewallet: str,
        face_image: str,
        front_side_image: str,
        reference_id: str,
        back_side_image: str = None,
        back_side_image_mime_type: str = None,
        contact: str = None,
        face_image_mime_type: str = None,
        front_side_image_mime_type: str = None,
        request_type: str = None,
        send_callback: str = None,
    ):
        self.back_side_image = back_side_image
        self.back_side_image_mime_type = back_side_image_mime_type
        self.contact = contact
        self.country = self._pattern_matching(
            country,
            "^(A(D|E|F|G|I|L|M|N|O|R|S|T|Q|U|W|X|Z)|B(A|B|D|E|F|G|H|I|J|L|M|N|O|R|S|T|V|W|Y|Z)|C(A|C|D|F|G|H|I|K|L|M|N|O|R|U|V|X|Y|Z)|D(E|J|K|M|O|Z)|E(C|E|G|H|R|S|T)|F(I|J|K|M|O|R)|G(A|B|D|E|F|G|H|I|L|M|N|P|Q|R|S|T|U|W|Y)|H(K|M|N|R|T|U)|I(D|E|Q|L|M|N|O|R|S|T)|J(E|M|O|P)|K(E|G|H|I|M|N|P|R|W|Y|Z)|L(A|B|C|I|K|R|S|T|U|V|Y)|M(A|C|D|E|F|G|H|K|L|M|N|O|Q|P|R|S|T|U|V|W|X|Y|Z)|N(A|C|E|F|G|I|L|O|P|R|U|Z)|OM|P(A|E|F|G|H|K|L|M|N|R|S|T|W|Y)|QA|R(E|O|S|U|W)|S(A|B|C|D|E|G|H|I|J|K|L|M|N|O|R|T|V|Y|Z)|T(C|D|F|G|H|J|K|L|M|N|O|R|T|V|W|Z)|U(A|G|M|S|Y|Z)|V(A|C|E|G|I|N|U)|W(F|S)|Y(E|T)|Z(A|M|W))$",
            "country",
        )
        self.document_type = document_type
        self.ewallet = ewallet
        self.face_image = face_image
        self.face_image_mime_type = face_image_mime_type
        self.front_side_image = front_side_image
        self.front_side_image_mime_type = front_side_image_mime_type
        self.reference_id = reference_id
        self.request_type = request_type
        self.send_callback = send_callback
