Note on Iterables and Iterators:

Iterables serve as containers for data, providing a way to access their elements, while iterators provide the mechanism to iterate over the elements of these containers sequentially. Here's a breakdown of each:

Iterables:

Iterables are objects that contain a sequence of elements.
They implement the __iter__() method, which returns an iterator object when called.
Iterables can be looped over directly using a for loop or other iterable-consuming constructs.
Iterators:

Iterators are objects that represent the state of iteration over an iterable.
They implement the __iter__() method to return themselves as iterators and the __next__() method to retrieve the next element in the iteration.
Iterators keep track of the current state of iteration, allowing for sequential access to elements of the iterable.
So, to iterate over the elements of an iterable, Python first obtains an iterator from the iterable using the __iter__() method. Then, it repeatedly calls the __next__() method of the iterator to retrieve elements until a StopIteration exception is raised, indicating that there are no more elements to iterate over.

By separating iterables and iterators, Python provides a clear and flexible mechanism for working with collections of data, promoting code clarity, modularity, and reusability.