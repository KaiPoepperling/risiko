from risk.src.map.world_factory import WorldFactory

class BattleManager(object):
    """
    """
    def __init__(self, attack_region, defend_region, units):
        """
        """
        self.attacker = attack_region
        self.defender = defend_region
        self.attacking_units = units

        self.world = WorldFactory.get_world()

    def attack(self):
        """
        """
        pass

    def _roll_dice(self):
        """
        """
        pass

__all__ = [BattleManager.__name__]
