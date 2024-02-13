from builder import ShapeBuilder


class SquareDirector:
    @staticmethod
    def construct():
        return ShapeBuilder()\
            .set_type("Square")\
            .set_length(4)\
            .get_result()
