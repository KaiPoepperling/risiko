class Region(object):
    """
    """
    def __init__(self, name):
        """
        """
        self._name = name
        self._owner = None
        self._units = 0

    @property
    def name(self):
        """
        """
        return self._name

    @property
    def owner(self):
        """
        """
        return self._owner

    @property
    def units(self):
        """
        """
        return self._units

    def _increase_units(self, units):
        """
        """
        self._units += units

    def _decrease_units(self, units):
        """
        """
        self._units -= units

    def _set_owner(self, new_owner):
        """
        """
        self._owner = new_owner

__all__ = [Region.__name__]
