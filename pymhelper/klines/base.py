# pylint: disable=missing-module-docstring

import datetime
from typing import Dict, List

from .datamodels import KLine


class KLinesHelper:
    """Candlestick / Kline data helper class.
    """

    def __init__(self, init_dict: dict = None):
        """Sets the helper data from initial dictionary.

        :param init_dict: {<open_ts>: <Kline obj>, }
        """
        if init_dict:
            self.klines: Dict[int: KLine] = init_dict
        else:
            self.klines: Dict[int: KLine] = {}

    def range(self):
        """Shows earliest and latest timestamp key in klines data.

        :return:
        """
        return (self.klines[min(self.klines.keys())].dt,
                self.klines[max(self.klines.keys())].dt)

    def idx2kl(self, idx):
        """Gets kline data by the open timestamp.

        :param idx:
        :return:
        """
        kline_idx = list(self.klines.keys())[idx]
        return self.klines[kline_idx]

    def len(self) -> int:
        """Length of Klines in Helper class.

        :return:
        """
        return len(self.klines)

    def items(self) -> tuple:
        """Kline iterator.

        :return:
        """
        for open_ts, kline in self.klines.items():
            yield open_ts, kline

    def filter(self, *,
               start_dt: datetime.datetime,
               stop_dt: datetime.datetime) -> None:
        """Filter out klines between two datetime start_dt and stop_dt.

        :param start_dt:
        :param stop_dt:
        :return:
        """
        self.klines = {open_ts: kline for open_ts, kline in self.items()
                       if stop_dt >= kline.dt >= start_dt}

    async def get_kline(self, *,
                        symbol: str,
                        interval: str = '1m',
                        start_str: str = '1 week ago',
                        end_str: str = '0 minute ago') -> List[dict]:
        """Getting the klines data from provider e.g. Binance API.

        :param symbol:
        :param interval:
        :param start_str:
        :param end_str:
        :return:
        """

        raise NotImplementedError()
