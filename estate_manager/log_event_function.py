from datetime import datetime #package/module/file?

def log_event(message):
    current_time = datetime.now()

    with open("diary.txt", "a") as file:
        file.write(f"{current_time} - {message}\n")


#"new events are added to the end, never wiping what came before". What does that here?

log_event("Test event")
print("Diary entry added.")