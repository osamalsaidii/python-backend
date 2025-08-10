def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

try:
    with open("celsius.txt", "r") as infile:
        lines = infile.readlines()

    with open("fahrenheit.txt", "w") as outfile:
        for line in lines:
            try:
                celsius = float(line.strip())
                fahrenheit = celsius_to_fahrenheit(celsius)
                outfile.write(f"{celsius:.1f}C = {fahrenheit:.1f}F\n")
            except ValueError:
                print(f"Invalid temperature value: '{line.strip()}' skipped.")

except FileNotFoundError:
    print("Error: 'celsius.txt' not found.")
except IOError:
    print("Error: Could not read/write file.")
