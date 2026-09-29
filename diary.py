from datetime import datetime
from study import study_sessions
from weather import weather_entries
def view_weather_diary():
    print("\n🌤️ WEATHER DIARY")
    print("====================")
    if len(weather_entries)==0:
        print("No weather entries yet.")
        return
    for entry in weather_entries:
        print(f"\nDate: {entry['date']}")
        print(f"Weather: {entry['weather']}")
        print(f"Temperature: {entry['temperature']}°C")
        print(f"Notes: {entry['notes']}")
def study_statistics():
    print("\n📊 STUDY STATISTICS")
    print("======================")
    if len(study_sessions)==0:
        print("No study sessions completed yet.")
        return
    total_minutes=0
    for session in study_sessions:
        total_minutes+=session["minutes"]
    number_of_sessions=len(study_sessions)
    print(f"Study sessions completed: {number_of_sessions}")
    print(f"Total study time: {total_minutes} minutes")
    hours=total_minutes//60
    minutes=total_minutes%60
    print(f"That's {hours} hour(s) and {minutes} minute(s).")
    average=total_minutes/number_of_sessions
    print(f"Average session length: {average:.1f} minutes")
def todays_summary():
    print("\n📚 TODAY'S SUMMARY")
    print("======================")
    today=datetime.now().strftime("%Y-%m-%d")
    today_sessions=0
    today_minutes=0
    for session in study_sessions:
        if session["date"]==today:
            today_sessions+=1
            today_minutes+=session["minutes"]
    print(f"Date: {today}")
    print(f"Study sessions today: {today_sessions}")
    print(f"Study time today: {today_minutes} minutes")
    found_weather=False
    for entry in weather_entries:
        if entry["date"]==today:
            print(f"Today's weather: {entry['weather']}")
            print(f"Temperature: {entry['temperature']}°C")
            found_weather=True
            break
    if not found_weather:
        print("Today's weather has not been recorded yet.")