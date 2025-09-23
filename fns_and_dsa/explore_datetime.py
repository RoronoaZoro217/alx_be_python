from datetime import datetime, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S') 
    print("Current date and time:", formatted_datetime)

def calculate_future_date(day):
    future_date = datetime.now() + timedelta(days = day)
    return future_date

display_current_datetime()
day = int(input("Enter the number of days to add to the current date:"))
future_date = calculate_future_date(day)
print("Future date:",future_date.strftime('%Y-%m-%d'))
