def display_mailing_labe(name, address, city, state, zip):
    print(f"{name}\n{address}\n{city}, {state} {zip}")

display_mailing_labe("Amina Example", "123 Oak Street", "Oakland", "CA", "94607")
display_mailing_labe("Daniel Example", "456 Pine Avenue", "Berkeley", "CA", "94704")

def add_numbers(*numbers):
    total = sum(numbers)
    equation = " + " .join(str(number) for number in numbers)
    print(f"{equation} = {total}")

add_numbers(8)
add_numbers(8, 12)
add_numbers(2, 4, 6, 8)

def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if amount_paid >= total_due:
        change_due = amount_paid - total_due
        print(f"Change Due: ${change_due:.2f}")
    else:
        remaining = total_due - amount_paid
        print(f"Remaining Balance: ${remaining:.2f}")

display_receipt(25, 30) # overpay
display_receipt(25, 25) #exact payment
display_receipt(25, 20) #underpay

