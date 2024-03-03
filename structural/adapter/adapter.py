
class Adapter:
    def __init__(self, obj, **adapted_method):
        self._obj = obj
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._obj, attr)