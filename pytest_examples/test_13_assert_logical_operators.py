import pytest


@pytest.mark.asserts
def test_assert_1():
    a = 10
    b = 30

    assert a < b, "A no es menor que B"

@pytest.mark.asserts
def test_assert_2():
    a = 10
    b = 30

    assert a > b, "A no es mayor que B"

@pytest.mark.asserts
def test_assert_3():
    a = 17
    b = 13
    c = 12
    assert a < b or c > b, 'La condicion no se cumple'

@pytest.mark.asserts
def test_assert_4():
    a = 17
    b = 13
    c = 12
    assert a > b and c > b, 'B no es el elemento menor'