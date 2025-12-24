from abc import ABC, abstractmethod

# --- Product ---
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

class NYStyleCheesePizza(Pizza):
    def prepare(self):
        return "Preparing NY-style cheese pizza"

class ChicagoStyleCheesePizza(Pizza):
    def prepare(self):
        return "Preparing Chicago-style cheese pizza"

# --- Creator ---
class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, type_: str) -> Pizza:
        pass

    def order_pizza(self, type_: str):
        pizza = self.create_pizza(type_)
        return pizza.prepare()

# --- Concrete Creators ---
class NYPizzaStore(PizzaStore):
    def create_pizza(self, type_: str):
        if type_ == "cheese":
            return NYStyleCheesePizza()
        raise ValueError("Unknown pizza type")

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, type_: str):
        if type_ == "cheese":
            return ChicagoStyleCheesePizza()
        raise ValueError("Unknown pizza type")

# --- Usage ---
store = NYPizzaStore()
print(store.order_pizza("cheese"))