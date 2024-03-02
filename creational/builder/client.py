from director import Director
from square_builder import SquareBuilder
from rectangle_builder import RectangleBuilder


if __name__ == "__main__":
    # construct a square
    square_builder = SquareBuilder()
    square_director = Director(square_builder)
    square = square_director.construct()

    print(square)

    # construct a rectangle
    rectangle_builder = RectangleBuilder()
    rectangle_director = Director(rectangle_builder)
    rectangle = rectangle_director.construct()

    print(rectangle)