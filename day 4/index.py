numbers = [10, 25, 35, 20, 40, 50, 35, 15]


first = numbers[0]
last = numbers[-1]


middle = numbers[2:5]  
print("Original List:", numbers)
print("First Element:", first)
print("Last Element:", last)
print("Sliced List [2:5]:", middle)


numbers.append(60)
numbers.remove(20)
numbers.sort()

print("After appending 60 and removing 20, sorted list:", numbers)

squared = [x ** 2 for x in numbers]
print("Squared List (list comprehension):", squared)


even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)


coordinates = (10.5, 20.3)


print("Coordinates Tuple:", coordinates)


def min_max(lst):
    return min(lst), max(lst)

min_val, max_val = min_max(numbers)
print("Min and Max of numbers:", (min_val, max_val))




set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Union of Sets:", union_set)


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = dict1 | dict2
print("Merged Dictionary (dict1 | dict2):", merged_dict)


def find_second_largest(lst):
    unique = list(set(lst)) 
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

nums = [10, 25, 35, 20, 40, 50, 35, 15]
second_largest = find_second_largest(nums)
print("Second Largest Number:", second_largest)

student_scores1 = {"Alice": 85, "Bob": 78}
student_scores2 = {"Bob": 90, "Charlie": 88}


merged_scores = student_scores1 | student_scores2
print("Merged Student Scores:", merged_scores)
