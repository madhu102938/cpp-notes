class Item:
    all_objects = []
    after_discount = 0.8

    def __init__(self, _name:str, _price:int, _quantity=0):
        # checking attributes
        assert _price >= 0, f'price negative'
        assert _quantity >= 0, f'quantity negative'

        # initializing
        self.__name = _name
        self.price = _price
        self.quantity = _quantity

        # extra operations
        Item.all_objects.append(self)

    def get_price(self):
        return self.price * self.quantity

    def price_after_discount(self) -> float:
        return self.price * self.after_discount

    @staticmethod
    def check_if_integer(num):
        if isinstance(num, int):
            return True
        elif isinstance(num, float):
            return num.is_integer()  # return True for XX.0 and False XX.XX
        else:
            return False

    def __repr__(self):
        """
        Represent the Item instance as a string.

        This method provides a formal string representation of the Item instance,
        including its class name, name, price, and quantity attributes. It is useful
        for debugging and logging purposes.

        Returns:
            str: A string representation of the Item instance, formatted as
                 ClassName('name', price, quantity).
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    @property
    def new_prop(self):     # this is a getter
        return "I am inevitable"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, text):
        if len(text) > 10:
            raise Exception('len of text greater than 10')
        else:
            self.__name = text
