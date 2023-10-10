import pytest
from tests.hw_14.car import Car
import sys


class TestCar:

    def setup_class(self):
        print('\nTest class')
        # self.new_car = Car('KIA', 'Sportage')

    def setup_method(self):
        print('Test setup')
        self.new_car = Car('KIA', 'Sportage')

    def teardown_method(self):
        print('\nTest teardown')

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

    def test_model_type(self):
        """
        negative test
        @preCond: create new car object
        @Steps: raise error if the model is not a string and send integer
        Assert: error raised
        """
        new_car = self.new_car
        with pytest.raises(TypeError, match='Oops! Model name must be string'):
            new_car.model = 300

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

    def test_start_engine(self, capsys):
        """
        @preCond: create new car object
        @Steps: start engine
        Assert: message received and engine started
        """
        new_car = self.new_car
        new_car.start_engine()
        captured = capsys.readouterr()
        assert captured.out == "Engine started."

    def test_engine_started(self, capsys):
        """
        @preCond: work with the same car object created in the previous test
        @Steps: start engine
        Assert: "already started" message received
        """
        new_car = self.new_car
        new_car.start_engine()
        new_car.start_engine()
        captured = capsys.readouterr()
        assert captured.out == "Engine is already running."
