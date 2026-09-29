from study import start_pomodoro
from weather import record_weather
from diary import view_weather_diary, study_statistics, todays_summary
def main():
    while True:
        print("\n")
        print("====================================")
        print("       🌦️ STUDY WEATHER 📚")
        print("====================================")
        print("1. 🍅 Start Pomodoro Study Session")
        print("2. 🌤️ Record Today's Weather")
        print("3. 📖 View Weather Diary")
        print("4. 📊 View Study Statistics")
        print("5. 📅 View Today's Summary")
        print("6. 🚪 Exit")
        print("====================================")
        choice=input("Enter your choice: ")
        if choice=="1":
            start_pomodoro()
        elif choice=="2":
            record_weather()
        elif choice=="3":
            view_weather_diary()
        elif choice=="4":
            study_statistics()
        elif choice=="5":
            todays_summary()
        elif choice=="6":
            print("\nThanks for using Study Weather! 👋")
            break
        else:
            print("\n❌ Invalid choice. Please choose 1-6.")
if __name__=="__main__":
    main()