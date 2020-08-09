# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import logging
from decimal import Decimal

from pymhelper.orders import Order

logging.basicConfig(level=logging.DEBUG)


def test_order_creation():
    order = Order(**{
        "symbol": "LTCBTC",
        "orderId": 1,
        "orderListId": 1,
        "clientOrderId": "myOrder1",
        "price": "0.1",
        "origQty": "1.0",
        "executedQty": "0.0",
        "cummulativeQuoteQty": 0,
        "status": "NEW",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY",
        "stopPrice": "0.0",
        "icebergQty": "0.0",
        "time": 1499827319559,
        "updateTime": 1499827319559,
        "isWorking": False,
        "origQuoteOrderQty": "1.0"
    })

    assert order.symbol == "LTCBTC"
    assert order.price == Decimal("0.1")
    assert order.side == "BUY"

    assert order.is_stale() is True
    assert order.is_stale(current_time_sec=1499827319) is False
    assert order.is_stale(current_time_sec=1499827319 + 31 * 60) is True

    order.status = 'FILLED'
    assert order.is_stale(current_time_sec=1499827319) is False
