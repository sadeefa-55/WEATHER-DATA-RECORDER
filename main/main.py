import pandas as pd
from datetime import datetime

weather_data = []   # List to store weather entries
date_set = set()    # Set to track unique dates

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_weather_entry():
    date = input("Enter date (YYYY-MM-DD): ")
    if not is_valid_date(date):
        print("❌ Invalid date format!")
        return

    if date in date_set:
        print("⚠️ Data for this date already exists!")
        return

    try:
        temp = float(input("Enter temperature (°C): "))
    except ValueError:
        print("❌ Temperature must be a number!")
        return

    condition = input("Enter weather condition (e.g., Sunny, Rainy): ")

    entry = {
        "date": date,
        "temperature": temp,
        "condition": condition
    }
    weather_data.append(entry)
    date_set.add(date)
    print("✅ Entry added successfully!")

def view_weather_entries():
    if not weather_data:
        print("📭 No data available.")
        return

    for entry in weather_data:
        print(entry)

def summarize_data():
    if not weather_data:
        print("📭 No data to summarize.")
        return

    df = pd.DataFrame(weather_data)
    print("\n--- Summary ---")
    print("🌡️ Average Temperature:", df['temperature'].mean())
    print("🌦️ Condition Counts:")
    print(df['condition'].value_counts())

def export_to_csv():
    if not weather_data:
        print("📭 No data to export.")
        return

    df = pd.DataFrame(weather_data)
    df.to_csv("data.csv", index=False)
    print("✅ Data exported to data.csv")

def main():
    while True:
        print("\n🌾 Weather Data Recorder")
        print("1. Add Data")
        print("2. View Data")
        print("3. Show Summary")
        print("4. Export to CSV")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_weather_entry()
        elif choice == "2":
            view_weather_entries()
        elif choice == "3":
            summarize_data()
        elif choice == "4":
            export_to_csv()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# ✅ Corrected this line
if __name__ == "__main__":
    main()
