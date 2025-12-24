from abc import ABC, abstractmethod

# --- Abstract Products ---
class Dough(ABC):
    pass

class Sauce(ABC):
    pass

# --- Concrete Products ---
class ThinCrustDough(Dough):
    pass

class ThickCrustDough(Dough):
    pass

class MarinaraSauce(Sauce):
    pass

class PlumTomatoSauce(Sauce):
    pass

# --- Abstract Factory ---
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abstractmethod
    def create_sauce(self) -> Sauce:
        pass

# --- Concrete Factories ---
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

# --- Client (Pizza) ---
class Pizza:
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.factory = ingredient_factory

    def prepare(self):
        dough = self.factory.create_dough()
        sauce = self.factory.create_sauce()
        return f"Prepared pizza with {dough.__class__.__name__} and {sauce.__class__.__name__}"

# --- Usage ---
pizza = Pizza(NYPizzaIngredientFactory())
print(pizza.prepare())