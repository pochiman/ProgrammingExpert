##### Temperature Class #####

# Create a Temperature class whose instances all contain a kelvin attribute.  This class should also 
# contain two class attributes named min_temperature and max_temperature which can be modified by 
# calling the respective class methods named update_min_temperature and update_max_temperature.

# min_temperature must always be less than max_temperature and each instances' kelvin attribute 
# must be between min_temperature and max_temperature, inclusively.  Any instantiation or method 
# call that breaks the outlined constraints should raise an Exception.

# Note: min_temperature should be initialized as 0 and max_temperature should be initialized as 1000.

# See below for an example.

# >>> t1 = Temperature(260)
# >>> Temperature.update_max_temperature(270)
# >>> Temperature.update_min_temperature(680)
# Exception: Invalid temperature.
# >>> t2 = Temperature(280)
# Exception: Invalid temperature.
# >>> Temperature.update_min_temperature(100)
# >>> t3 = Temperature(120)
# >>> Temperature.update_max_temperature(90)
# Exception: Invalid temperature.

class Temperature:
    min_temperature = 0
    max_temperature = 1000

    def __init__(self, kelvin):
        if kelvin > self.max_temperature or kelvin < self.min_temperature:
            raise Exception("Invalid temperature.")

        self.kelvin = kelvin

    @classmethod
    def update_min_temperature(cls, kelvin):
        if kelvin > cls.max_temperature:
            raise Exception("Invalid temperature.")

        cls.min_temperature = kelvin

    @classmethod
    def update_max_temperature(cls, kelvin):
        if kelvin < cls.min_temperature:
            raise Exception("Invalid temperature.")

        cls.max_temperature = kelvin