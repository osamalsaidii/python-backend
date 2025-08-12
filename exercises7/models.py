class Student:
    school_name = "Default School" 

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, score):
        if 0 <= score <= 100:
            self.grades.append(score)
        else:
            print(f"Invalid grade '{score}'. Must be between 0 and 100.")

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def student_info(self):
        avg = self.average_grade()
        return f"Student: {self.name}, School: {Student.school_name}, Average Grade: {avg:.2f}"


class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if isinstance(item, MenuItem):
            self.items.append(item)
        else:
            print("Only MenuItem objects can be added.")

    def remove_item(self, name):
        for i, item in enumerate(self.items):
            if item.name == name:
                del self.items[i]
                print(f"Removed '{name}' from the order.")
                return
        print(f"Item '{name}' not found in the order.")

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def display_order(self):
        if not self.items:
            return "Order is empty."
        result = "Order Items:\n"
        for item in self.items:
            result += f" - {item.display()}\n"
        result += f"Total: ${self.calculate_total():.2f}"
        return result