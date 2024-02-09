import pytest


@pytest.mark.run
def test_one():
    assert True

@pytest.mark.run
def test_two():
    a = 10
    b = 10
    assert a == b, 'No son iguales'
    assert a != b, 'Son iguales'
    assert a < b, 'A es mayor que B'
    assert a > b, 'A es menor que B'

@pytest.mark.run
def test_three():
    a = 5
    b = 10
    assert a==b, 'No son iguales'

@pytest.mark.run
def test_four():
    a = 15
    b = 10
    assert a > b,  'A no es mayor que B'


@pytest.mark.run
def test_five():
    name = 'Clara'
    assert name == 'Veronica', 'El nombre no es Veronica'