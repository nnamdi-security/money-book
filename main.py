from estate_manager.data_storage import load_data
from estate_manager.estate_tenants import show_all_members, register_new_member
import estate_manager.payment_record as payments


data = load_data()


while True:
    print("\n========================================")
    print("       ESTATE UNION DUES TRACKER")
    print("========================================")
    print("1. Register member")
    print("2. View members")
    print("3. Record payment")
    print("4. View payment history")
    print("5. View owing members")
    print("6. View up-to-date members")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        register_new_member(data)

    elif choice == "2":
        show_all_members(data)

    elif choice == "3":
        payments.record_payment(data)

    elif choice == "4":
        payments.show_payment_history(data)

    elif choice == "5":
        payments.show_owing_members(data)

    elif choice == "6":
        payments.show_up_to_date_members(data)

    elif choice == "7":
        print("Thank you for using the Estate Union Due App.")
        break

    else:
        print("Invalid choice. Please try again.")
