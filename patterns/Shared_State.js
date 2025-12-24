class SharedState {
  constructor() {
    if (SharedState.instance) return SharedState.instance;

    this.data = {};
    SharedState.instance = this;
  }

  set(key, value) {
    this.data[key] = value;
  }

  get(key) {
    return this.data[key];
  }
}