from .services.e_wallets import EWalletsService
from .services.virtual_accounts import VirtualAccountsService
from .services.disburse import DisburseService
from .services.fx import FxService
from .services.checkout_page import CheckoutPageService
from .services.coupon import CouponService
from .services.customer import CustomerService
from .services.customer_payment_method import CustomerPaymentMethodService
from .services.dispute import DisputeService
from .services.subscription_invoice import SubscriptionInvoiceService
from .services.order import OrderService
from .services.payment_method_type import PaymentMethodTypeService
from .services.payment import PaymentService
from .services.subscription import SubscriptionService
from .services.subscription_plan import SubscriptionPlanService
from .services.subscription_product import SubscriptionProductService
from .services.refund import RefundService
from .services.subscription_subscription_item import SubscriptionSubscriptionItemService
from .services.sku import SkuService
from .net.environment import Environment


class RapydSdk:
    def __init__(self, base_url: str = Environment.DEFAULT.value, timeout: int = 60000):
        """
        Initializes RapydSdk the SDK class.
        """

        self.e_wallets = EWalletsService(base_url=base_url)
        self.virtual_accounts = VirtualAccountsService(base_url=base_url)
        self.disburse = DisburseService(base_url=base_url)
        self.fx = FxService(base_url=base_url)
        self.checkout_page = CheckoutPageService(base_url=base_url)
        self.coupon = CouponService(base_url=base_url)
        self.customer = CustomerService(base_url=base_url)
        self.customer_payment_method = CustomerPaymentMethodService(base_url=base_url)
        self.dispute = DisputeService(base_url=base_url)
        self.subscription_invoice = SubscriptionInvoiceService(base_url=base_url)
        self.order = OrderService(base_url=base_url)
        self.payment_method_type = PaymentMethodTypeService(base_url=base_url)
        self.payment = PaymentService(base_url=base_url)
        self.subscription = SubscriptionService(base_url=base_url)
        self.subscription_plan = SubscriptionPlanService(base_url=base_url)
        self.subscription_product = SubscriptionProductService(base_url=base_url)
        self.refund = RefundService(base_url=base_url)
        self.subscription_subscription_item = SubscriptionSubscriptionItemService(
            base_url=base_url
        )
        self.sku = SkuService(base_url=base_url)
        self.set_timeout(timeout)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.e_wallets.set_base_url(base_url)
        self.virtual_accounts.set_base_url(base_url)
        self.disburse.set_base_url(base_url)
        self.fx.set_base_url(base_url)
        self.checkout_page.set_base_url(base_url)
        self.coupon.set_base_url(base_url)
        self.customer.set_base_url(base_url)
        self.customer_payment_method.set_base_url(base_url)
        self.dispute.set_base_url(base_url)
        self.subscription_invoice.set_base_url(base_url)
        self.order.set_base_url(base_url)
        self.payment_method_type.set_base_url(base_url)
        self.payment.set_base_url(base_url)
        self.subscription.set_base_url(base_url)
        self.subscription_plan.set_base_url(base_url)
        self.subscription_product.set_base_url(base_url)
        self.refund.set_base_url(base_url)
        self.subscription_subscription_item.set_base_url(base_url)
        self.sku.set_base_url(base_url)

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
        self.checkout_page.set_timeout(timeout)
        self.coupon.set_timeout(timeout)
        self.customer.set_timeout(timeout)
        self.customer_payment_method.set_timeout(timeout)
        self.dispute.set_timeout(timeout)
        self.subscription_invoice.set_timeout(timeout)
        self.order.set_timeout(timeout)
        self.payment_method_type.set_timeout(timeout)
        self.payment.set_timeout(timeout)
        self.subscription.set_timeout(timeout)
        self.subscription_plan.set_timeout(timeout)
        self.subscription_product.set_timeout(timeout)
        self.refund.set_timeout(timeout)
        self.subscription_subscription_item.set_timeout(timeout)
        self.sku.set_timeout(timeout)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
