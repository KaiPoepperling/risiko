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

        # When
        attacker = dice.roll(3)
        defender = dice.roll(2)

        # Then
        self.assertEqual(len(attacker), 3)
        self.assertEqual(len(defender), 2)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(BattleManagerRollTest)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
