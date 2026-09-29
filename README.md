# Study Weather

## 1. Project Overview

**Study Weather** is a Python-based, menu-driven productivity application that combines study-time management with daily weather tracking.

The application allows users to start Pomodoro study sessions, record the day's weather, view a weather diary, check study statistics, and view a summary of the current day. The main menu connects these features into a single command-line application.

The project is divided into separate Python modules so that study management, weather recording, diary/statistics, and the main application flow are organized independently.



## 2. Features

### 🍅 Pomodoro Study Timer

The application provides a customizable Pomodoro-style study timer.

* Enter a study duration in minutes.
* Enter a break duration in minutes.
* Uses **25 minutes** as the default study duration.
* Uses **5 minutes** as the default break duration.
* Validates that entered durations are greater than zero.
* Handles invalid numeric input.
* Displays the remaining study and break time.
* Records completed study sessions.
* Records the total study time for the current date.

The study module stores completed sessions in memory and provides a function for calculating today's study-session count and total study time.



### 🌤️ Weather Recording

Users can record the weather for the current day.

The weather entry includes:

* Date
* Temperature in °C
* Weather condition
* A personal note about the day

Available weather conditions are:

1. Sunny
2. Cloudy
3. Rainy
4. Stormy
5. Other

The weather module stores the entries in memory and can retrieve the weather recorded for the current day.



### 📖 Weather Diary

The weather diary displays previously recorded weather entries.

For each entry, it displays:

* Date
* Weather condition
* Temperature
* Notes

If no weather entries have been recorded, the application displays an appropriate message.



### 📊 Study Statistics

The application calculates and displays study statistics, including:

* Number of completed study sessions
* Total study time in minutes
* Total study time in hours and minutes
* Average study-session length

The statistics are calculated from the study sessions recorded during the current program execution.



### 📅 Today's Summary

The daily summary combines study and weather information for the current date.

It displays:

* Today's date
* Number of study sessions today
* Total study time today
* Today's weather, if it has been recorded
* Today's temperature, if it has been recorded

If weather has not yet been recorded for the current day, the application indicates that it has not been recorded.



### 🚪 Menu-Based Navigation

The main program provides the following options:


1. 🍅 Start Pomodoro Study Session
2. 🌤️ Record Today's Weather
3. 📖 View Weather Diary
4. 📊 View Study Statistics
5. 📅 View Today's Summary
6. 🚪 Exit


The program continues displaying the menu until the user selects the Exit option.



## 3. Technologies and Tools Used

### Programming Language

* **Python 3**

### Python Modules

The project uses Python's built-in modules:

* 'datetime' — used to obtain and format the current date.
* 'time' — used to create the countdown timer for study and break periods.

### Data Structures

* **Lists** are used to store weather entries and study sessions.
* **Dictionaries** are used to represent individual weather entries and study-session records.

### Interface

* **Command-Line Interface (CLI)**
* User input is collected using Python's 'input()' function.
* Output is displayed using 'print()'.

### Project Modules


main.py
study.py
weather.py
diary.py




## 4. Project Structure


study-weather/program modules

#### main.py       # Main menu and application flow
#### study.py      # Pomodoro timer and study-session tracking
#### weather.py    # Weather recording and today's weather retrieval
#### diary.py      # Weather diary, study statistics, and daily summary
#### README.md     # Project documentation


### Module Responsibilities

#### 'main.py'
Acts as the entry point of the application. It imports the required functions from the other modules and provides the main menu.

#### 'study.py'
Contains the Pomodoro timer functionality and study-session tracking.

#### 'weather.py'
Handles recording weather information and retrieving today's weather.

#### 'diary.py'
Provides the weather diary, study statistics, and today's combined summary.


## 5. Installation and Setup

### Prerequisites

Make sure **Python 3** is installed on your computer.

You can check the Python installation by running:
python --version

or, depending on your system:
python3 --version


### Step 1: Download or Copy the Project

Place all four Python files in the same folder:

main.py
study.py
weather.py
diary.py


The files should remain in the same directory because the modules import functions and data from one another.

### Step 2: Open a Terminal

Navigate to the folder containing the project files.

For example:
cd path/to/study-weather/program modules


### Step 3: Run the Application

Run: python main.py
If your system uses 'python3', run: python3 main.py
The Study Weather main menu should then appear in the terminal.



## 6. How to Use the Application

### Option 1 — Start Pomodoro Study Session

Select: 1
Enter the desired study duration and break duration.

For example:
Enter study time in minutes (default 25): 1
Enter break time in minutes (default 5): 1

The application starts the study countdown. After the study session finishes, the completed session is recorded.
You can then choose whether to start the break.

> \*\*Testing tip:\*\* Use '1' minute for both study and break durations when testing so that you do not have to wait for the default 25-minute session.


### Option 2 — Record Today's Weather

Select: 2
Enter the temperature and choose a weather condition.

For example:
Enter temperature (°C): 28

Weather conditions:
1. Sunny ☀️
2. Cloudy ☁️
3. Rainy 🌧️
4. Stormy ⛈️
5. Other

Choose an option: 1
Add a note about your day: Warm and sunny

The application saves the weather entry in memory.



### Option 3 — View Weather Diary

Select: 3
The application displays all weather entries recorded during the current program execution.

If no entries have been recorded, it displays:
No weather entries yet.


### Option 4 — View Study Statistics

Select: 4
The application displays the number of completed sessions, total study time, and average session length.

For example:
Study sessions completed: 2
Total study time: 50 minutes
That's 0 hour(s) and 50 minute(s).
Average session length: 25.0 minutes


### Option 5 — View Today's Summary

Select: 5
The application combines the study and weather information recorded for the current date.

This is useful for quickly reviewing the day's study activity and weather information.


### Option 6 — Exit

Select: 6
The application exits and displays a goodbye message.


## 7. Testing Instructions

Testing can be performed directly through the command-line interface.

### Test 1: Launch the Application

Run: python main.py

**Expected result:**  
The Study Weather menu is displayed with options 1 through 6.


### Test 2: Test the Pomodoro Timer

1. Select option '1'.
2. Enter '1' for the study duration.
3. Enter '1' for the break duration.
4. Wait for the study countdown to finish.
5. Choose 'yes' when asked whether to start the break.

**Expected result:**
* The study countdown runs.
* The completed study session is recorded.
* The break countdown runs.
* The session information becomes available to the statistics and daily-summary features.


### Test 3: Test Invalid Study Input

Select option '1' and enter a non-numeric value, such as: abc
**Expected result:**
Please enter a valid number.

You can also enter '0' or a negative number.
**Expected result:**
Please enter numbers greater than 0.


### Test 4: Test Weather Recording

1. Select option '2'.
2. Enter a temperature.
3. Select a weather condition.
4. Enter a note.

**Expected result:**
The application confirms that the weather entry was saved and displays the recorded date, weather, and temperature.


### Test 5: Test Weather Diary

1. Record at least one weather entry using option '2'.
2. Select option '3'.

**Expected result:**  
The recorded weather entry is displayed with its date, weather condition, temperature, and notes.


### Test 6: Test Study Statistics

1. Complete one or more short study sessions.
2. Select option '4'.

**Expected result:**  
The application displays:

* Number of completed study sessions
* Total study time
* Total time in hours/minutes
* Average session length


### Test 7: Test Today's Summary

1. Record today's weather.
2. Complete at least one study session.
3. Select option '5'.

**Expected result:**  
The application displays the current date together with today's study and weather information.


### Test 8: Test Invalid Menu Choice

Enter a value outside the available menu options, such as: 9

**Expected result:**
❌ Invalid choice. Please choose 1-6.


### Test 9: Test Exit

Select option: 6

**Expected result:**  
The application exits and displays:

Thanks for using Study Weather! 👋


## 8. Screenshots

### Main Menu

![This is the main menu of the program](https://github.com/TheHanshal/study-weather/blob/ac0534906621138fa75fdce694753745793764b5/Main%20Menu%20Screenshot.png)


## 9. Data Storage

The project currently stores study sessions and weather entries **in memory using Python lists**.
This means that the recorded data is available while the application is running, but it is not permanently saved to a file or database.

For example:
* Weather information is stored in 'weather\_entries'.
* Study information is stored in 'study\_sessions'.

If the program is closed, the in-memory data is lost.



## 10. Conclusion

**Study Weather** is a simple command-line Python application that combines productivity tracking and daily weather journaling.

It demonstrates the use of:

* Python functions
* Modules and imports
* Lists and dictionaries
* Loops and conditional statements
* User input and validation
* Date and time handling
* Countdown timers
* Basic data analysis and summaries

The modular structure makes the project easy to understand and provides a foundation for adding future features such as permanent data storage, graphical interfaces, or additional productivity tracking.
