# 1: Create a program that greets the user based on the current time.
# (e.g., "Good Morning" before noon, "Good Afternoon" in the afternoon, and "Good Evening" in the evening). 
# Use the datetime module to retrieve the current time and conditionally display a greeting.

from datetime import datetime

currentTime=datetime.now()
currentHour=currentTime.hour

if 1<=currentHour<12:
    greet="Good Morning"
elif 12<=currentHour<18:
    greet="Good Afternoon"
else:
    greet="Good Evening"

print(f"{greet}! The current time is : {currentTime.strftime('%H:%M')}")


# 2: Write a Python program that asks the user to input two dates in ( YYYY-MM-DD) format and 
# calculates the number of days between the two dates. Use the datetime module to perform the calculation.

from datetime import datetime
def calculateDays():
    date1_str=input("Enter the first date (YYYY-MM-DD):")
    date2_str=input("Enter the second date (YYYY-MM-DD):")

    try:
        d1=datetime.strptime(date1_str,"%Y-%m-%d")
        d2=datetime.strptime(date2_str,"%Y-%m-%d")
        
        diff=abs(d2-d1)
        print(f"Number of days between {date1_str} and {date2_str} is {diff.days} days.")

    except ValueError:
        print("Invalid date format! Please use the formate like YYYY-MM-DD ")

calculateDays()