'''This is an example Module'''

from math import pi

class Circle():
    """A class for circles

    :param radius: The radius of the circle
    :type radius: int
    """

    def __init__(self, radius):
        """Constructor method
        """
        self.radius = radius

    def calcCircumference(self, radius):
        """Calculates the circumference for a given radius

        :param radius: The input radius
        :type radius: int
        :return: The circumference for a given radius
        :rtype: float
        """
        return pi * 2 * radius