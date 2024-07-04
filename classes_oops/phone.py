from item import Item

class Phone(Item):

    def __init__(self, _broken:bool, *args):
        # super().__init__()
        super().__init__(args[0], args[1], args[2])  # calling this would take us to constructor of parent class

        self.broken = _broken
