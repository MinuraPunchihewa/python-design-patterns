
class Shape:
    def __init__(self):
        self.type = None
        self.length = None
        self.breadth = None

    def __str__(self):
        return f"This is a {self.type} shape with a length of {self.length} and a breadth of {self.breadth}!"