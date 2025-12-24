from abc import ABC, abstractmethod

# --- Strategies ---
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        return "Flying with wings!"

class FlyNoWay(FlyBehavior):
    def fly(self):
        return "I can't fly."

# --- Context ---
class Duck:
    def __init__(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior

    def perform_fly(self):
        return self.fly_behavior.fly()

    def set_fly_behavior(self, fb: FlyBehavior):
        self.fly_behavior = fb


# --- Usage ---
duck = Duck(FlyWithWings())
print(duck.perform_fly())   # Flying with wings!

duck.set_fly_behavior(FlyNoWay())
print(duck.perform_fly())   # I can't fly.