from .data_storage import save_data #Why is there a . before storage?

def register_new_member(data):
   name = input("Enter the new estate member's name here:\t")
   address = input("Enter new member's address\t")

   member = {
      "name": name,
      "address": address
   } 

   data["members"].append(member)

   save_data(data)

   print(f"{name} has been registered successfully.")


def show_all_members(data):
   if not data["members"]:
      print("There are no registered members yet.")
      return

   print("\nRegistered Members:")

   for member in data["members"]:
      print(f"Name: {member["name"]}") 
      print(f"Address: {member["address"]}")    
      print("-" * 30)

    