import pytest


@pytest.fixture(scope='module')
def setup_one():
    print('Start setup 1')
    yield
    print('Finish setup 1')

@pytest.fixture(scope='module')
def setup_two():
    print('Start setup 2')
    yield
    print('Finish setup 2')

@pytest.fixture(scope='module')
def setup_three():
    print('Start setup 3')
    yield
    print('Finish setup 3')

def test_one(setup_one):
    print('Test one')

def test_two(setup_two):
    print('Test two')

@pytest.mark.usefixtures('setup_three')
def test_three():
    print('Test three')

@pytest.mark.usefixtures('setup_three')
def test_four():
    print('Test four')