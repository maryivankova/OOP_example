class Human:
"""Create a Human class.
Define two static fields for it: default_name and default_age."""

    default_name = "Kate"
    default_age = 18


    def __init__(self, money, name=default_name, age=default_age, house=None):
   """Create an __init__() method that takes two more parameters in addition to self: name and age. Set these parameters to default values ​​using the default_name and default_age.""" 
        self.name = name
        self.age = age
        self.money = money
        self.house = house


    def info(self):
    """Implement an info() help method that will output the name, age, house, and money fields."""
        print(f'имя:{self.name}, возраст:{self.age},дом: {self.house}, сумма: {self.money}')


    @classmethod
    def default_info(cls):
    """Implement a reference static default_info() method that will output the default_name and default_age static fields."""

        print(f'имя:{cls.default_name}, возраст:{cls.default_age}')


    def make_deal(self, house, price):
    """Implement a private make_deal() method, which will be responsible for the technical implementation of buying a house: reduce the amount of money in the account and assign a link to the newly purchased house. This method takes a house object and its price as arguments."""
        self.money = self.money - house.price
        self.house = House()


    def earn_money(self, summ):
    """Implement the earn_money() method that increments the value of the money property."""
        self.money += summ
     


    def buy_house(self, house, discount):
    """Implement a buy_house() method that will check that the person has enough money to buy and make a deal. If there is too little money, you need to display a warning in the console. Method parameters: house link and discount amount."""

        if house.final_price(discount) < self.money:
            house.make_deal()
        else:
            print("Money is not enoug")


class House:
"""Create a House class"""

    def __init__(self, area, price):
    """Create an __init__() method and define two dynamic properties inside it: _area and _price. They get their initial values ​​from the parameters of the __init__() method."""
        self.area = area
        self.price = price

    def final_price(self, discount=15):
    """Create a final_price() method that takes a discount amount as a parameter and returns the price including the discount."""
        self.price = self.price - discount
        return self.price


class SmallHouse(House):
"""Create a SmallHouse class, inheriting its functionality from the House class."""

    def __init__(self, area, price, square = 40):
    """Inside the SmallHouse class, override the __init__() method to create an object with an area of ​​40m2."""
        super(SmallHouse, self).__init__(area, price)
        self.square = square






        
