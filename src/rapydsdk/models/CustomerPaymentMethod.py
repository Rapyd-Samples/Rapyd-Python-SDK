from __future__ import annotations
from typing import Union
from .utils.JsonMap import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .Category import Category
from .NextAction import NextAction
from .BinDetails import BinDetails


@JsonMap({"type_": "type"})
class CustomerPaymentMethod1(BaseModel):
    def __init__(
        self,
        bic_swift: str = None,
        account_last4: str = None,
        id: str = None,
        type_: str = None,
        category: Category = None,
        metadata: dict = None,
        image: str = None,
        webhook_url: str = None,
        supporting_documentation: str = None,
        next_action: NextAction = None,
    ):
        self.bic_swift = bic_swift
        self.account_last4 = account_last4
        self.id = id
        self.type_ = type_
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
        )
        self.metadata = metadata
        self.image = image
        self.webhook_url = webhook_url
        self.supporting_documentation = supporting_documentation
        self.next_action = (
            self._enum_matching(next_action, NextAction.list(), "next_action")
            if next_action
            else None
        )


@JsonMap({"type_": "type"})
class CustomerPaymentMethod2(BaseModel):
    def __init__(
        self,
        last_name: str = None,
        first_name: str = None,
        id: str = None,
        type_: str = None,
        category: Category = None,
        metadata: dict = None,
        image: str = None,
        webhook_url: str = None,
        supporting_documentation: str = None,
        next_action: NextAction = None,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.id = id
        self.type_ = type_
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
        )
        self.metadata = metadata
        self.image = image
        self.webhook_url = webhook_url
        self.supporting_documentation = supporting_documentation
        self.next_action = (
            self._enum_matching(next_action, NextAction.list(), "next_action")
            if next_action
            else None
        )


@JsonMap({"type_": "type"})
class CustomerPaymentMethod3(BaseModel):
    def __init__(
        self,
        last4: str = None,
        acs_check: str = None,
        cvv_check: str = None,
        bin_details: BinDetails = None,
        expiration_year: str = None,
        expiration_month: str = None,
        fingerprint_token: str = None,
        id: str = None,
        type_: str = None,
        category: Category = None,
        metadata: dict = None,
        image: str = None,
        webhook_url: str = None,
        supporting_documentation: str = None,
        next_action: NextAction = None,
    ):
        self.last4 = last4
        self.acs_check = acs_check
        self.cvv_check = cvv_check
        self.bin_details = self._define_object(bin_details, BinDetails)
        self.expiration_year = expiration_year
        self.expiration_month = expiration_month
        self.fingerprint_token = fingerprint_token
        self.id = id
        self.type_ = type_
        self.category = (
            self._enum_matching(category, Category.list(), "category")
            if category
            else None
        )
        self.metadata = metadata
        self.image = image
        self.webhook_url = webhook_url
        self.supporting_documentation = supporting_documentation
        self.next_action = (
            self._enum_matching(next_action, NextAction.list(), "next_action")
            if next_action
            else None
        )


class CustomerPaymentMethodGuard(OneOfBaseModel):
    class_list = {
        "CustomerPaymentMethod1": CustomerPaymentMethod1,
        "CustomerPaymentMethod2": CustomerPaymentMethod2,
        "CustomerPaymentMethod3": CustomerPaymentMethod3,
    }


CustomerPaymentMethod = Union[
    CustomerPaymentMethod1, CustomerPaymentMethod2, CustomerPaymentMethod3
]
