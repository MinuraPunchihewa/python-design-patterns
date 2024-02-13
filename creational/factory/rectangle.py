from factory import IShape


class Rectangle(IShape):
    def __init__(self, length: int, breadth: int):
        self.length = int(length)
        self.breadth = int(breadth)

    def perimeter(self):
        """
        Calculates the perimeter of a Rectangle.
        """
        perimeter = (self.length * 2) + (self.breadth * 2)
        return f"The perimeter of the Rectangle is {perimeter}!"

    def __str__(self) -> str:
        return f"This is a Rectangle with a length of {self.length} and a breadth of {self.breadth}!"


# class Rectangle(IShape):
#     def __init__(self, dimensions: dict):
#         self.length = dimensions['length']
#         self.breadth = dimensions['breadth']
#
#     def perimeter(self):
#         """
#         Calculates the perimeter of a Rectangle.
#         """
#         return f"The perimeter of the Rectangle is {self.length * 2 + self.breadth * 2}!"
#
#     def __str__(self) -> str:
#         return f"This is a Rectangle with a length of {self.length} and a breadth of {self.breadth}!"
