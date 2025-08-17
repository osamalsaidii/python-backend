def validate_positive_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"[Input Validator] All inputs must be positive. Found: {arg}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive_numbers
def add_positive_numbers(a, b):
    return a + b

print("[Input Validator] add_positive_numbers(5, 10):", add_positive_numbers(5, 10))  

