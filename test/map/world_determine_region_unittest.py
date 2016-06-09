import unittest

from risk.src.map.continent import Continent
from risk.src.map.region import Region
from risk.src.map.world import World


class WorldDetermineRegionTest(unittest.TestCase):
    """
    """
    def test_determine_the_correct_region_in_continents(self):
        """
        """
        # Given
        world = World()

        europe = Continent('Europe')
        germany = Region('Germany')
        spain = Region('Spain')
        france = Region('France')

        spain.set_owner('Heinz')

        europe.add_region(germany)
        europe.add_region(spain)
        europe.add_region(france)

        south_america = Continent('South America')
        argentina = Region('Argentina')
        brazil = Region('Brazil')
        peru = Region('Peru')
        venezuela = Region('Venezuela')

        south_america.add_region(argentina)
        south_america.add_region(brazil)
        south_america.add_region(peru)
        south_america.add_region(venezuela)

        world.add_continent(europe)
        world.add_continent(south_america)

        # When
        region = world.determine_region_object('Spain')

        # Then
        self.assertEqual(region.owner, 'Heinz')

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(WorldDetermineRegionTest)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
