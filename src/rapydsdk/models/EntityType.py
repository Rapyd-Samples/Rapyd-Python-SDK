from enum import Enum


class EntityType(Enum):
    COMPANY = "company"
    INDIVIDUAL = "individual"

    def list():
        return list(map(lambda x: x.value, EntityType._member_map_.values()))
