from builder import SquareDirector
from builder import RectangleDirector


if __name__ == "__main__":
    # construct a square
    square = SquareDirector.construct()

    print(square)

    # construct a rectangle
    rectangle = RectangleDirector.construct()

    print(rectangle)