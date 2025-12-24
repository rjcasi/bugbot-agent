from abc import ABC, abstractmethod

# --- Component ---
class Beverage(ABC):
    @abstractmethod
    def cost(self):
        pass

# --- Concrete Component ---
class Espresso(Beverage):
    def cost(self):
        return 2.00

# --- Decorator Base ---
class AddOnDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

# --- Concrete Decorators ---
class Mocha(AddOnDecorator):
    def cost(self):
        return self.beverage.cost() + 0.50

class Whip(AddOnDecorator):
    def cost(self):
        return self.beverage.cost() + 0.30

# --- Usage ---
drink = Espresso()
drink = Mocha(drink)
drink = Whip(drink)

print(drink.cost())  # 2.80