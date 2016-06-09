from random import randint
from risk.src.map.world_factory import WorldFactory

class BattleManager(object):
    """
    """
    def __init__(self, attack_region, defend_region, attack_units, defend_units):
        """
        """
        self.world = WorldFactory.get_world()

        self.attacker = attack_region
        self.defender = defend_region
        self.attacking_units = attack_units
        self.defending_units = defend_units

    def attack(self):
        """
        """
        pass

    def roll(self, number):
        """Rolls a number of random int between 1 and 6.
        """
        result = list()

        for i in range(number):
            random_number = randint(1, 6)
            result.append(random_number)

        result = sorted(result, reverse=True)

        return result

    def calculate_casualties(self, attacker, defender):
        """
        """
        attacker_casualties = 0
        defender_casualties = 0

        for i in range(len(defender)):
            if attacker[i] > defender[i]:
                defender_casualties += 1
            else:
                attacker_casualties += 1

        # Ziehe Einheiten aus region ab

__all__ = [BattleManager.__name__]
