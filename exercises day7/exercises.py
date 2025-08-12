print("\n--- Exercise 1: Basic Class and Object ---")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."



person1 = Person("osama", 22)
person2 = Person("alsaidi", 25)
print(person1.introduce())
print(person2.introduce())



print("\n--- Exercise 2: Instance vs Class Variables ---")
class Dog:
    species = "Canis familiaris" 

    def __init__(self, name, breed):
        self.name = name     
        self.breed = breed   

    def describe(self):
        return f"{self.name} is a {self.breed}. Species: {self.species}."



dog1 = Dog("sky", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")
print(dog1.describe())
print(dog2.describe())


dog1.species = "Canis lupus familiaris"  
print("After modifying species for dog1:")
print(dog1.describe()) 
print(dog2.describe())  



print("\n--- Exercise 3: Bank Account with Validation ---")
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")

    def get_balance(self):
        return self.balance



account = BankAccount("John Doe", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)  
print(f"Final balance: ${account.get_balance()}")


print("\n--- Exercise 4: Library System ---")
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed book: {book.title}")
                return
        print(f"No book with ISBN {isbn} found.")

    def list_books(self):
        if not self.books:
            return "No books in the library."
        return "\n".join(book.display_info() for book in self.books)



library = Library()
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "0987654321")

library.add_book(book1)
library.add_book(book2)
print("Books in library:")
print(library.list_books())

library.remove_book("1234567890")
print("Books after removal:")
print(library.list_books())


print("\n--- Exercise 5: Class Variable Counter ---")
class Car:
    total_cars = 0  

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1  

    def display_car(self):
        return f"{self.make} {self.model}"

    @staticmethod
    def get_total_cars():
        return Car.total_cars



car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

print(car1.display_car())
print(car2.display_car())
print(f"Total cars created: {Car.get_total_cars()}")
