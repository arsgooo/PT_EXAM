def days_in_month(month):
    months = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    if month in months:
        return months[month]
    else:
        raise ValueError("Invalid month name")

if __name__ == "__main__":
    user_input = "January"
    try:
        result = days_in_month(user_input)
        print(f"{user_input} has {result} days.")
    except ValueError as e:
        print(e)
