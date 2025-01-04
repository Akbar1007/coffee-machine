import json

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self, menu_file="python/menu/menu.json"):
        self.menu = []
        self.load_menu(menu_file)

        # self.menu = [
        #     MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
        #     MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
        #     MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        #     MenuItem(name="americano", water=300, milk=0, coffee=24, cost=2),
        #     MenuItem(name="macchiato", water=200, milk=50, coffee=24, cost=2.5),
        #     MenuItem(name="flat white", water=150, milk=150, coffee=18, cost=2.5),
        #     MenuItem(name="ristretto", water=30, milk=0, coffee=18, cost=1.5),
        #     MenuItem(name="lungo", water=70, milk=0, coffee=18, cost=1.5)
        # ]

    def load_menu(self, menu_file):
        """Loads menu items from a JSON file."""
        try:
            with open(menu_file, "r") as file:
                items = json.load(file)
                for item in items:
                    self.menu.append(MenuItem(
                        name=item["name"],
                        water=item["water"],
                        milk=item["milk"],
                        coffee=item["coffee"],
                        cost=item["cost"]
                    ))
        except FileNotFoundError:
            print(f"Error: The file '{menu_file}' was not found.")
        # except json.JSONDecodeError:
        #     print(f"Error: The file '{menu_file}' contains invalid JSON.")


    def get_items(self):
        """Returns all the names of the available menu items"""
        if not self.menu:
            print("Menu is empty!")
        options = ""

        for item in self.menu:
            options += f"${item.cost} - {item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
