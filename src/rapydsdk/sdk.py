"""
Creates a Rapydsdk class.
Generates the main SDK with all available queries as attributes.

Class:
    Rapydsdk
"""

from .net.environment import Environment

from .services.collect import Collect
from .services.disburse import Disburse
from .services.e_wallets import EWallets
from .services.general_resources import GeneralResources
from .services.hosted import Hosted
from .services.issuing import Issuing
from .services.verify import Verify


class Rapydsdk:
    """
    A class representing the full Rapydsdk SDK

    Attributes
    ----------
    collect : Collect
    disburse : Disburse
    e_wallets : EWallets
    general_resources : GeneralResources
    hosted : Hosted
    issuing : Issuing
    verify : Verify

    Methods
    -------
    set_base_url(url: str)
        Sets the end URL
    """

    def __init__(self, environment=Environment.DEFAULT) -> None:
        """
        Initializes the Rapydsdk SDK class.
        Parameters
        ----------
        environment: str
            The environment that the SDK is accessing
        """
        self.collect = Collect()
        self.disburse = Disburse()
        self.e_wallets = EWallets()
        self.general_resources = GeneralResources()
        self.hosted = Hosted()
        self.issuing = Issuing()
        self.verify = Verify()

        self.set_base_url(environment.value)

    def set_base_url(self, url: str) -> None:
        """
        Sets the end URL

        Parameters
        ----------
            url:
                The end URL
        """
        self.collect.set_base_url(url)
        self.disburse.set_base_url(url)
        self.e_wallets.set_base_url(url)
        self.general_resources.set_base_url(url)
        self.hosted.set_base_url(url)
        self.issuing.set_base_url(url)
        self.verify.set_base_url(url)


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
