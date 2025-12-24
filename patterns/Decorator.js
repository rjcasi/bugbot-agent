// --- Component ---
class Beverage {
  cost() {
    throw new Error("Must implement cost()");
  }
}

// --- Concrete Component ---
class Espresso extends Beverage {
  cost() {
    return 2.00;
  }
}

// --- Decorator Base ---
class AddOnDecorator extends Beverage {
  constructor(beverage) {
    super();
    this.beverage = beverage;
  }
}

// --- Concrete Decorators ---
class Mocha extends AddOnDecorator {
  cost() {
    return this.beverage.cost() + 0.50;
  }
}

class Whip extends AddOnDecorator {
  cost() {
    return this.beverage.cost() + 0.30;
  }
}

// --- Usage ---
let drink = new Espresso();
drink = new Mocha(drink);
drink = new Whip(drink);

console.log(drink.cost()); // 2.80