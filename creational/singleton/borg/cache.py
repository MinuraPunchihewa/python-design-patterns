from borg import Borg


class Cache(Borg):
    def __init__(self, **kwargs):
        super().__init__()
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)

    def get(self, key):
        return self._shared_state.get(key)

    def set(self, key, value):
        self._shared_state[key] = value

    def delete(self, key):
        del self._shared_state[key]