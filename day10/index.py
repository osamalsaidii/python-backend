my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  
print(next(iterator))  
print(next(iterator))

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)

squares = [x**2 for x in range(10)]

squares_dict = {x: x**2 for x in range(5)}

evens = {x for x in range(10) if x % 2 == 0}

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1


for num in Countdown(5):
    print(num)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
for _ in range(10):
    print(next(fib))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


gen = prime_generator()
for _ in range(20):  
    print(next(gen))
