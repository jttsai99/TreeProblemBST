class Donor(object):
    """
    Maybe it would be a good idea to a make a simple donor class
    """

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return str(self.name) + "  with a donation of " + str(self.amount)

    def __str__(self):
        return str(self.name) + "  with a donation of " + str(self.amount)