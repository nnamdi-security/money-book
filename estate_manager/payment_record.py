from .data_storage import save_data
from .log_event_function import log_event as logger

def record_payment(data):
    if not data["members"]:
        print("There are no registered members yet")
        return

    name = input("Enter member's name:\t")

    member_found = False

    for member in data["members"]:
        if member["name"].lower() == name.lower():
            member_found = True
            break

    if not member_found:
        print("Member not found")
        return
        
    month = input("Enter payment month:\t")

    for payment in data["payments"]:
        if (
            payment["member"].lower() == name.lower()
            and payment["month"].lower() == month.lower()
        ):
            print("A payment for this member and month already exists.")
            return
        
    amount = int(input("Enter payment amount:\t"))

    payment = {
        "name": name.title(),
        "month": month.title(),
        "amount": amount
    }

    data["payments"].append(payment)

    save_data(data)

    logger(f"Payment recorded: {name} paid {amount} for month of {month}")
    print("Payment recorded successfully.")