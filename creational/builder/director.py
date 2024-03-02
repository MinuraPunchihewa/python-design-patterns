
class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.set_type()
        self._builder.set_length()
        self._builder.set_breadth()

        return self._builder.shape