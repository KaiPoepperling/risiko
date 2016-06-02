class Continent(object):
    """
    """
    def __init__(self):
        """
        """
        self._owner = None
        self._regions = dict()

    @property
    def owner(self):
        """
        """
        return self._owner

    @property
    def regions(self):
        """
        """
        return self._regions

    def add_region(self, region):
        """
        """
        self._regions[region.name] = region

    def check_continent_has_owner(self):
        """
        """
        owner = None
        for region in self._regions:
            if region.owner is not None:
                if owner is None:
                    owner = region.owner
                if owner is not region.owner:
                    # Log continent has not just one owner
                    return false
                else:
                    self._owner = owner
            else:
                # Log region has no owner

