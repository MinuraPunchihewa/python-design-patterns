import copy


class Prototype:
    """
    A prototype class to clone objects.

    Attributes
    ----------
    _objects: dict
        A dictionary to store the objects to be cloned.
    """
    
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """
        Register an object to be cloned with a name.

        Parameters
        ----------
        name: str
            The name of the object to be registered.
        obj: obj
            The object to be registered.        
        """

        self._objects[name] = obj

    def unregister_object(self, name):
        """
        Unregister an object from the list of objects to be cloned.

        Parameters
        ----------
        name: str
            The name of the object to be unregistered.
        """

        del self._objects[name]

    def clone(self, name, **attr):
        """
        Clone a registered object and update its attributes, if required.

        Parameters
        ----------
        name: str
            The name of the object to be cloned.
        attr: dict
            A dictionary of attributes to update after cloning.

        Returns
        -------
        obj
            A cloned object.
        """

        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj