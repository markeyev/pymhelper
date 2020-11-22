# pylint: disable=too-many-instance-attributes,invalid-name

"""Binance kline represented in dataclasses format.
"""
import datetime
from dataclasses import dataclass
from decimal import Decimal

from pymhelper.dataclasseshelper import AutoConvertingField


@dataclass
class KLine(AutoConvertingField):
    """
    Candlestick / Kline data.

    Full representation contains:

    1499040000000,      // Open time
    "0.01634790",       // Open
    "0.80000000",       // High
    "0.01575800",       // Low
    "0.01577100",       // Close
    "148976.11427815",  // Volume
    1499644799999,      // Close time
    "2434.19055334",    // Quote asset volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base asset volume
    "28.46694368",      // Taker buy quote asset volume
    """
    dt: datetime.datetime  # Open time
    open: Decimal  # Open
    high: Decimal  # High
    low: Decimal  # Low
    close: Decimal  # Close
    vol: Decimal  # Volume
    # Close time
    qty_vol: Decimal  # Quote asset volume
    count: int  # Number of trades
    # Taker buy base asset volume
    # Taker buy quote asset volume
