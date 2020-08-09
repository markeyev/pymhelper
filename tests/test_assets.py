# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from decimal import Decimal

from pymhelper.assets import Asset


def test_asset_creation():
    btc = Asset(name='BTC', free=Decimal('1234.5678'), locked=Decimal('0'),
                minimum=Decimal('0'))
    assert btc.free == Decimal('1234.5678')
    assert btc.name == 'BTC'
    assert str(btc) == 'BTC free / locked: 1234.5678 / 0'


def test_asset_creation_from_dict():
    btc = Asset(**dict(name='BTC', free='1234.5678', locked='0', minimum='10'))
    assert btc.free == Decimal('1234.5678')
    assert btc.name == 'BTC'
    assert str(btc) == 'BTC free / locked: 1234.5678 / 0'
    assert btc.minimum == Decimal('10')


def test_auto_field_convert():
    btc = Asset(name='BTC', free=22, locked='0.001', minimum='10')
    assert btc.free == Decimal('22')
    assert btc.locked == Decimal('0.001')
    assert btc.minimum == Decimal('10')


def test_free_round():
    busd = Asset(name='BUSD', free=Decimal('12.3456789'), locked=Decimal('0'),
                 minimum=Decimal('10'))
    assert busd.round() == Decimal('12.345678')
    assert busd.round(2) == Decimal('12.34')


def test_is_enough():
    btc = Asset(name='BTC', free=10, locked=0, minimum=10, step=1)
    assert btc.is_enough is False
    btc = Asset(name='BTC', free=11, locked=0, minimum=10, step=1)
    assert btc.is_enough is False
    btc = Asset(name='BTC', free=11.1, locked=0, minimum=10, step=1)
    assert btc.is_enough is True
