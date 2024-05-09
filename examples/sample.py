from os import getenv
from pprint import pprint
from rapydsdk import Rapydsdk

sdk = Rapydsdk()

results = sdk.collect.list_coupon()

pprint(vars(results))
