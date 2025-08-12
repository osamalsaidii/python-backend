from classes import Person, Dog, BankAccount, Book, Library, Car

print("\n--- Exercise 1: Basic Class and Object ---")
person1 = Person("osama", 22)
person2 = Person("alsaidi", 25)
print(person1.introduce())
print(person2.introduce())

print("\n--- Exercise 2: Instance vs Class Variables ---")
dog1 = Dog("sky", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")
print(dog1.describe())
print(dog2.describe())

dog1.species = "Canis lupus familiaris"
print("After modifying species for dog1:")
print(dog1.describe())
print(dog2.describe())

print("\n--- Exercise 3: Bank Account with Validation ---")
account = BankAccount("John Doe", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)
print(f"Final balance: ${account.get_balance()}")

print("\n--- Exercise 4: Library System ---")
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
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

print(car1.display_car())
print(car2.display_car())
print(f"Total cars created: {Car.get_total_cars()}")



from models import Student, MenuItem, Order

def main():
  
    s = Student("osama")
    s.add_grade(88)
    s.add_grade(92)
    s.add_grade(105) 
    print(s.student_info())

    print()

    
    menu_item1 = MenuItem("Caesar Salad", 7.99, "Appetizer")
    menu_item2 = MenuItem("Steak", 24.99, "Main Course")
    menu_item3 = MenuItem("Cheesecake", 6.50, "Dessert")

    order = Order()
    order.add_item(menu_item1)
    order.add_item(menu_item2)
    order.add_item(menu_item3)
    print(order.display_order())

    order.remove_item("Steak")
    print("\nAfter removing Steak:")
    print(order.display_order())

if __name__ == "__main__":
    main()
