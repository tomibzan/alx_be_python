
# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32


def convert_to_celsius(fahrenheit):
    """
    Converts temperature from Fahrenheit to Celsius.
    Uses global conversion factor.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_OFFSET
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Converts temperature from Celsius to Fahrenheit.
    Uses global conversion factor.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FAHRENHEIT_OFFSET
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET


def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)

        unit_input = input(
            "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit_input == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {celsius:.1f}°C")
        elif unit_input == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {fahrenheit:.1f}°F")
        else:
            raise ValueError(
                "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        print(f"Error: {ve}")
        print("Error: Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()
