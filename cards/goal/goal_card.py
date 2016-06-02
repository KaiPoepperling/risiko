class GoalCard(object):
    """
    """
    def __init__(self, number, description, army):
        """
        """
        self._number = number
        self._description = description
        self._army = army

    @property
    def number(self):
        """
        """
        return self._number

    @property
    def description(self):
        """
        """
        return self._description

    @property
    def army(self):
        """
        """
        return self._army
