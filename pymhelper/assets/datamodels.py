"""Assets represented in dataclasses format.
"""

from dataclasses import dataclass
from decimal import Decimal

from pymhelper.dataclasseshelper import AutoConvertingField
from pymhelper.numbers import round_down


@dataclass
class Asset(AutoConvertingField):
    """Base or quote asset.
    """
    name: str
    free: Decimal
    locked: Decimal

    minimum: Decimal
    step: Decimal = Decimal('0')

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return (f'{self.name} free / locked: {self.free} / '
                f'{self.locked}')

    @property
    def is_enough(self) -> bool:
        """Check is free asset enough to buy or sell.
        :return:
        """
        return self.free > self.minimum + self.step

    def round(self, precision: int = 6) -> Decimal:
        """Returns rounded free asset.

        :param precision:
        :return:
        """
        return round_down(self.free, precision)
