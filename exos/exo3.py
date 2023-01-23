from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    pass

class AerialVehicle(metaclass=ABCMeta):

  
    def __init__(self, brand, fuel):
        """Initialize the unmanned vehicule"""

    def get_brand(self):
        """Get the brand of a vehicule"""

  
    def set_brand(self, brand):
        """Get the brand of a vehicule"""

    def get_fuel(self):
        """Get fuel"""

    def set_fuel(self, fuel):
        """Get fuel"""

    def nohuman_presentation(self):
        """Test if the vehicul is unmanned"""

    def get_default_brand(cls):
        """Get the default brand"""

class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    pass

class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    pass

class UAV():
    """Unmanned Aerial Vehicle"""
    pass

class UUV():
    """Unmanned Undersea Vehicle"""
    pass

class UGV():
    """Unmanned Ground Vehicle"""
    pass


uav = UAV()
uav.do_something_interesting()
uav.do_something_aerial_specific()

ugv = UGV()
ugv.do_something_interesting()
ugv.do_something_ground_specific()

uuv = UUV()
uuv.do_something_interesting()
uuv.do_something_undersea_specific()

