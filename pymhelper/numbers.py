"""Set of function related to numbers, math, percentages.
"""
from decimal import Decimal, ROUND_DOWN
from typing import Union, List


def percentage(*, percent: Union[int, Decimal], whole: Decimal) -> Decimal:
    """Returns percentage of a number.

    :param percent: for example Decimal('105.95'), means 105.95%.
    :param whole:
    :return:
    """
    return Decimal((percent * whole) / 100)


def round_down(number: Decimal, decimals: int = 6) -> Decimal:
    """Round down decimal.

    :param number:
    :param decimals:
    :return:
    """
    return number.quantize(Decimal(10) ** -decimals,
                           rounding=ROUND_DOWN).normalize()


def split_amount(*, min_amount: Decimal, whole: Decimal) -> List[Decimal]:
    """Splits number into almost equal parts of the whole number which are
    greater then min_amount.

    For example 56 / 10 = 11.2.

    :param min_amount:
    :param whole:
    :return:
    """
    parts = whole // min_amount
    return [whole / parts for _ in range(int(parts))]


def prep_range(*,
               min_value: Decimal,
               max_value: Decimal,
               length: int) -> List[Decimal]:
    """Example:

    prep_range(min_value=Decimal('0.001'), max_value=Decimal('0.005'),
               length=5)
        [
            Decimal('0.0010'), Decimal('0.0018'), Decimal('0.0026'),
            Decimal('0.0034'), Decimal('0.0042')
        ]

    :param min_value:
    :param max_value:
    :param length:
    :return:
    """
    step = (max_value - min_value) / length
    return [min_value + Decimal(step) * i for i in range(length)]
