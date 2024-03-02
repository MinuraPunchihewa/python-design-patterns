# Borg

Borg is a variation of the Singleton design pattern. Unlike the Singleton, Borg allows for the creation of multiple instances of the class, but all instances share the same state. This is achieved by making the `__dict__` attribute of the instances point to the same dictionary.

## Implementation Details (Shared State)

In Python, every object has a `__dict__` attribute, which is a dictionary that stores the object's attributes and their values. When you do something like `self.x = 10`, Python is actually adding a key-value pair to this dictionary: `{'x': 10}`.

n the Borg class, self.`__dict__` is assigned to self._shared_state, which is a class attribute. Class attributes in Python are shared among all instances of the class. So, by making `__dict__` point to a class attribute, you're making all instances of the class share the same attribute dictionary.

1. When you create an instance of Borg, its __init__ method is called.
2. self.`__dict__` = self._shared_state is executed. This makes the instance's attribute dictionary (`__dict__`) point to the class's _shared_state dictionary.
3. Now, any changes to the instance's attributes are actually changes to _shared_state, because `__dict__` is just a reference to _shared_state.
4. When you create another instance of Borg, the same thing happens. Its `__dict__` also points to _shared_state.
5. Now, both instances' attribute dictionaries are pointing to the same dictionary. So, changes to the attributes of one instance are reflected in the other.