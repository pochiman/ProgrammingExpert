##### Physics Class #####

# Create a Physics class that contains no constructor method and three static methods as outlined below.

##### calculate_net_force(mass, acceleration) which returns the product of the passed mass and acceleration.
##### calculate_acceleration(mass, net_force) which returns the quotient of the passed net_force and mass.
##### calculate_mass(net_force, acceleration) which returns the quotient of the passed net_force and acceleration.

# Your static methods should handle any errors cleanly and return the value 0.0 if any error occurs or 
# invalid input is passed.  For the purpose of this question, invalid input is any negative value.

# See below for an example.

# >>> Physics.calculate_net_force(2, 4)
# 8
# >>> Physics.calculate_acceleration(2.5, 35)
# 14.0
# >>> Physics.calculate_mass(40, 10)
# 4.0

class Physics:

    @staticmethod
    def calculate_net_force(mass, acceleration):
        if mass < 0 or acceleration < 0:
            return 0.0

        return mass * acceleration

    @staticmethod
    def calculate_acceleration(mass, net_force):
        # Also checking if mass is 0 because of division by 0 error.
        if mass <= 0 or net_force < 0:
            return 0.0

        return net_force / mass

    @staticmethod
    def calculate_mass(net_force, acceleration):
        # Also checking if acceleration is 0 because of division by 0 error.
        if acceleration <= 0 or net_force < 0:
            return 0.0

        return net_force / acceleration