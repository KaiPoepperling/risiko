from random import randint

class Dice(object):
    """
    """
    def __init__(self):
        """
        """
        pass

    def roll(self, number):
        """
        """
        result = list()

        for i in range(number):
            random_number = randint(1, 6)
            result.append(random_number)

        result = sorted(result, reverse=True)

        return result

__all__ = [Dice.__name__]
