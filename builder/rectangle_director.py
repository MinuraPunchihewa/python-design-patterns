from builder import ShapeBuilder


class RectangleDirector:
    @staticmethod
    def construct():
        return ShapeBuilder()\
            .set_type("Rectangle")\
            .set_length(6) \
            .set_breadth(5) \
            .get_result()
