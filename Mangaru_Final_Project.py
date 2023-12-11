from datetime import datetime


#PART A GREETING

#Gets the current time
def get_current_time():
    return datetime.now().time()

#Deternines if the current time is moring or afternoon
def is_morning(current_time):
    return current_time < datetime.strptime("12:00", "%H:%M").time()

#Formats the current time from 24hour format to 12hour format
def format_time_12_hour(current_time):
    return current_time.strftime("%I:%M %p")

#Creates a greeting message saying good moring or good afternoon during the appriate times and the current time
def get_greeting_message():
    current_time = get_current_time()
    formatted_time = format_time_12_hour(current_time)

    if is_morning(current_time):
        return f"Good morning Brian! The current time is {formatted_time}."
    else:
        return f"Good afternoon Brian! The current time is {formatted_time}."

def main():

#PART A GREETING
# prints the greeting message
    greeting_message = get_greeting_message()
    print(greeting_message)

if __name__ == "__main__":
    main()

