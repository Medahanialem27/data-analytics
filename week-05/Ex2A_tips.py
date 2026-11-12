# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the total
total_due = food_cost + tax + tip

# str() converts the number to text so it can be joined with the message.
print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
print("The total due is " + str(total_due))
#print("Tips is " + fromat(tip))
print("Tip is " + format(tip, ".2f"))
