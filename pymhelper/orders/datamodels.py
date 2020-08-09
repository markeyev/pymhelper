# pylint: disable=too-many-instance-attributes,invalid-name

"""Binance order represented in dataclasses format.
"""
import time
from dataclasses import dataclass
from decimal import Decimal

from pymhelper.dataclasseshelper import AutoConvertingField


@dataclass
class OrderACK(AutoConvertingField):
    """Order ACK message.
    """
    symbol: str
    orderId: int
    orderListId: int
    clientOrderId: str
    transactTime: int


@dataclass
class Order(AutoConvertingField):
    """Order representation.
    """
    symbol: str
    orderId: int
    orderListId: int
    clientOrderId: str
    price: Decimal
    origQty: Decimal
    executedQty: Decimal
    cummulativeQuoteQty: Decimal
    status: str
    timeInForce: str
    type: str
    side: str
    stopPrice: Decimal
    icebergQty: Decimal
    time: int
    updateTime: int
    isWorking: bool
    origQuoteOrderQty: Decimal

    @property
    def time_sec(self) -> int:
        """Returns order time in seconds.

        :return: bool
        """
        return self.time // 1000

    def is_buy(self) -> bool:
        """Checks if order side is buy.

        :return: bool
        """
        return bool(self.side == 'BUY')

    def is_sell(self) -> bool:
        """Checks if order side is sell.

        :return: bool
        """
        return bool(self.side == 'SELL')

    def is_stale(self, current_time_sec: int = None,
                 timeout_sec: int = None) -> bool:
        """Checks if order is still open and timeout exceeds.

        :param current_time_sec: if None, then time.time()
        :param timeout_sec: if None, 30 minutes for BUY and 24 hours for SELL
        :return: bool
        """
        if self.status not in ('NEW', 'PARTIALLY_FILLED'):
            return False
        if timeout_sec is None:
            if self.is_buy():
                timeout_sec = 30 * 60  # 30 minutes
            else:
                timeout_sec = 24 * 60 * 60  # 24 hours
        if current_time_sec is None:
            current_time_sec = time.time()
        return bool(current_time_sec - self.time_sec > timeout_sec)
