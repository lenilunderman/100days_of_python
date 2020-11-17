# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the Tip Calculator")
bill_amount = float(input("What was the total bill? $ "))
tip_percentage = int(
    input("What percentage tip you would like to give? 10, 12, 15? "))
number_people = int(input("How many people will split the bill? "))

bill_with_tip = (tip_percentage / 100) * bill_amount + bill_amount
bill_per_person = bill_with_tip / number_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay $ {final_amount}")
