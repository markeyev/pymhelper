# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from decimal import Decimal

from pymhelper.numbers import (percentage, round_down, split_amount,
                               prep_range)


def test_percentage():
    assert percentage(percent=1, whole=Decimal('100')) == Decimal('1')
    assert percentage(percent=2, whole=Decimal('100')) == Decimal('2')

    assert percentage(percent=Decimal('1.1111'),
                      whole=Decimal('100')) == Decimal('1.1111')

    assert percentage(percent=3,
                      whole=Decimal('44.64548732')) == Decimal('1.3393646196')


def test_round_down():
    assert round_down(Decimal('1234567890'),
                      6) == Decimal('1234567890').normalize()
    assert round_down(Decimal('123456.7890'),
                      1) == Decimal('123456.7').normalize()
    assert round_down(Decimal('1.234567890'),
                      6) == Decimal('1.234567').normalize()


def test_together():
    assert round_down(
        percentage(percent=3,
                   whole=Decimal('44.64548732')), 2) == Decimal('1.33')


def test_split_amount():
    assert split_amount(min_amount=Decimal('10'),
                        whole=Decimal('44')) == [Decimal('11'), Decimal('11'),
                                                 Decimal('11'), Decimal('11')]
    assert split_amount(min_amount=Decimal('0.002'),
                        whole=Decimal('0.003')) == [Decimal('0.003')]
    assert split_amount(min_amount=Decimal('0.001'),
                        whole=Decimal('0.002')) == [Decimal('0.001'),
                                                    Decimal('0.001')]


def test_prep_range():
    assert prep_range(min_value=Decimal('1'),
                      max_value=Decimal('2'),
                      length=4) == [Decimal('1'), Decimal('1.25'),
                                    Decimal('1.5'), Decimal('1.75')]
