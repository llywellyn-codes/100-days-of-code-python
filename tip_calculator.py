def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

print("Welcome to the tip calculator!")

bill = get_float("What was the total bill? $")
tip = get_float("What percentage tip would you like to give? (e.g., 10, 12, 15): ")
people = get_int("How many people to split the bill? ")

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_person = total_bill / people

print(f"Each person should pay: ${bill_per_person:.2f}")
