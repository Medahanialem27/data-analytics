
current_savings = 1000.00
interest_rate = 6.0

years_to_double = 72 / interest_rate
doubled_balance = current_savings * 2

print("Your current savings is $" + format(current_savings, " .2f") +".")
print("At a " + format(interest_rate / 100, ".0%") +
 " interest rate, your savings account will be worth $" +
format(doubled_balance, ".2f") + " in " +
format(years_to_double, ".1f") + " years")
