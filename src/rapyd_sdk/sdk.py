from typing import Union
from .services.e_wallets import EWalletsService
from .services.virtual_accounts import VirtualAccountsService
from .services.disburse import DisburseService
from .services.fx import FxService
from .services.issuing import IssuingService
from .services.checkout_page import CheckoutPageService
from .services.coupon import CouponService
from .services.customer import CustomerService
from .services.customer_payment_method import CustomerPaymentMethodService
from .services.digital_wallet import DigitalWalletService
from .services.dispute import DisputeService
from .services.escrow import EscrowService
from .services.group_payment import GroupPaymentService
from .services.subscription_invoice import SubscriptionInvoiceService
from .services.order import OrderService
from .services.order_return import OrderReturnService
from .services.payment_method_type import PaymentMethodTypeService
from .services.payment_link import PaymentLinkService
from .services.payment_card_token import PaymentCardTokenService
from .services.payment import PaymentService
from .services.payment_address import PaymentAddressService
from .services.subscription import SubscriptionService
from .services.subscription_plan import SubscriptionPlanService
from .services.subscription_product import SubscriptionProductService
from .services.refund import RefundService
from .services.subscription_subscription_item import SubscriptionSubscriptionItemService
from .services.sku import SkuService
from .services.verify import VerifyService
from .net.environment import Environment


class RapydSdk:
    def __init__(
        self,
        base_url: Union[Environment, str] = Environment.DEFAULT,
        timeout: int = 60000,
    ):
        """
        Initializes RapydSdk the SDK class.
        """

        self._base_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )
        self.e_wallets = EWalletsService(base_url=self._base_url)
        self.virtual_accounts = VirtualAccountsService(base_url=self._base_url)
        self.disburse = DisburseService(base_url=self._base_url)
        self.fx = FxService(base_url=self._base_url)
        self.issuing = IssuingService(base_url=self._base_url)
        self.checkout_page = CheckoutPageService(base_url=self._base_url)
        self.coupon = CouponService(base_url=self._base_url)
        self.customer = CustomerService(base_url=self._base_url)
        self.customer_payment_method = CustomerPaymentMethodService(
            base_url=self._base_url
        )
        self.digital_wallet = DigitalWalletService(base_url=self._base_url)
        self.dispute = DisputeService(base_url=self._base_url)
        self.escrow = EscrowService(base_url=self._base_url)
        self.group_payment = GroupPaymentService(base_url=self._base_url)
        self.subscription_invoice = SubscriptionInvoiceService(base_url=self._base_url)
        self.order = OrderService(base_url=self._base_url)
        self.order_return = OrderReturnService(base_url=self._base_url)
        self.payment_method_type = PaymentMethodTypeService(base_url=self._base_url)
        self.payment_link = PaymentLinkService(base_url=self._base_url)
        self.payment_card_token = PaymentCardTokenService(base_url=self._base_url)
        self.payment = PaymentService(base_url=self._base_url)
        self.payment_address = PaymentAddressService(base_url=self._base_url)
        self.subscription = SubscriptionService(base_url=self._base_url)
        self.subscription_plan = SubscriptionPlanService(base_url=self._base_url)
        self.subscription_product = SubscriptionProductService(base_url=self._base_url)
        self.refund = RefundService(base_url=self._base_url)
        self.subscription_subscription_item = SubscriptionSubscriptionItemService(
            base_url=self._base_url
        )
        self.sku = SkuService(base_url=self._base_url)
        self.verify = VerifyService(base_url=self._base_url)
        self.set_timeout(timeout)

    def set_base_url(self, base_url: Union[Environment, str]):
        """
        Sets the base URL for the entire SDK.

        :param Union[Environment, str] base_url: The base URL to be set.
        :return: The SDK instance.
        """
        self._base_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )

        self.e_wallets.set_base_url(self._base_url)
        self.virtual_accounts.set_base_url(self._base_url)
        self.disburse.set_base_url(self._base_url)
        self.fx.set_base_url(self._base_url)
        self.issuing.set_base_url(self._base_url)
        self.checkout_page.set_base_url(self._base_url)
        self.coupon.set_base_url(self._base_url)
        self.customer.set_base_url(self._base_url)
        self.customer_payment_method.set_base_url(self._base_url)
        self.digital_wallet.set_base_url(self._base_url)
        self.dispute.set_base_url(self._base_url)
        self.escrow.set_base_url(self._base_url)
        self.group_payment.set_base_url(self._base_url)
        self.subscription_invoice.set_base_url(self._base_url)
        self.order.set_base_url(self._base_url)
        self.order_return.set_base_url(self._base_url)
        self.payment_method_type.set_base_url(self._base_url)
        self.payment_link.set_base_url(self._base_url)
        self.payment_card_token.set_base_url(self._base_url)
        self.payment.set_base_url(self._base_url)
        self.payment_address.set_base_url(self._base_url)
        self.subscription.set_base_url(self._base_url)
        self.subscription_plan.set_base_url(self._base_url)
        self.subscription_product.set_base_url(self._base_url)
        self.refund.set_base_url(self._base_url)
        self.subscription_subscription_item.set_base_url(self._base_url)
        self.sku.set_base_url(self._base_url)
        self.verify.set_base_url(self._base_url)

        return self

    def set_timeout(self, timeout: int):
        """
        Sets the timeout for the entire SDK.

        :param int timeout: The timeout (ms) to be set.
        :return: The SDK instance.
        """
        self.e_wallets.set_timeout(timeout)
        self.virtual_accounts.set_timeout(timeout)
        self.disburse.set_timeout(timeout)
        self.fx.set_timeout(timeout)
        self.issuing.set_timeout(timeout)
        self.checkout_page.set_timeout(timeout)
        self.coupon.set_timeout(timeout)
        self.customer.set_timeout(timeout)
        self.customer_payment_method.set_timeout(timeout)
        self.digital_wallet.set_timeout(timeout)
        self.dispute.set_timeout(timeout)
        self.escrow.set_timeout(timeout)
        self.group_payment.set_timeout(timeout)
        self.subscription_invoice.set_timeout(timeout)
        self.order.set_timeout(timeout)
        self.order_return.set_timeout(timeout)
        self.payment_method_type.set_timeout(timeout)
        self.payment_link.set_timeout(timeout)
        self.payment_card_token.set_timeout(timeout)
        self.payment.set_timeout(timeout)
        self.payment_address.set_timeout(timeout)
        self.subscription.set_timeout(timeout)
        self.subscription_plan.set_timeout(timeout)
        self.subscription_product.set_timeout(timeout)
        self.refund.set_timeout(timeout)
        self.subscription_subscription_item.set_timeout(timeout)
        self.sku.set_timeout(timeout)
        self.verify.set_timeout(timeout)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
