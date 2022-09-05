# Factory Design Pattern

The goal of the Factory Pattern is to help write code that separates creation from use. In other words, you should create your objects in a different place than where you use them.

An example of applying this pattern to an example of creating shapes has been given here.

This pattern is commonly used when we want to allow clients to be able to determine what type of object is required to be created. This can be seen in the implementation of the `client.py` file. The client takes the type of shape to be created as an input from the user and passes this value to the `build_shape()` method of the `ShapeFactory`, which will return an object of that chosen type.

With this, our application has a single point of interaction with other parts of the program, thereby encapsulating the process of creating objects.

## Advantages

A major advantage that employing this pattern offers is that our code becomes loosely coupled with the components of our program.

It helps us include additional functionality without breaking the existing implementation. In our application, this would be done by adding new shapes.

The Factory Pattern helps us maintain the Single Responsibility principle of the SOLID framework as our classes and objects will handle only a single specifically defined task.

Our code will also be more easy to understand and testable.

## Disadvantages

The addition of extra classes will inevitably lead to code that is more verbose and less readable.