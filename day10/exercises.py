class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return 0
        elif self.count == 1:
            self.count += 1
            return 1
        else:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.b


print("Exercise 1: Fibonacci sequence up to 10 terms")
fib = Fibonacci(10)
for num in fib:
    print(num, end=' ')
print("\n")



def alternating_signs(numbers):
    sign = 1
    for num in numbers:
        yield sign * abs(num)
        sign *= -1


print("Exercise 2: Alternating signs")
nums = [1, 2, 3, 4, 5]
for val in alternating_signs(nums):
    print(val, end=' ')
print("\n")



print("Exercise 3: Word character ASCII mapping")
words = ["hello", "world"]
ascii_dict = {
    word: {char: ord(char) for char in word}
    for word in words
}
print(ascii_dict)
print("\n")



print("Exercise 4: Uppercase vowels in string")
text = "The quick brown fox jumps over the lazy dog"
vowels = {'a', 'e', 'i', 'o', 'u'}
found_vowels = {char.upper() for char in text.lower() if char in vowels}
print(found_vowels)
print("\n")



def primes():
    num = 2
    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1


print("Exercise 5: First 6 prime numbers")
prime_gen = primes()
for _ in range(6):
    print(next(prime_gen), end=' ')
print()
