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

    def increase_units(self, units):
        """
        """
        self._units += units

    def decrease_units(self, units):
        """
        """
        self._units -= units

    def set_owner(self, new_owner):
        """
        """
        self._owner = new_owner
