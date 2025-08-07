print("Exercise 1: Sets")


lst = [3, 5, 7, 5, 9, 3]
unique_list = list(set(lst))
print("Unique values:", unique_list)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union (A ∪ B):", A | B)
print("Intersection (A ∩ B):", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference (A ∆ B):", A ^ B)


text = "apple banana apple cherry banana"
words = text.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))

print("\n")


print("Exercise 2: Dictionaries")

student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}
print("Student dictionary:", student)


text2 = "hello world hello"
word_freq = {}
for word in text2.split():
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word frequencies:", word_freq)

squares = {x: x**2 for x in range(1, 6)}
print("Squares dictionary:", squares)

print("\n")




print("Exercise 3: Walrus Operator")

while (num_str := input("Enter a number greater than 10: ")).isdigit() is False or int(num_str) <= 10:
    print("Try again! Number must be > 10.")
print(f"Thank you! You entered {num_str}")

print("\n")




print("Exercise 4: Merge Dictionaries with Conflict Resolution")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = {}

for key, val in dict1.items():
    merged[key] = val

for key, val in dict2.items():
    if (existing := merged.get(key)) is not None:
        merged[f"{key}_resolved"] = existing + val
        merged.pop(key)
    else:
        merged[key] = val

print("Merged dictionary:", merged)