# Builder Design Pattern

The Builder Pattern and Factory Pattern are both quite similar in the sense that they both create objects at runtime. They are also able to separate the creation of objects from their use.

However, the main difference between the two is that the Builder Pattern focuses on creating complex objects, one step at a time.

The Builder Pattern has been applied to an example of creating shapes here. The `Shape` objects created here are not very complex, but the implementation is accurate.

In this example, `Shape` is the object being built, and the steps to build an object is provided by the `ShapeBuilder`, which implements the `IShapeBuilder` interface.

The `Director` classes for each 'type' of `Shape` contains a `construct()` method, which creates a customized object by calling the methods of the `ShapeBuilder`.

## Advantages

## Disadvantages