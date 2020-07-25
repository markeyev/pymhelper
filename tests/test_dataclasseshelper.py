# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from dataclasses import dataclass
from decimal import Decimal

from pymhelper.dataclasseshelper import AutoConvertingField


@dataclass
class TestDataClass(AutoConvertingField):
    dec: Decimal
    num: int
    string: str


def test_auto_convert():
    tdc = TestDataClass(dec='5.5001', num='5', string=5)
    assert isinstance(tdc.dec, Decimal)
    assert tdc.dec == Decimal('5.5001')
    assert isinstance(tdc.num, int)
    assert tdc.num == 5
    assert isinstance(tdc.string, str)
    assert tdc.string == '5'
