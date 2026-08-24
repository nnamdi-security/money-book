from estate_manager.data_storage import save_data, load_data

data = {
    "memebers": [
        {"name": "Ajala"}
    ],
    "payments": []
}

#save_data(data)

print("Data saved")

loaded_data = load_data()
print(loaded_data)