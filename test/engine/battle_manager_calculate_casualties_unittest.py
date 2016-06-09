import unittest
from risk.src.engine.battle_manager import BattleManager


class BattleManagerRollTest(unittest.TestCase):
    """
    """
    def test_dice_roll_returns_correct_list_length(self):
        """
        """
        # Given
        dice = BattleManager("test", "test", 2)
        attacker = [5, 5, 2]
        defender = [6, 5]

        # When
        result = dice.calculate_casualties(attacker, defender)

        # Then


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(BattleManagerRollTest)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
