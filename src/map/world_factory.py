class WorldFactory(object):
    """
    """
    _world = None

    @staticmethod
    def get_world():
        """
        """
        if not WorldFactory._world:
            WorldFactory._world = WorldFactory()

        return WorldFactory._world

__all__ = [WorldFactory.__name__]
