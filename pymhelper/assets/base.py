# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import logging
from decimal import Decimal

from .datamodels import Asset

logger = logging.getLogger(__name__)


class AssetBaseClass:
    """Basic implementation of Bot class with Assets.
    """

    def __init__(self, base_asset_name: str, quote_asset_name: str,
                 base_asset_min: Decimal, quote_asset_min: Decimal) -> None:
        """

        :param base_asset_name:
        :param quote_asset_name:
        :param base_asset_min:
        :param quote_asset_min:
        """
        self.symbol = base_asset_name + quote_asset_name
        self.base_asset_name = base_asset_name
        self.quote_asset_name = quote_asset_name

        # Allocating assets:
        setattr(self, self.base_asset_name,  # e.g. BTC
                Asset(name=self.base_asset_name,
                      free=Decimal('0'),
                      locked=Decimal('0'),
                      minimum=base_asset_min))  # e.g. BTC = 0.001
        setattr(self, self.quote_asset_name,  # e.g. BUSD
                Asset(name=self.quote_asset_name,
                      free=Decimal('0'),
                      locked=Decimal('0'),
                      minimum=quote_asset_min))  # e.g. BUSD = $10

        logger.debug('Base asset %s', self.base_asset)
        logger.debug('Quote asset %s', self.quote_asset)

    @property
    def base_asset(self) -> Asset:
        return getattr(self, self.base_asset_name)

    @property
    def quote_asset(self) -> Asset:
        return getattr(self, self.quote_asset_name)

    def sync_balances(self) -> None:
        raise NotImplementedError()
