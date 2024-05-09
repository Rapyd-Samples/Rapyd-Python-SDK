from __future__ import annotations
from typing import List
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .AttemptItem import AttemptItem


@JsonMap({"type_": "type"})
class Webhook(BaseModel):
    def __init__(
        self,
        token: str = None,
        type_: str = None,
        data: dict = None,
        attempts: List[AttemptItem] = None,
        status: str = None,
        last_attempt_at: float = None,
        created_at: float = None,
        next_attempt_at: float = None,
    ):
        self.token = token
        self.type_ = type_
        self.data = data
        self.attempts = self._define_list(attempts, AttemptItem)
        self.status = status
        self.last_attempt_at = last_attempt_at
        self.created_at = created_at
        self.next_attempt_at = next_attempt_at
