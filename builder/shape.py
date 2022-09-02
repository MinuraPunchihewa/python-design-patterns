
class Shape:
    def __init__(self, type=None, length=None, breadth=None):
        self.type = type
        self.length = length
        self.breadth = breadth

    def __str__(self):
        return f"This is a {self.type} shape with a length of {self.length} and a breadth of {self.breadth}!"