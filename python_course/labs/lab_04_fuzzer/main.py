import traceback
from utils import random_input

def target_function(x):
    """A simple function that expects an integer."""
    return x * 2

def fuzz(iterations=50):
    errors = []

    for i in range(iterations):
        value = random_input()
        try:
            result = target_function(value)
            print(f"[OK] Input: {value!r} -> Output: {result!r}")
        except Exception as e:
            print(f"[ERR] Input: {value!r} -> {type(e).__name__}")
            errors.append({
                "input": repr(value),
                "error": type(e).__name__,
                "trace": traceback.format_exc()
            })

    return errors

def summarize(errors):
    summary = {}
    for err in errors:
        summary.setdefault(err["error"], 0)
        summary[err["error"]] += 1
    return summary

def main():
    print("Running safe Python fuzzer...\n")
    errors = fuzz(50)

    print("\n=== Error Summary ===")
    summary = summarize(errors)
    for err_type, count in summary.items():
        print(f"{err_type}: {count}")

if __name__ == "__main__":
    main()
