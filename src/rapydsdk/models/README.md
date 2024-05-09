# Rapydsdk Models

A list of all models.

- [Status](#status)
- [EWalletsStatus](#ewalletsstatus)
- [FundsTransfer200Response](#fundstransfer200response)
- [SetFundsTransferResponse200Response](#setfundstransferresponse200response)
- [CreateAddress200Response](#createaddress200response)
- [RetrieveAddress200Response](#retrieveaddress200response)
- [UpdateAddress200Response](#updateaddress200response)
- [ListCoupon200Response](#listcoupon200response)
- [CreateCoupon200Response](#createcoupon200response)
- [RetrieveCoupon200Response](#retrievecoupon200response)
- [UpdateCoupon200Response](#updatecoupon200response)
- [DeleteCoupon200Response](#deletecoupon200response)
- [GetHostedPagePayment200Response](#gethostedpagepayment200response)
- [GenerateHostedPagePayment200Response](#generatehostedpagepayment200response)
- [ListCustomer200Response](#listcustomer200response)
- [CreateCustomer200Response](#createcustomer200response)
- [RetrieveCustomer200Response](#retrievecustomer200response)
- [UpdateCustomer200Response](#updatecustomer200response)
- [DeleteCustomer200Response](#deletecustomer200response)
- [DeleteCustomerDiscount200Response](#deletecustomerdiscount200response)
- [GetCustomerPaymentMethods200Response](#getcustomerpaymentmethods200response)
- [CreateCustomerPaymentMethod200Response](#createcustomerpaymentmethod200response)
- [GetCustomerPaymentMethod200Response](#getcustomerpaymentmethod200response)
- [UpdateCustomerPaymentMethod200Response](#updatecustomerpaymentmethod200response)
- [DeleteCustomerPaymentMethod200Response](#deletecustomerpaymentmethod200response)
- [GetCountries200Response](#getcountries200response)
- [GetCurrencies200Response](#getcurrencies200response)
- [GetDisputesListByOrgId200Response](#getdisputeslistbyorgid200response)
- [GetDispute200Response](#getdispute200response)
- [GetEwalletContacts200Response](#getewalletcontacts200response)
- [CreateEwalletContact200Response](#createewalletcontact200response)
- [GetEwalletContact200Response](#getewalletcontact200response)
- [UpdateEwalletContact200Response](#updateewalletcontact200response)
- [DeleteEwalletContact200Response](#deleteewalletcontact200response)
- [GetEwalletContactComplianceLevels200Response](#getewalletcontactcompliancelevels200response)
- [GenerateCardTokenizationPage200Response](#generatecardtokenizationpage200response)
- [GenerateIdvPage200Response](#generateidvpage200response)
- [GenerateCardIssuingPage200Response](#generatecardissuingpage200response)
- [PerformIdentityVerification200Response](#performidentityverification200response)
- [GetKycIdVerificationSupportedDocTypes200Response](#getkycidverificationsupporteddoctypes200response)
- [ListInvoices200Response](#listinvoices200response)
- [RetrieveInvoice200Response](#retrieveinvoice200response)
- [UpdateInvoice200Response](#updateinvoice200response)
- [DeleteInvoice200Response](#deleteinvoice200response)
- [FinalizeInvoice200Response](#finalizeinvoice200response)
- [PayInvoice200Response](#payinvoice200response)
- [CreateIssuing200Response](#createissuing200response)
- [SimulateCompleteBankAccountIssuingTransaction200Response](#simulatecompletebankaccountissuingtransaction200response)
- [RetrieveIssuingByRapydToken200Response](#retrieveissuingbyrapydtoken200response)
- [UpdateReceivingCurrency200Response](#updatereceivingcurrency200response)
- [CloseIssuing200Response](#closeissuing200response)
- [RetrieveIssuingTransaction200Response](#retrieveissuingtransaction200response)
- [GetCardIssuingList200Response](#getcardissuinglist200response)
- [IssueCard200Response](#issuecard200response)
- [GetCardIssuingDetails200Response](#getcardissuingdetails200response)
- [ActivateCard200Response](#activatecard200response)
- [ModifyCard200Response](#modifycard200response)
- [UpdateCardStatus200Response](#updatecardstatus200response)
- [GetCardIssuingTransactions200Response](#getcardissuingtransactions200response)
- [GetCardIssuingTransaction200Response](#getcardissuingtransaction200response)
- [ListOrder200Response](#listorder200response)
- [CreateOrder200Response](#createorder200response)
- [RetrieveOrder200Response](#retrieveorder200response)
- [UpdateOrder200Response](#updateorder200response)
- [ReturnsOrder200Response](#returnsorder200response)
- [PayOrder200Response](#payorder200response)
- [ListOrderReturn200Response](#listorderreturn200response)
- [RetrieveOrderReturn200Response](#retrieveorderreturn200response)
- [GetPaymentMethodsTypesByCountry200Response](#getpaymentmethodstypesbycountry200response)
- [GetPaymentMethodTypeRequiredFields200Response](#getpaymentmethodtyperequiredfields200response)
- [ListPayments200Response](#listpayments200response)
- [CreatePayment200Response](#createpayment200response)
- [RetrievePayment200Response](#retrievepayment200response)
- [UpdatePayment200Response](#updatepayment200response)
- [CancelPayment200Response](#cancelpayment200response)
- [GetSubscriptionList200Response](#getsubscriptionlist200response)
- [CreateSubscription200Response](#createsubscription200response)
- [GetSubscription200Response](#getsubscription200response)
- [UpdateSubscription200Response](#updatesubscription200response)
- [CancelSubscription200Response](#cancelsubscription200response)
- [DeleteSubscriptionDiscount200Response](#deletesubscriptiondiscount200response)
- [GetPayoutMethodTypesDetails200Response](#getpayoutmethodtypesdetails200response)
- [ListPayouts200Response](#listpayouts200response)
- [CreatePayout200Response](#createpayout200response)
- [CreateBeneficiary200Response](#createbeneficiary200response)
- [ValidateBeneficiary200Response](#validatebeneficiary200response)
- [GetBeneficiary200Response](#getbeneficiary200response)
- [DeleteBeneficiary200Response](#deletebeneficiary200response)
- [SimulateCompletePayout200Response](#simulatecompletepayout200response)
- [ConfirmPayout200Response](#confirmpayout200response)
- [CreateSender200Response](#createsender200response)
- [GetPayer200Response](#getpayer200response)
- [DeletePayer200Response](#deletepayer200response)
- [GetPayoutMethodTypes200Response](#getpayoutmethodtypes200response)
- [GetPayout200Response](#getpayout200response)
- [UpdatePayout200Response](#updatepayout200response)
- [CancelPayout200Response](#cancelpayout200response)
- [ListPlans200Response](#listplans200response)
- [CreatePlan200Response](#createplan200response)
- [RetrievePlan200Response](#retrieveplan200response)
- [UpdatePlan200Response](#updateplan200response)
- [DeletePlan200Response](#deleteplan200response)
- [GetProductsList200Response](#getproductslist200response)
- [CreateProduct200Response](#createproduct200response)
- [GetProduct200Response](#getproduct200response)
- [UpdateProduct200Response](#updateproduct200response)
- [DeleteProduct200Response](#deleteproduct200response)
- [GetDailyRate200Response](#getdailyrate200response)
- [AllRefunds200Response](#allrefunds200response)
- [RequestTotalCreateRefund200Response](#requesttotalcreaterefund200response)
- [SimulateCompleteRefund200Response](#simulatecompleterefund200response)
- [RefundGroupPayment200Response](#refundgrouppayment200response)
- [RefundByToken200Response](#refundbytoken200response)
- [UpdateRefund200Response](#updaterefund200response)
- [ListSubscriptionItem200Response](#listsubscriptionitem200response)
- [CreateSubscriptionItem200Response](#createsubscriptionitem200response)
- [RetrieveSubscriptionItem200Response](#retrievesubscriptionitem200response)
- [UpdateSubscriptionItem200Response](#updatesubscriptionitem200response)
- [DeleteSubscriptionItem200Response](#deletesubscriptionitem200response)
- [UsageRecordSummaries200Response](#usagerecordsummaries200response)
- [CreateSubscriptionItemUsageRecord200Response](#createsubscriptionitemusagerecord200response)
- [GetSubscriptionDiscountById200Response](#getsubscriptiondiscountbyid200response)
- [RetrieveSku200Response](#retrievesku200response)
- [UpdateSku200Response](#updatesku200response)
- [DeleteSku200Response](#deletesku200response)
- [ListSku200Response](#listsku200response)
- [CreateSku200Response](#createsku200response)
- [GetUsers200Response](#getusers200response)
- [CreateUser200Response](#createuser200response)
- [GetUser200Response](#getuser200response)
- [UpdatedUser200Response](#updateduser200response)
- [DeleteUser200Response](#deleteuser200response)
- [UpdateEwalletStatus200Response](#updateewalletstatus200response)
- [SetAccountLimit200Response](#setaccountlimit200response)
- [RemoveAccountLimit200Response](#removeaccountlimit200response)
- [GetApplicationTypesByCountry200Response](#getapplicationtypesbycountry200response)
- [GetApplicationStatus200Response](#getapplicationstatus200response)
- [GetUserAccounts200Response](#getuseraccounts200response)
- [GetUserTransactions200Response](#getusertransactions200response)
- [GetUserTransactionDetails200Response](#getusertransactiondetails200response)
- [CreateHostedApplicationToken200Response](#createhostedapplicationtoken200response)
- [GetHostedApplicationByToken200Response](#gethostedapplicationbytoken200response)
- [GetWebhooks200Response](#getwebhooks200response)
- [GetWebhookByToken200Response](#getwebhookbytoken200response)
- [ResendWebhookByToken200Response](#resendwebhookbytoken200response)
- [FundsTransferRequest](#fundstransferrequest)
- [SetFundsTransferResponseRequest](#setfundstransferresponserequest)
- [CreateAddressRequest](#createaddressrequest)
- [CreateCouponRequest](#createcouponrequest)
- [GenerateHostedPagePaymentRequest](#generatehostedpagepaymentrequest)
- [CreateCustomerRequest](#createcustomerrequest)
- [CreateCustomerPaymentMethodRequest](#createcustomerpaymentmethodrequest)
- [CreateEwalletContactRequest](#createewalletcontactrequest)
- [GenerateCardTokenizationPageRequest](#generatecardtokenizationpagerequest)
- [GenerateIdvPageRequest](#generateidvpagerequest)
- [GenerateCardIssuingPageRequest](#generatecardissuingpagerequest)
- [PerformIdentityVerificationRequest](#performidentityverificationrequest)
- [UpdateInvoiceRequest](#updateinvoicerequest)
- [PayInvoiceRequest](#payinvoicerequest)
- [CreateIssuingRequest](#createissuingrequest)
- [SimulateCompleteBankAccountIssuingTransactionRequest](#simulatecompletebankaccountissuingtransactionrequest)
- [UpdateReceivingCurrencyRequest](#updatereceivingcurrencyrequest)
- [IssueCardRequest](#issuecardrequest)
- [ActivateCardRequest](#activatecardrequest)
- [ModifyCardRequest](#modifycardrequest)
- [UpdateCardStatusRequest](#updatecardstatusrequest)
- [CreateOrderRequest](#createorderrequest)
- [UpdateOrderRequest](#updateorderrequest)
- [ReturnsOrderRequest](#returnsorderrequest)
- [PayOrderRequest](#payorderrequest)
- [CreatePaymentRequest](#createpaymentrequest)
- [UpdatePaymentRequest](#updatepaymentrequest)
- [CreateSubscriptionRequest](#createsubscriptionrequest)
- [UpdateSubscriptionRequest](#updatesubscriptionrequest)
- [CreatePayoutRequest](#createpayoutrequest)
- [CreateBeneficiaryRequest](#createbeneficiaryrequest)
- [ValidateBeneficiaryRequest](#validatebeneficiaryrequest)
- [CreateSenderRequest](#createsenderrequest)
- [UpdatePayoutRequest](#updatepayoutrequest)
- [CreatePlanRequest](#createplanrequest)
- [UpdatePlanRequest](#updateplanrequest)
- [CreateProductRequest](#createproductrequest)
- [UpdateProductRequest](#updateproductrequest)
- [RequestTotalCreateRefundRequest](#requesttotalcreaterefundrequest)
- [SimulateCompleteRefundRequest](#simulatecompleterefundrequest)
- [RefundGroupPaymentRequest](#refundgrouppaymentrequest)
- [UpdateRefundRequest](#updaterefundrequest)
- [CreateSubscriptionItemRequest](#createsubscriptionitemrequest)
- [UpdateSubscriptionItemRequest](#updatesubscriptionitemrequest)
- [CreateSubscriptionItemUsageRecordRequest](#createsubscriptionitemusagerecordrequest)
- [UpdateSkuRequest](#updateskurequest)
- [CreateSkuRequest](#createskurequest)
- [CreateUserRequest](#createuserrequest)
- [UpdatedUserRequest](#updateduserrequest)
- [SetAccountLimitRequest](#setaccountlimitrequest)
- [RemoveAccountLimitRequest](#removeaccountlimitrequest)
- [CreateHostedApplicationTokenRequest](#createhostedapplicationtokenrequest)
- [Transfer](#transfer)
- [AddressRequest](#addressrequest)
- [Address](#address)
- [Coupon](#coupon)
- [CheckoutPageResponse](#checkoutpageresponse)
- [MerchantCustomerSupport](#merchantcustomersupport)
- [HostedPageStatus](#hostedpagestatus)
- [Payment](#payment)
- [Dispute](#dispute)
- [NextAction](#nextaction)
- [Outcome](#outcome)
- [PaymentFields](#paymentfields)
- [PaymentAmountRangePerCurrency](#paymentamountrangepercurrency)
- [BinDetails](#bindetails)
- [Category](#category)
- [Condition](#condition)
- [Customer](#customer)
- [CustomerDiscount](#customerdiscount)
- [CustomerPaymentMethod](#customerpaymentmethod)
- [Subscription](#subscription)
- [SubscriptionDiscount](#subscriptiondiscount)
- [SubscriptionItems](#subscriptionitems)
- [SubscriptionItem](#subscriptionitem)
- [Plan](#plan)
- [Product](#product)
- [Sku](#sku)
- [SubscriptionRetryOptions](#subscriptionretryoptions)
- [PaymentFee](#paymentfee)
- [FxFee](#fxfee)
- [TransactionFee](#transactionfee)
- [PaymentStatus](#paymentstatus)
- [CustomerRequest](#customerrequest)
- [CustomerDetailsPmt](#customerdetailspmt)
- [PaymentMethodType](#paymentmethodtype)
- [PaymentMethodTypeField](#paymentmethodtypefield)
- [CountryObject](#countryobject)
- [CurrencyObject](#currencyobject)
- [Contact](#contact)
- [ContactBusiness](#contactbusiness)
- [HostedPageResponse](#hostedpageresponse)
- [PaymentParams](#paymentparams)
- [InvoiceResponse](#invoiceresponse)
- [Payout](#payout)
- [Beneficiary](#beneficiary)
- [EntityType](#entitytype)
- [PayoutFees](#payoutfees)
- [Sender](#sender)
- [PayoutStatus](#payoutstatus)
- [InvoiceItem](#invoiceitem)
- [CardTransaction](#cardtransaction)
- [VirtualAccountTransactionResponse](#virtualaccounttransactionresponse)
- [CardIssuing](#cardissuing)
- [CardIssuingMasked](#cardissuingmasked)
- [OrderResponse](#orderresponse)
- [OrderItemResponse](#orderitemresponse)
- [OrderReturnedItemResponse](#orderreturneditemresponse)
- [OrderReturnedResponse](#orderreturnedresponse)
- [PaymentMethodTypeRequiredFields](#paymentmethodtyperequiredfields)
- [ClientDetailsObject](#clientdetailsobject)
- [Ewallet](#ewallet)
- [Account](#account)
- [Limit](#limit)
- [PayoutMethodTypeDetails](#payoutmethodtypedetails)
- [PayoutRequiredFields](#payoutrequiredfields)
- [PayoutMethodType](#payoutmethodtype)
- [PayoutAmountRangePerCurrency](#payoutamountrangepercurrency)
- [DailyRate](#dailyrate)
- [Refund](#refund)
- [EntityTypeVerify](#entitytypeverify)
- [EwalletTransactionDetails](#ewallettransactiondetails)
- [EwalletTransaction](#ewallettransaction)
- [VerifyHostedAppResponse](#verifyhostedappresponse)
- [Webhook](#webhook)
- [AttemptItem](#attemptitem)

## Status

## EWalletsStatus

## FundsTransfer200Response

## SetFundsTransferResponse200Response

## CreateAddress200Response

## RetrieveAddress200Response

## UpdateAddress200Response

## ListCoupon200Response

## CreateCoupon200Response

## RetrieveCoupon200Response

## UpdateCoupon200Response

## DeleteCoupon200Response

## GetHostedPagePayment200Response

## GenerateHostedPagePayment200Response

## ListCustomer200Response

## CreateCustomer200Response

## RetrieveCustomer200Response

## UpdateCustomer200Response

## DeleteCustomer200Response

## DeleteCustomerDiscount200Response

## GetCustomerPaymentMethods200Response

## CreateCustomerPaymentMethod200Response

## GetCustomerPaymentMethod200Response

## UpdateCustomerPaymentMethod200Response

## DeleteCustomerPaymentMethod200Response

## GetCountries200Response

## GetCurrencies200Response

## GetDisputesListByOrgId200Response

## GetDispute200Response

## GetEwalletContacts200Response

## CreateEwalletContact200Response

## GetEwalletContact200Response

## UpdateEwalletContact200Response

## DeleteEwalletContact200Response

## GetEwalletContactComplianceLevels200Response

## GenerateCardTokenizationPage200Response

## GenerateIdvPage200Response

## GenerateCardIssuingPage200Response

## PerformIdentityVerification200Response

## GetKycIdVerificationSupportedDocTypes200Response

## ListInvoices200Response

## RetrieveInvoice200Response

## UpdateInvoice200Response

## DeleteInvoice200Response

## FinalizeInvoice200Response

## PayInvoice200Response

## CreateIssuing200Response

## SimulateCompleteBankAccountIssuingTransaction200Response

## RetrieveIssuingByRapydToken200Response

## UpdateReceivingCurrency200Response

## CloseIssuing200Response

## RetrieveIssuingTransaction200Response

## GetCardIssuingList200Response

## IssueCard200Response

## GetCardIssuingDetails200Response

## ActivateCard200Response

## ModifyCard200Response

## UpdateCardStatus200Response

## GetCardIssuingTransactions200Response

## GetCardIssuingTransaction200Response

## ListOrder200Response

## CreateOrder200Response

## RetrieveOrder200Response

## UpdateOrder200Response

## ReturnsOrder200Response

## PayOrder200Response

## ListOrderReturn200Response

## RetrieveOrderReturn200Response

## GetPaymentMethodsTypesByCountry200Response

## GetPaymentMethodTypeRequiredFields200Response

## ListPayments200Response

## CreatePayment200Response

## RetrievePayment200Response

## UpdatePayment200Response

## CancelPayment200Response

## GetSubscriptionList200Response

## CreateSubscription200Response

## GetSubscription200Response

## UpdateSubscription200Response

## CancelSubscription200Response

## DeleteSubscriptionDiscount200Response

## GetPayoutMethodTypesDetails200Response

## ListPayouts200Response

## CreatePayout200Response

## CreateBeneficiary200Response

## ValidateBeneficiary200Response

## GetBeneficiary200Response

## DeleteBeneficiary200Response

## SimulateCompletePayout200Response

## ConfirmPayout200Response

## CreateSender200Response

## GetPayer200Response

## DeletePayer200Response

## GetPayoutMethodTypes200Response

## GetPayout200Response

## UpdatePayout200Response

## CancelPayout200Response

## ListPlans200Response

## CreatePlan200Response

## RetrievePlan200Response

## UpdatePlan200Response

## DeletePlan200Response

## GetProductsList200Response

## CreateProduct200Response

## GetProduct200Response

## UpdateProduct200Response

## DeleteProduct200Response

## GetDailyRate200Response

## AllRefunds200Response

## RequestTotalCreateRefund200Response

## SimulateCompleteRefund200Response

## RefundGroupPayment200Response

## RefundByToken200Response

## UpdateRefund200Response

## ListSubscriptionItem200Response

## CreateSubscriptionItem200Response

## RetrieveSubscriptionItem200Response

## UpdateSubscriptionItem200Response

## DeleteSubscriptionItem200Response

## UsageRecordSummaries200Response

## CreateSubscriptionItemUsageRecord200Response

## GetSubscriptionDiscountById200Response

## RetrieveSku200Response

## UpdateSku200Response

## DeleteSku200Response

## ListSku200Response

## CreateSku200Response

## GetUsers200Response

## CreateUser200Response

## GetUser200Response

## UpdatedUser200Response

## DeleteUser200Response

## UpdateEwalletStatus200Response

## SetAccountLimit200Response

## RemoveAccountLimit200Response

## GetApplicationTypesByCountry200Response

## GetApplicationStatus200Response

## GetUserAccounts200Response

## GetUserTransactions200Response

## GetUserTransactionDetails200Response

## CreateHostedApplicationToken200Response

## GetHostedApplicationByToken200Response

## GetWebhooks200Response

## GetWebhookByToken200Response

## ResendWebhookByToken200Response

## FundsTransferRequest

## SetFundsTransferResponseRequest

## CreateAddressRequest

## CreateCouponRequest

## GenerateHostedPagePaymentRequest

## CreateCustomerRequest

## CreateCustomerPaymentMethodRequest

## CreateEwalletContactRequest

## GenerateCardTokenizationPageRequest

## GenerateIdvPageRequest

## GenerateCardIssuingPageRequest

## PerformIdentityVerificationRequest

## UpdateInvoiceRequest

## PayInvoiceRequest

## CreateIssuingRequest

## SimulateCompleteBankAccountIssuingTransactionRequest

## UpdateReceivingCurrencyRequest

## IssueCardRequest

## ActivateCardRequest

## ModifyCardRequest

## UpdateCardStatusRequest

## CreateOrderRequest

## UpdateOrderRequest

## ReturnsOrderRequest

## PayOrderRequest

## CreatePaymentRequest

## UpdatePaymentRequest

## CreateSubscriptionRequest

## UpdateSubscriptionRequest

## CreatePayoutRequest

## CreateBeneficiaryRequest

## ValidateBeneficiaryRequest

## CreateSenderRequest

## UpdatePayoutRequest

## CreatePlanRequest

## UpdatePlanRequest

## CreateProductRequest

## UpdateProductRequest

## RequestTotalCreateRefundRequest

## SimulateCompleteRefundRequest

## RefundGroupPaymentRequest

## UpdateRefundRequest

## CreateSubscriptionItemRequest

## UpdateSubscriptionItemRequest

## CreateSubscriptionItemUsageRecordRequest

## UpdateSkuRequest

## CreateSkuRequest

## CreateUserRequest

## UpdatedUserRequest

## SetAccountLimitRequest

## RemoveAccountLimitRequest

## CreateHostedApplicationTokenRequest

## Transfer

## AddressRequest

## Address

## Coupon

## CheckoutPageResponse

## MerchantCustomerSupport

## HostedPageStatus

## Payment

## Dispute

## NextAction

## Outcome

## PaymentFields

## PaymentAmountRangePerCurrency

## BinDetails

## Category

## Condition

## Customer

## CustomerDiscount

## CustomerPaymentMethod

## Subscription

## SubscriptionDiscount

## SubscriptionItems

## SubscriptionItem

## Plan

## Product

## Sku

## SubscriptionRetryOptions

## PaymentFee

## FxFee

## TransactionFee

## PaymentStatus

## CustomerRequest

## CustomerDetailsPmt

## PaymentMethodType

## PaymentMethodTypeField

## CountryObject

## CurrencyObject

## Contact

## ContactBusiness

## HostedPageResponse

## PaymentParams

## InvoiceResponse

## Payout

## Beneficiary

## EntityType

## PayoutFees

## Sender

## PayoutStatus

## InvoiceItem

## CardTransaction

## VirtualAccountTransactionResponse

## CardIssuing

## CardIssuingMasked

## OrderResponse

## OrderItemResponse

## OrderReturnedItemResponse

## OrderReturnedResponse

## PaymentMethodTypeRequiredFields

## ClientDetailsObject

## Ewallet

## Account

## Limit

## PayoutMethodTypeDetails

## PayoutRequiredFields

## PayoutMethodType

## PayoutAmountRangePerCurrency

## DailyRate

## Refund

## EntityTypeVerify

## EwalletTransactionDetails

## EwalletTransaction

## VerifyHostedAppResponse

## Webhook

## AttemptItem
