import json

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open("data.json", "r") as file: # as "file"?
            return json.load(file)
        
    except FileNotFoundError:
        return {
            "members": [],
            "payments": []
        }

    except json.JSONDecodeError:
        print("Sorry, the data file appears to be corrupted.")
        print("The program will now start with an empty data")

        return {
            "members": [],
            "payments": []
        }