from enum import Enum


class EntityTypeVerify(Enum):
    PARTNERSHIP = "Partnership"
    SOLE_PROPRIETOR = "Sole Proprietor"
    PRIVATE_LIMITED_COMPANY = "Private Limited Company"
    CHARITY_OR_NPO = "Charity or NPO"
    INDIVIDUAL = "Individual"

    def list():
        return list(map(lambda x: x.value, EntityTypeVerify._member_map_.values()))
