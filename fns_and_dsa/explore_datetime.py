from datetime import datetime, timedelta


def display_current_datetime():
    """
    Display current date and time>'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date


def calculate_future_date(current_date):
    """
    Ask the user for a number of days to add, calculate and display the future date.
    """
    try:
        days_to_add = int(
            input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    current_time = display_current_datetime()
    calculate_future_date(current_time)
