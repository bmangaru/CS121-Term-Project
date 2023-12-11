from datetime import datetime

# PART A GREETING

# Gets the current time
def get_current_time():
    return datetime.now()

# Determines if the current time is morning or afternoon
def is_morning(current_time):
    return current_time.hour < 12

# Formats the current time from 24-hour format to 12-hour format
def format_time_12_hour(current_time):
    return current_time.strftime("%I:%M %p")

# Formats the current date
def format_date(current_time):
    return current_time.strftime("%Y-%m-%d")

# Creates a greeting message saying good morning or good afternoon during the appropriate times and the current time
def get_greeting_message():
    current_time = get_current_time()
    formatted_time = format_time_12_hour(current_time)

    if is_morning(current_time):
        return f"Good morning Brian! The current time is {formatted_time}."
    else:
        return f"Good afternoon Brian! The current time is {formatted_time}."

# PART B MEDICINE LOGGING

# Asks whether the user has taken their medicine and logs the response and time in a file
def log_medicine_taken():
    response = input("Have you taken your medicine? (y/n): ").lower()
    current_time = get_current_time()
    formatted_date = format_date(current_time)
    formatted_time = format_time_12_hour(current_time)

    with open("medicine_log.csv", "a") as log_file:
        if response == 'y':
            log_file.write(f"{formatted_date},{formatted_time},1\n")
            print("Medicine logged successfully.")
        elif response == 'n':
            log_file.write(f"{formatted_date},{formatted_time},0\n")
            print("Medicine not logged.")
        else:
            print("Invalid response. Please enter 'y' or 'n'.")

def main():
    # PART A GREETING
    # Prints the greeting message
    greeting_message = get_greeting_message()
    print(greeting_message)

    # PART B MEDICINE LOGGING
    # Logs medicine intake
    log_medicine_taken()

    # Check if it's midnight and medicine is not logged, then log as not taken
    current_time = get_current_time()
    if current_time.hour == 0 and current_time.minute == 0:
        formatted_date = format_date(current_time)
        with open("medicine_log.csv", "a") as log_file:
            log_file.write(f"{formatted_date},{current_time.strftime('%I:%M %p')},0\n")
        print("Automatic log: Medicine not taken at midnight.")

if __name__ == "__main__":
    main()
