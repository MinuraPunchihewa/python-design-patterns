from factory import IShape


class Square(IShape):
    def __init__(self, dimensions: dict):
        self.length = dimensions['length']

    def perimeter(self):
        """
        Calculates the perimeter of a Square.
        """
        return f"The perimeter of the Square is {self.length * 4}!"

    def __str__(self) -> str:
        return f"This is a Square with a length of {self.length}!"
