def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

try:
    with open("input.txt", "r") as infile:
        words = [line.strip() for line in infile]

    palindromes = [word.upper() for word in words if is_palindrome(word)]

    with open("palindromes.txt", "w") as outfile:
        for word in palindromes:
            outfile.write(word + "\n")

except FileNotFoundError:
    print("Error: 'input.txt' not found.")
except IOError:
    print("Error: File could not be read or written.")
