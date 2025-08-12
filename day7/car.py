class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_started = False

    def start(self):
        self.is_started = True
        print(f"{self.brand} {self.model} is now started.")

    def stop(self):
        self.is_started = False
        print(f"{self.brand} {self.model} is now stopped.")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Wheels: {Car.wheels}")



if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Honda", "Civic", 2022)

    car1.start()
    car2.info()
    car1.stop()
