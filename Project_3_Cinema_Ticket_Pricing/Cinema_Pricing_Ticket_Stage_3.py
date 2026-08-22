# Ask for the customer's age and day type
age = int(input("Age: "))
day_type = input("Day type (weekday/weekend): ")

# Determine the ticket price based on age and day type
if age < 5:
    price = 0
elif age <= 12:
    if day_type == "weekday":
        price = 1500
    else:
        price = 2000
elif age <= 59:
    if day_type == "weekday":
        price = 2500
    else:
        price = 3500
else:
    if day_type == "weekday":
        price = 1200
    else:
        price = 1800

# Display the calculated ticket price in the required format
print(f"Price: {price}")
