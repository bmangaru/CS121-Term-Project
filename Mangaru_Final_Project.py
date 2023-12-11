from datetime import datetime

# PART A GREETING

# Gets the current time
def get_current_time():
    return datetime.now().time()

# Determines if the current time is morning or afternoon
def is_morning(current_time):
    return current_time < datetime.strptime("12:00", "%H:%M").time()

# Formats the current time from 24-hour format to 12-hour format
def format_time_12_hour(current_time):
    return current_time.strftime("%I:%M %p")

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
    while True:
        response = input("Have you taken your medicine? (y/n): ").lower()
        current_time = get_current_time()
        formatted_time = format_time_12_hour(current_time)

        with open("medicine_log.txt", "a") as log_file:
            if response == 'y':
                log_file.write(f"Medicine taken at {formatted_time}\n")
                print("Medicine logged successfully.")
                break  # Exit the loop if a valid response is provided
            elif response == 'n':
                log_file.write(f"Medicine not taken at {formatted_time}\n")
                print("Medicine not logged.")
                break  # Exit the loop if a valid response is provided
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
        with open("medicine_log.txt", "a") as log_file:
            log_file.write(f"Medicine not taken at midnight\n")
        print("Automatic log: Medicine not taken at midnight.")

if __name__ == "__main__":
    main()
