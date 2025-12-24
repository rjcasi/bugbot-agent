class Singleton {
  constructor() {
    if (Singleton.instance) {
      return Singleton.instance;
    }
    Singleton.instance = this;
  }
}

// --- Usage ---
const s1 = new Singleton();
const s2 = new Singleton();

console.log(s1 === s2); // true