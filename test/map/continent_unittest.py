import unittest

from risk.src.map.continent import Continent
from risk.src.map.region import Region


class ContinentTest(unittest.TestCase):
    """
    """
    def test_check_continent_has_correct_owner(self):
        """
        """
        # Given
        europe = Continent('Europe')
        germany = Region('Germany')
        spain = Region('Spain')
        france = Region('France')

        europe.add_region(germany)
        europe.add_region(spain)
        europe.add_region(france)

        germany.set_owner('Kai')
        spain.set_owner('Kai')
        france.set_owner('Kai')

        # When
        europe.check_continent_has_owner()

        # Then
        self.assertEqual(europe.owner, 'Kai')

    def test_check_continent_has_no_owner(self):
        """
        """
        # Given
        europe = Continent('Europe')
        germany = Region('Germany')
        spain = Region('Spain')
        france = Region('France')

        europe.add_region(germany)
        europe.add_region(spain)
        europe.add_region(france)

        germany.set_owner('Kai')
        spain.set_owner('Hannes')
        france.set_owner('Kevin')

        # When
        europe.check_continent_has_owner()

        # Then
        self.assertEqual(europe.owner, None)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(ContinentTest)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
