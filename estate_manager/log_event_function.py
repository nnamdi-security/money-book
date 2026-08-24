from datetime import datetime #package/module/file?

def log_event(message):
    current_time = datetime.now()

    with open("diary.txt", "a") as file:
        file.write(f"{current_time} - {message}\n")


