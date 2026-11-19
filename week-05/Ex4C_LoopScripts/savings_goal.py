bank_balance = 500
savings_goal = 1000
weely_savings = 100
while bank_balance < savings_goal:
    bank_balance = bank_balance + weely_savings
    print("This week my balance increased to", bank_balance)

    if bank_balance > savings_goal / 2:
     print("Alomst there! This week my balance is up to", bank_balance)

    if bank_balance >= savings_goal * 0.75:
     bank_balance = bank_balance - 20
     print("So close! After treating myself, my balance is up to", bank_balance)

print("Goal met! My current balance is", bank_balance)

