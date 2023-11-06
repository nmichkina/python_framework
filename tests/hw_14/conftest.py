import pytest
from tests.hw_14.car import Car


@pytest.fixture(scope='function')
def get_new_car():
    print('\nSetup')
    new_car = Car('Toyota', 'Yaris', 10)
    yield new_car
    print('\nTeardown')
