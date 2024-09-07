class MenuItem:
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("latte", 2.5, {"water": 200, "milk": 150, "coffee": 24}),
            MenuItem("espresso", 1.5, {"water": 50, "coffee": 18}),
            MenuItem("cappuccino", 3.0, {"water": 250, "milk": 100, "coffee": 24})
        ]

    def get_items(self):
        return [item.name for item in self.menu]


    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        return None


class CoffeeMaker:

    def __init__(self):
        self.water = 500
        self.milk = 300
        self.coffee = 70

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")

    def is_resource_sufficient(self, drink):
        if drink.ingredients.get("water") > self.water:
            return False
        if drink.ingredients.get("milk") > self.milk:
            return False
        if drink.ingredients.get("coffee") > self.coffee:
            return False
        return True

    def make_coffee(self, order):
        self.water -= order.ingredients.get("water")
        self.milk -= order.ingredients.get("milk")
        self.coffee -= order.ingredients.get("coffee")



class MoneyMachine:
    def __init__(self):
        self.profit = 0
        self.penny = 0.01
        self.nickel = 0.05
        self.dime = 0.10
        self.quarter = 0.25

    def report(self):
        print(f"Money: {self.profit}")

    def make_payment(self, cost):
        print("Please insert coins.")
        total = 0
        total += int(input("How many pennies?: "))
        total += int(input("How many nickels?: "))
        total += int(input("How many dimes?: "))
        total += int(input("How many quarters?: "))

        if total >= cost:
            extra = total - cost
            self.profit += cost
            print(f"Here is ${extra}")
            return True
        else:
            print("not enough")
            return False


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()



def order(choice, menu, coffee_maker, money_machine):
    drink = menu.find_drink(choice)
    if drink:
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                print(f"Here is your {choice}. Enjoy!")
            else:
                print("not enough money")
        else:
            print("not enough resources")
    else:
        print(f"we don't have {choice}")


On = True

while On:
    coffe = menu.get_items()
    Order= input(f"What would you like? ({coffe}):")
    if Order == "off":
        On = False
    elif Order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order(Order, menu, coffee_maker, money_machine)
