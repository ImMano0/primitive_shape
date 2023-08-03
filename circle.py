from math import pi
class Circle:
    def __init__(self, r) -> None:
        self.r = r

    def getArea(self):
        """
        This method finds the area of the Circle.

        Args:
            No
        Returns:
            float or int: result.
        """
        r = self.r
        f = pi*r*r
        return f 

    def getLength(self):
        """
        This method finds the length of the cirle.

        Args:
            No
        Returns:
            float or int: result..
        """
        r = self.r
        m = pi*r*2
        return m 
x = Circle(1)    
print(x.getArea())
print(x.getLength())
