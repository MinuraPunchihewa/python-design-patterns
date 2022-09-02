from factory.shape_factory import ShapeFactory

if __name__ == "__main__":
    # build a square
    square = ShapeFactory.build_shape(
        'Square',
        {
            "length": 4
        }
    )

    print(square)
    print(square.perimeter())

    # build a rectangle
    rectangle = ShapeFactory.build_shape(
        'Rectangle',
        {
            "length": 6,
            "breadth": 5
        }
    )

    print(rectangle)
    print(rectangle.perimeter())