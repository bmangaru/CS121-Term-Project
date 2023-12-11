from datetime import datetime

def get_current_time():
    return datetime.now().time()

def is_morning(current_time):
    return current_time < datetime.strptime("12:00", "%H:%M").time()

def format_time_12_hour(current_time):
    return current_time.strftime("%I:%M %p")

def get_greeting_message():
    current_time = get_current_time()
    formatted_time = format_time_12_hour(current_time)

    if is_morning(current_time):
        return f"Good morning Brian! The current time is {formatted_time}."
    else:
        return f"Good afternoon Brian! The current time is {formatted_time}."

def main():
    greeting_message = get_greeting_message()
    print(greeting_message)

if __name__ == "__main__":
    main()

