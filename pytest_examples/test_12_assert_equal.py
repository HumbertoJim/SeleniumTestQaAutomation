import pytest


@pytest.mark.asserts
def test_assert_1():
    nom1 = "Gepeto"
    nom2 = "Carlota"

    assert nom1 == nom2, "Los nombres no son iguales"

@pytest.mark.asserts
def test_assert_2():
    nom1 = "Jim"
    nom2 = "Jim"

    assert nom1 == nom2, "Los nombres no son iguales"