from factory import IShape


class Square(IShape):
    def __init__(self, length: int):
        self.length = int(length)

    def perimeter(self):
        """
        Calculates the perimeter of a Square.
        """
        perimeter = self.length * 4
        return f"The perimeter of the Square is {perimeter}!"

    def __str__(self) -> str:
        return f"This is a Square with a length of {self.length}!"


# class Square(IShape):
#     def __init__(self, dimensions: dict):
#         self.length = dimensions['length']
#
#     def perimeter(self):
#         """
#         Calculates the perimeter of a Square.
#         """
#         return f"The perimeter of the Square is {self.length * 4}!"
#
#     def __str__(self) -> str:
#         return f"This is a Square with a length of {self.length}!"
