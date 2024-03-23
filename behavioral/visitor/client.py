from circle import Circle
from square import Square
from rectangle import Rectangle

from area_visitor import AreaVisitor
from perimeter_visitor import PerimeterVisitor


if __name__ == "__main__":
    shapes = [Circle(2), Rectangle(2, 3), Square(2)]
    area_visitor = AreaVisitor()
    perimeter_visitor = PerimeterVisitor()
    for shape in shapes:
        print(f"Area of {shape.__class__.__name__}: {shape.accept(area_visitor)}")
        print(f"Perimeter of {shape.__class__.__name__}: {shape.accept(perimeter_visitor)}")