
#Nikita.Mahindrakar_39.

import calendar

def get_year_input():
    """
    Prompt the user to enter a valid year.
    
    Returns:
        int: A valid year (positive integer).
    """
    while True:
        try:
            year = int(input("Enter the year (e.g., 2025): "))
            if year <= 0:
                raise ValueError("Year must be a positive number.")
            return year
        except ValueError as e:
            print("Invalid input:", e)

def print_calendar(year):
    """
    Print the full calendar of the given year.
    
    Args:
        year (int): The year for which to print the calendar.
    """
    print("\n🗓️  Calendar for the Year", year)
    print("-" * 30)
    # Print the full year calendar with 3 months per row
    cal = calendar.TextCalendar(calendar.SUNDAY)
    full_calendar = cal.formatyear(year, 2, 1, 6)
    print(full_calendar)

def main():
    """
    Main function to run the calendar display program.
    """
    print("📅 Basic Yearly Calendar Display")
    print("===============================")
    year = get_year_input()
    print_calendar(year)

if __name__ == "__main__":
    main()
