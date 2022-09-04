from factory.shape_factory import ShapeFactory

if __name__ == "__main__":
    shape_name = input("Enter the name of the shape: ")
    shape_obj = ShapeFactory.build_shape(shape_name)

    print(shape_obj)
    print(shape_obj.perimeter())