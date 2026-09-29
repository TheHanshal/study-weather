from datetime import datetime
weather_entries=[]
def record_weather():
    print("\n🌤️ RECORD TODAY'S WEATHER")
    print("----------------------------")
    date=datetime.now().strftime("%Y-%m-%d")
    temperature=input("Enter temperature (°C): ")
    print("\nWeather conditions:")
    print("1. Sunny ☀️")
    print("2. Cloudy ☁️")
    print("3. Rainy 🌧️")
    print("4. Stormy ⛈️")
    print("5. Other")
    choice=input("Choose an option: ")
    weather_types={"1": "Sunny",
                   "2": "Cloudy",
                   "3": "Rainy",
                   "4": "Stormy",
                   "5": "Other"}
    weather=weather_types.get(choice,"Unknown")
    notes=input("Add a note about your day: ")
    entry={"date": date,
           "temperature": temperature,
           "weather": weather,
           "notes": notes}
    weather_entries.append(entry)
    print("\n✅ Weather entry saved!")
    print(f"Date: {date}")
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature}°C")
def get_today_weather():
    today=datetime.now().strftime("%Y-%m-%d")
    for entry in weather_entries:
        if entry["date"]==today:
            return entry
    return None