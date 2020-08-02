# pylint: disable=too-many-instance-attributes,invalid-name

"""Binance order represented in dataclasses format.
"""

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
