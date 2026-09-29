import time
from datetime import datetime
study_sessions=[]
def start_pomodoro():
    print("\n🍅 POMODORO TIMER")
    print("--------------------")
    try:
        study_minutes=int(input("Enter study time in minutes (default 25): ") or 25)
        break_minutes=int(input("Enter break time in minutes (default 5): ") or 5)
        if study_minutes <= 0 or break_minutes<=0:
            print("Please enter numbers greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print("\nStudy session starting!")
    print("Focus on your work 📚")
    seconds = study_minutes*60
    while seconds>0:
        minutes=seconds//60
        remaining_seconds=seconds%60
        print(f"\rTime remaining: {minutes:02d}:{remaining_seconds:02d}",end="")
        time.sleep(1)
        seconds-=1
    print("\n\n🎉 Study session completed!")
    today=datetime.now().strftime("%Y-%m-%d")
    study_sessions.append({"date": today,"minutes": study_minutes})
    print(f"Study time recorded: {study_minutes} minutes.")
    choice=input("\nWould you like to start your break? (yes/no): ")
    if choice.lower()=="yes":
        print("\n☕ Break time! Relax for a while.")
        seconds=break_minutes*60
        while seconds>0:
            minutes=seconds//60
            remaining_seconds=seconds%60
            print(f"\rBreak remaining:{minutes:02d}:{remaining_seconds:02d}",end="")
            time.sleep(1)
            seconds-=1
        print("\n\nBreak finished! Ready to study again? 📚")
def get_today_study_summary():
    today=datetime.now().strftime("%Y-%m-%d")
    today_sessions=0
    today_minutes=0
    for session in study_sessions:
        if session["date"]==today:
            today_sessions+=1
            today_minutes+=session["minutes"]
    return today_sessions,today_minutes