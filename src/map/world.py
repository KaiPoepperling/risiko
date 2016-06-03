class World(object):
    """
    """
    def __init__(self, name):
        """
        """
        self._continents = dict()

    @property
    def continents(self):
        """
        """
        return self._continents

    def _get_region_owner(self, region_name):
        """
        """
        region = self._continents
        owner = region

    def _get_region_units(self, region):
        """
        """
        pass

    def _change_region_owner(self, new_owner, region):
        """
        """
        pass

    def _determine_region_object(self, region_name):
        """Determines the region object in continents dictionary
        """

__all__ = [World.__name__]
