import pytest
from tests.hw_14.car import Car


def setup_class():
    print('\nTest class')


def teardown_method():
    print('\nTest teardown')


class TestCar:

    def setup_method(self):
        print('Test setup')
        self.new_car = Car('KIA', 'Sportage ')

    def test_change_model(self):
        """
        @preCond: create new car object
        @Steps: change model
        Assert: model changed
        """
        new_car = self.new_car
        excepted_model = f'Picanto' or f'Ceratto'
        new_car.model = excepted_model
        assert new_car.model == excepted_model

    def test_change_brand(self):
        """
        @preCond: create new car object
        @Steps: change brand
        Assert: brand changed
        """
        new_car = self.new_car
        excepted_brand = f'Mercedes' or f'Toyota'
        new_car.brand = excepted_brand
        assert new_car.brand == excepted_brand

    def test_start_engine(self):
        """
        @preCond: create new car object
        @Steps: start engine
        Assert: message received and engine started
        """
        new_car = self.new_car
        expected_message = 'Engine started.'
        assert new_car.start_engine() == expected_message

    def test_engine_started(self):
        """
        @preCond: work with the same car object created in the previous test
        @Steps: start engine
        Assert: "already started" message received
        """
        new_car = self.new_car
        new_car.start_engine()
        new_car.start_engine()
        expected_message = 'Engine is already running.'
        assert new_car.start_engine() == expected_message

    def test_stop_engine(self):
        """
        @preCond: create new car object
        @Steps: start engine, stop engine
        Assert: message received and engine stopped
        """
        new_car = self.new_car
        new_car.start_engine()
        expected_message = 'Engine stopped.'
        assert new_car.stop_engine() == expected_message

    def test_stop_engine_stopped(self):
        """
        @preCond: create new car object
        @Steps: start engine, stop engine, try to stop it one more time
        Assert: expected message received
        """
        new_car = self.new_car
        new_car.start_engine()
        new_car.stop_engine()
        expected_message = 'Engine is already off.'
        assert new_car.stop_engine() == expected_message

    def test_drive_engine_stopped(self):
        """
        @preCond: create new car object
        @Steps: start engine, stop engine, try to drive
        Assert: expected message received
        """
        new_car = self.new_car
        new_car.start_engine()
        new_car.stop_engine()
        expected_message = 'Cannot drive. Engine is off.'
        assert new_car.drive(5) == expected_message


assert isinstance(pytest.mark.smoke, object)


def test_drive_limit_larger(get_new_car):
    """
        @preCond: create new car object with limit 10
        @Steps: start engine, drive 5 miles
        Assert: expected message received
        """
    new_car = get_new_car
    new_car.start_engine()
    expected_message = 'Driving 5 miles.'
    assert new_car.drive(5) == expected_message


def test_drive_limit_equal(get_new_car):
    """
    @preCond: create new car object with limit 10
    @Steps: start engine, drive 10 miles
    Assert: expected message received
    """
    new_car = get_new_car
    new_car.start_engine()
    expected_message = 'Driving 10 miles.'
    assert new_car.drive(10) == expected_message


def test_drive_limit_less(get_new_car):
    """
    @preCond: create new car object with limit 10
    @Steps: start engine, try to drive 11 miles
    Assert: expected message received
    """
    new_car = get_new_car
    new_car.start_engine()
    expected_message = 'The miles limit has been exceeded'
    assert new_car.drive(11) == expected_message
