from i_decorator import IDecorator


class BoldDecorator(IDecorator):
    def render(self):
        return f'<b>{self._tag.render()}</b>'