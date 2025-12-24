// --- Product ---
class Pizza {
  prepare() {
    throw new Error("Must implement prepare()");
  }
}

class NYStyleCheesePizza extends Pizza {
  prepare() {
    return "Preparing NY-style cheese pizza";
  }
}

class ChicagoStyleCheesePizza extends Pizza {
  prepare() {
    return "Preparing Chicago-style cheese pizza";
  }
}

// --- Creator ---
class PizzaStore {
  orderPizza(type) {
    const pizza = this.createPizza(type);
    return pizza.prepare();
  }

  createPizza(type) {
    throw new Error("Subclass must implement createPizza()");
  }
}

// --- Concrete Creators ---
class NYPizzaStore extends PizzaStore {
  createPizza(type) {
    if (type === "cheese") return new NYStyleCheesePizza();
    throw new Error("Unknown pizza type");
  }
}

class ChicagoPizzaStore extends PizzaStore {
  createPizza(type) {
    if (type === "cheese") return new ChicagoStyleCheesePizza();
    throw new Error("Unknown pizza type");
  }
}

// --- Usage ---
const store = new NYPizzaStore();
console.log(store.orderPizza("cheese"));