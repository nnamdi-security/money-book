from estate_manager.data_storage import load_data
from estate_manager.estate_tenants import show_all_members, register_new_member
from estate_manager.payment_record import record_payment, show_payment_history


data = load_data()
#record_payment(data)
#register_new_member(data)
#show_all_members(data)

show_payment_history(data)