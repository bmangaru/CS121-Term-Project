from datetime import datetime
import random
import os

# Lists to store medicine log data
dates = []
times = []
statuses = []

# PART A GREETING

def get_current_time():
    return datetime.now()

def is_morning(current_time):
    return current_time.hour < 12

def format_time_12_hour(current_time):
    return current_time.strftime("%I:%M %p")

def format_date(current_time):
    return current_time.strftime("%Y-%m-%d")

def get_greeting_message():
    current_time = get_current_time()
    formatted_time = format_time_12_hour(current_time)

    if is_morning(current_time):
        return f"Good morning Brian! The current time is {formatted_time}."
    else:
        return f"Good afternoon Brian! The current time is {formatted_time}."

# PART B MEDICINE LOGGING

def log_medicine_taken():
    current_time = get_current_time()
    current_date = format_date(current_time)

    while True:
        response = input("Have you taken your medicine? (y/n): ").lower()

        if response == 'y':
            status = 1
            print("\nUsing your asthma inhaler is easy:")
            print("  - Shake it well.")
            print("  - Take off the cap and breathe out.")
            print("  - Hold the inhaler with your finger on top and your thumb underneath.")
            print("  - Put the mouthpiece in your mouth, close your lips, and breathe in slowly when you press the spray button.")
            print("  - Hold your breath for 10 seconds, then breathe out.")
            print("  - If you need a second puff, wait a bit.")
            print("  - Rinse your mouth if your doctor says so.")
            print("  - Always follow your doctor's instructions for the best results!")

            dates.append(current_date)
            times.append(current_time.strftime('%I:%M %p'))
            statuses.append(status)
            print("Medicine logged successfully.")
            break

        elif response == 'n':
            status = 0
            dates.append(current_date)
            times.append(current_time.strftime('%I:%M %p'))
            statuses.append(status)
            print("Medicine not logged.")
            break

        else:
            print("Invalid response. Please enter 'y' or 'n'.")

    save_data_to_csv()

def save_data_to_csv():
    csv_path = "Data/Magaru-Medicine-Log.csv"
    with open(csv_path, "a") as log_file:
        for i in range(len(dates)):
            log_file.write(f"{dates[i]},{times[i]},{statuses[i]}\n")

# PART C STREAK COUNTING

def count_streak():
    csv_path = "Data/Magaru-Medicine-Log.csv"
    try:
        with open(csv_path, "r") as log_file:
            lines = log_file.readlines()
    except FileNotFoundError:
        # Handle the case where the log file doesn't exist
        lines = []

    streak = 0
    for line in reversed(lines):
        parts = line.strip().split(',')
        # Check if the line has exactly three parts and the status is '1' (medicine taken)
        if len(parts) == 3 and parts[2] == '1':
            streak += 1
        else:
            # Break the loop if the streak is broken (medicine wasn't taken on a particular day)
            break

    return streak

# PART D AVERAGE CALCULATION

def calculate_average_status():
    csv_path = "Data/Magaru-Medicine-Log.csv"
    try:
        with open(csv_path, "r") as log_file:
            lines = log_file.readlines()
    except FileNotFoundError:
        return None  # Return None if the log file doesn't exist

    # Skip the first line (headers) and extract status values
    statuses_from_file = [int(line.strip().split(',')[2]) for line in lines[1:] if len(line.strip().split(',')) >= 3]

    if not statuses_from_file:
        return None  # Return None if there are no valid statuses in the file

    total_status = sum(statuses_from_file)
    total_entries = len(statuses_from_file)
    average_status = total_status / total_entries
    return average_status

def main():
    # PART A GREETING
    greeting_message = get_greeting_message()
    print(greeting_message)

    # PART B MEDICINE LOGGING
    log_medicine_taken()

    # Check if it's midnight and medicine is not logged, then log as not taken
    current_time = get_current_time()
    if current_time.hour == 0 and current_time.minute == 0:
        formatted_date = format_date(current_time)
        dates.append(formatted_date)
        times.append(current_time.strftime('%I:%M %p'))
        statuses.append(0)
        print("Automatic log: Medicine not taken at midnight.")

        # Save data to CSV file
        save_data_to_csv()

    # PART C STREAK COUNTING
    current_streak = count_streak()
    print(f"\nCurrent Streak: {current_streak} days")

    # Print a motivational message based on the streak
    if current_streak == 0:
        print("\nUh-oh! Looks like the streak is broken. Here's a motivational message to keep you going:")
        print(random.choice([
            "Don't let a missed day discourage you! Get back on track and continue your progress.",
            "Every setback is a setup for a comeback. Restart your streak and keep moving forward.",
            "It's okay to stumble, but it's the rise that matters. Restart your streak with determination.",
            "Mistakes are proof that you're trying. Keep pushing forward and don't let a missed day define you.",
            "You've come so far! One missed day won't undo your progress. Get back on track and keep going."
        ]))
    elif current_streak == 1:
        print("\nCongratulations on completing one day of your streak! Here's a motivational message to inspire you:")
        print(random.choice([
            "Fantastic job! You've completed one more day of your streak – a testament to your commitment and discipline.",
            "Day by day, you're building a chain of success. Today marks another triumph in your journey to better health!",
            "One day at a time, you're creating a positive routine. Embrace today's victory in your quest for well-being.",
            "Today's success is a building block for a healthier future. Keep up the good work on this journey of self-care.",
            "Cheers to your dedication! You've conquered another day on your path to optimal health. Keep shining!",
            "You did it again! Another day, another win. Your persistence is bringing you closer to your health goals.",
            "One more day checked off! Your commitment to your well-being is truly commendable. Keep the momentum going!",
            "Today's achievement is a step forward in your health journey. You're making progress with each passing day!",
            "Celebrate your victory today – you're making strides toward a healthier and happier you. Keep pushing forward!",
            "Kudos! One more day in the bag. Your consistency is paving the way for a brighter and healthier future."
        ]))
    elif current_streak > 1:
        print("\nCelebrating your ongoing streak! Here's a special message for you:")
        print(random.choice([
            "Celebrate each day as a victory in your health journey. You're making progress, one day at a time!",
            "Another successful day in the books! Your commitment to your well-being is truly inspiring.",
            "Cheers to consistency! Each day you stay on track is a step closer to reaching your health goals.",
            "You're on a roll! Keep the positive momentum going as you conquer another day of your streak.",
            "Day by day, you're creating a healthier and happier version of yourself. Embrace the journey!",
            "Today's achievement is a testament to your dedication. You're turning healthy choices into habits.",
            "Acknowledge the small wins! Every day of your streak is a victory in your ongoing health story.",
            "Your commitment to a healthier lifestyle shines through each successful day. Keep it up!",
            "Embrace the power of consistency. Every day counts toward a healthier and more vibrant you.",
            "You're building a foundation for lasting change. Celebrate today's win in your health journey!"
        ]))

    # PART D AVERAGE CALCULATION AND DISPLAY
    average_status = calculate_average_status()
    if average_status is not None:
        print(f"\nAverage of taking medicine: {average_status * 100:.2f}%")

if __name__ == "__main__":
    main()
