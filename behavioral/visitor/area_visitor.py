from visitor import IVisitor


class AreaVisitor(IVisitor):
    def visit_rectangle(self, rectangle):
        return rectangle.width * rectangle.height

    def visit_circle(self, circle):
        return 3.14 * circle.radius ** 2

    def visit_square(self, square):
        return square.length ** 2