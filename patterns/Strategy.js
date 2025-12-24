// --- Strategies ---
class FlyWithWings {
  fly() {
    return "Flying with wings!";
  }
}

class FlyNoWay {
  fly() {
    return "I can't fly.";
  }
}

// --- Context ---
class Duck {
  constructor(flyBehavior) {
    this.flyBehavior = flyBehavior;
  }

  performFly() {
    return this.flyBehavior.fly();
  }

  setFlyBehavior(fb) {
    this.flyBehavior = fb;
  }
}

// --- Usage ---
const duck = new Duck(new FlyWithWings());
console.log(duck.performFly()); // Flying with wings!

duck.setFlyBehavior(new FlyNoWay());
console.log(duck.performFly()); // I can't fly.