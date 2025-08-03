import math
import statistics
import requests
from utils import square_numbers, filter_even


response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    print("Fetched data from API.")
    data = response.json()
   

    numbers = [len(item['title']) for item in data[:10]]
else:
    print("Failed to fetch data.")
    numbers = [10, 15, 22, 7, 9]  # fallback

print(f"\nOriginal numbers: {numbers}")


even_numbers = filter_even(numbers)
squared = square_numbers(even_numbers)

print(f"Even numbers: {even_numbers}")
print(f"Squared even numbers: {squared}")


mean_val = statistics.mean(numbers)
std_dev = statistics.stdev(numbers)
sqrt_first = math.sqrt(numbers[0])

print(f"\nMean: {mean_val}")
print(f"Standard Deviation: {std_dev}")
print(f"Square root of first number: {sqrt_first:.2f}")

