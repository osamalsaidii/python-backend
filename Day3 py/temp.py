def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        celsius = input("Enter temperature in Celsius: ")
        try:
            celsius = float(celsius)
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        fahrenheit = input("Enter temperature in Fahrenheit: ")
        try:
            fahrenheit = float(fahrenheit)
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()