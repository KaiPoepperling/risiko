class Continent(object):
    """
    """
    def __init__(self, name):
        """
        """
        self._name = name
        self._owner = None
        self._regions = dict()

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
        list_region_owner = []
        continent_owner = None
        counter = 0

        for region in self._regions:
            region_object = self._regions[region]
            if region_object.owner is not None:
                list_region_owner.append(region_object.owner)
            else:
                # Error(Log), region has no owner
                pass

        for owner in list_region_owner:
            if continent_owner is None:
                continent_owner = owner
                counter += 1
            elif continent_owner is owner:
                counter+= 1
                if len(list_region_owner) is counter:
                    self._owner = continent_owner
            else:
                break



