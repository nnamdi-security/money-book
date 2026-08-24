from estate_manager.data_storage import load_data
from estate_manager.estate_tenants import show_all_members, register_new_member


data = load_data()
register_new_member(data)
show_all_members(data)

