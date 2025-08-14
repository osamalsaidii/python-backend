class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance  
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Balance for account {self.account_number}: ${self.__balance}")

    @property
    def balance(self):
        return self.__balance

    def __str__(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder}, Balance: ${self.__balance:.2f}"

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.account_number == other.account_number
        return False


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
       
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.balance - amount < 100:
            print("Cannot withdraw. Balance cannot go below $100.")
        else:
            
            self._Account__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def __str__(self):
        return f"SavingsAccount[{self.account_number}] - Holder: {self.account_holder}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate*100:.2f}%"


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.balance - amount < -self.overdraft_limit:
            print(f"Cannot withdraw. Overdraft limit of ${self.overdraft_limit} exceeded.")
        else:
            self._Account__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def __str__(self):
        return f"CheckingAccount[{self.account_number}] - Holder: {self.account_holder}, Balance: ${self.balance:.2f}, Overdraft Limit: ${self.overdraft_limit}"



class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.__price = price 
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    def apply_discount(self, percent):
        if 0 <= percent <= 100:
            discount_amount = self.__price * (percent / 100)
            self.__price -= discount_amount
            print(f"Applied {percent}% discount. New price: ${self.__price:.2f}")
        else:
            print("Invalid discount percent.")

    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Restocked {amount}. New quantity: {self.quantity}")
        else:
            print("Restock amount must be positive.")

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        if self.product_id != other.product_id:
            print("Cannot add products with different IDs.")
            return None
        
        new_price = (self.price + other.price) / 2
        return Product(self.product_id, self.name, new_price, self.quantity + other.quantity)

    def __call__(self):
        print(f"Product Summary:\nID: {self.product_id}\nName: {self.name}\nPrice: ${self.price:.2f}\nQuantity: {self.quantity}")

    def __str__(self):
        return f"Product[{self.product_id}] - {self.name}: ${self.price:.2f}, Qty: {self.quantity}"


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, file_size):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size  

    def apply_discount(self, percent):
        
        if percent > 20:
            percent = 20
        super().apply_discount(percent)

    def __str__(self):
        return f"DigitalProduct[{self.product_id}] - {self.name}: ${self.price:.2f}, Qty: {self.quantity}, File Size: {self.file_size}MB"


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight  

    def apply_discount(self, percent):
        if 0 <= percent <= 100:
            discount_amount = self.price * (percent / 100)
            new_price = self.price - discount_amount
            if new_price < 5:
                print("Discount cannot reduce price below $5.")
            else:
                self._Product__price = new_price
                print(f"Applied {percent}% discount. New price: ${self.price:.2f}")
        else:
            print("Invalid discount percent.")

    def __str__(self):
        return f"PhysicalProduct[{self.product_id}] - {self.name}: ${self.price:.2f}, Qty: {self.quantity}, Weight: {self.weight}kg"




class Person:
    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.__email = email  

    def display_info(self):
        print(f"ID: {self.id}\nName: {self.name}\nEmail: {self.__email}")

    @property
    def email(self):
        return self.__email

    def __repr__(self):
        return f"Person(id={self.id!r}, name={self.name!r}, email={self.__email!r})"


class Student(Person):
    def __init__(self, id_, name, email, major, gpa=0.0):
        super().__init__(id_, name, email)
        self.major = major
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}.")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.gpa < other.gpa

    def __repr__(self):
        return f"Student(id={self.id!r}, name={self.name!r}, email={self.email!r}, major={self.major!r}, gpa={self.gpa!r})"


class Professor(Person):
    def __init__(self, id_, name, email, department):
        super().__init__(id_, name, email)
        self.department = department
        self.courses_teaching = []

    def assign_course(self, course):
        self.courses_teaching.append(course)
        print(f"{self.name} assigned to teach {course}.")

    def __repr__(self):
        return f"Professor(id={self.id!r}, name={self.name!r}, email={self.email!r}, department={self.department!r})"



if __name__ == "__main__":
   
    print("=== Banking System ===")
    sa = SavingsAccount("123", "Alice", 500, 0.03)
    sa.display_balance()
    sa.withdraw(450)  
    sa.withdraw(350)  
    sa.deposit(200)
    print(sa)

    ca = CheckingAccount("456", "Bob", 200, overdraft_limit=100)
    ca.withdraw(250)  
    ca.withdraw(100)  
    print(ca)
    print(sa == ca)  
    sa2 = SavingsAccount("123", "Alice", 1000)
    print(sa == sa2) 
 
    print("\n=== Product System ===")
    p1 = DigitalProduct(1, "E-book", 50, 100, 500)
    p2 = DigitalProduct(1, "E-book", 60, 50, 500)
    p1.apply_discount(30)  
    p1()
    p3 = p1 + p2
    print(p3)

    p4 = PhysicalProduct(2, "Laptop", 1000, 10, 2.5)
    p4.apply_discount(10)
    p4.apply_discount(95)  
    p4()

   
    print("\n=== University System ===")
    student1 = Student(1, "Charlie", "charlie@example.com", "Computer Science", 3.5)
    student2 = Student(2, "Diana", "diana@example.com", "Mathematics", 3.8)
    student1.enroll("CS101")
    student2.enroll("MATH202")

    professor = Professor(100, "Dr. Smith", "smith@university.edu", "Computer Science")
    professor.assign_course("CS101")

    print(student1)
    print(student2)
    print(student1 < student2)  
    print(professor)
