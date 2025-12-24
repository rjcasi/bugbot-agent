// --- Abstract Products ---
class Dough {}
class Sauce {}

// --- Concrete Products ---
class ThinCrustDough extends Dough {}
class ThickCrustDough extends Dough {}
class MarinaraSauce extends Sauce {}
class PlumTomatoSauce extends Sauce {}

// --- Abstract Factory ---
class PizzaIngredientFactory {
  createDough() { throw "Not implemented"; }
  createSauce() { throw "Not implemented"; }
}

// --- Concrete Factories ---
class NYPizzaIngredientFactory extends PizzaIngredientFactory {
  createDough() { return new ThinCrustDough(); }
  createSauce() { return new MarinaraSauce(); }
}

class ChicagoPizzaIngredientFactory extends PizzaIngredientFactory {
  createDough() { return new ThickCrustDough(); }
  createSauce() { return new PlumTomatoSauce(); }
}

// --- Client ---
class Pizza {
  constructor(factory) {
    this.factory = factory;
  }

  prepare() {
    const dough = this.factory.createDough();
    const sauce = this.factory.createSauce();
    return `Prepared pizza with ${dough.constructor.name} and ${sauce.constructor.name}`;
  }
}

// --- Usage ---
const pizza = new Pizza(new NYPizzaIngredientFactory());
console.log(pizza.prepare());