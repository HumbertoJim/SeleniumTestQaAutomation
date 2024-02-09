from library.commons import Data
import pytest


@pytest.mark.asserts
def test_assert_1():
    word = "Lorem"

    assert word in Data.LOREM_IPSUM, f"La frase no contiene la palabra {word}"

@pytest.mark.asserts
def test_assert_2():
    word = "Pakal"

    assert word in Data.LOREM_IPSUM, f"La frase no contiene la palabra {word}"