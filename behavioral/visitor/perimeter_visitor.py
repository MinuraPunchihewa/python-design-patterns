from i_visitor import IVisitor


class PerimeterVisitor(IVisitor):
    def visit_rectangle(self, rectangle):
        return 2 * (rectangle.width + rectangle.height)

    def visit_circle(self, circle):
        return 2 * 3.14 * circle.radius

    def visit_square(self, square):
        return 4 * square.length