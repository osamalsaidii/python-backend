def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"[Call Counter] Function '{func.__name__}' called {wrapper.call_count} times.")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@call_counter
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("osama")
say_hello("ahmad")
say_hello("mohammad")
print(f"[Call Counter] Final count: {say_hello.call_count}")