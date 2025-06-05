# Global conversion factors
FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5
FREEZING_POINT_DIFFERENCE = 32  # Offset for Fahrenheit to Celsius


def convert_to_celsius(fahrenheit):
    """
    Converts temperature from Fahrenheit to Celsius.

    Parameters:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    global FAHRENHEIT_TO_CELSIUS, FREEZING_POINT_DIFFERENCE
    return (fahrenheit - FREEZING_POINT_DIFFERENCE) * FAHRENHEIT_TO_CELSIUS


def convert_to_fahrenheit(celsius):
    """
    Converts temperature from Celsius to Fahrenheit.

    Parameters:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    global CELSIUS_TO_FAHRENHEIT, FREEZING_POINT_DIFFERENCE
    return (celsius * CELSIUS_TO_FAHRENHEIT) + FREEZING_POINT_DIFFERENCE


def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)

        unit_input = input(
            "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit_input == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temp:.2f}°C")
        elif unit_input == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temp:.1f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError as ve:
        print(f"Error: {ve}")
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()
