// --- Subject ---
class Subject {
  constructor() {
    this.observers = [];
  }

  register(observer) {
    this.observers.push(observer);
  }

  unregister(observer) {
    this.observers = this.observers.filter(o => o !== observer);
  }

  notify(data) {
    this.observers.forEach(o => o.update(data));
  }
}

// --- Observers ---
class Logger {
  update(data) {
    console.log(`[Logger] Received: ${data}`);
  }
}

class SpikeMonitor {
  update(data) {
    console.log(`[SpikeMonitor] Spike event: ${data}`);
  }
}

// --- Usage ---
const subject = new Subject();
subject.register(new Logger());
subject.register(new SpikeMonitor());

subject.notify("Neuron 12 fired");