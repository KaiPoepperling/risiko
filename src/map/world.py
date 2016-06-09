class World(object):
    """
    """
    def __init__(self):
        """
        """
        self._continents = dict()

    @property
    def continents(self):
        """
        """
        return self._continents

    def add_continent(self, continent):
        """
        """
        self._continents[continent.name] = continent

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

    def determine_region_object(self, region_name):
        """Determines the region object in continents dictionary
        """
        for continent in self._continents:
            for region in continent.regions:
                if region.name is region_name:
                    return region

__all__ = [World.__name__]
