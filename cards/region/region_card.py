class RegionCard(object):
    """
    """
    def __init__(self, name, continent, unit):
        """
        """
        self._name = name
        self._continent = continent
        self._unit = unit

    @property
    def name(self):
        """
        """
        return self._name

    @property
    def continent(self):
        """
        """
        return self._continent

    @property
    def unit(self):
        """
        """
        return self._unit
