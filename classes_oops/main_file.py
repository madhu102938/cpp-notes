from item import Item
from phone import Phone


def main():
    # Use a breakpoint in the code line below to debug your script.
    item1 = Item('phone', 100, 1)
    item2 = Item('computer', 1000, 2)

    # print(item1.get_price())

    # for instance in Item.all_objects:
    #     print(instance)

    # print(item1.price_after_discount())

    # print(Item.check_if_integer('9'))

    phone1 = Phone(False, 'oneplus', 101, 2)
    # print(phone1.price, phone1.quantity, phone1.name, phone1.broken, phone1.get_price(), phone1.price_after_discount(),
    #       phone1)
    #
    # print(Item.all_objects[-1])

    # getters, setters, fixed attributes @property @attribute.setter
    # encapsulation, abstraction
    # polymorphism

    # what if we want to have unchangeable attributes, then we need to create a special getter
    # item1.new_prop = 'something else'   # gives an error
    # print(item1.new_prop)

    # but how to make an attribute we defined in `__init__()` method, unchangeable?
    # ofcourse we create a new getter for it, we need to change the attribute inside the class
    # to __name this will make the attribute `private` (inaccessible from outside the class)
    # print(item1.__name)     # will give us an error
    # print(item1.name)

    # but now, how do we change this `name` attribute? we need to create a setter for it
    # item1.name = 'phone99'
    # print(item1.name)

    # We can place some conditions inside setters
    # item1.name = '12338329421'  # raises an exception

    # 1. Encapsulation, hiding some things, we can do this by self.__name = something
    # 2. Abstraction, hiding complex part and just giving simple interface to user
    #    we can do this by `def __somefunction():` this function won't be accessible
    #    from outside
    # 3. Inheritance, taking methods from parent classes, so we don't need to rewrite the same
    #    code again and again
    # 4. Polymorphism, one thing being able to represent multiple things,
    #    like len(str) will give number of character, but len(list) gives us number of elements


if __name__ == '__main__':
    main()
