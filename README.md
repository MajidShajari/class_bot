## Selenium Script for Online Class Access

This script is designed to automate the process of joining an online class. It uses the Selenium library to interact with a web browser and perform the necessary actions to join the class.
Getting Started

These instructions will help you set up and run the script on your local machine.
### Usage

Run the `main.py` file in the terminal to start the script. The script will open a Firefox browser and navigate to the specified URL. It will then wait until the specified day and time to access the online class.

During this time, the script will periodically check if the time has come to access the class. Once it is time, it will automatically enter the specified name into the input field and submit it to access the class. After the specified class duration, the script will automatically close the browser.

### Prerequisites
To run this script, you will need the following software installed on your system:
- Python 3.x
- Mozilla Firefox web browser
- GeckoDriver executable file

### Installing
- Install Python 3.x from the official website.
- Download and install Mozilla Firefox web browser.
- Download GeckoDriver executable file from *[here](https://github.com/mozilla/geckodriver/releases)* and place it in a directory accessible from your system's PATH.
- Clone this repository or download the script `main.py` to your local machine.

### Configuration

Before running the script, you need to set up the necessary environment variables. Create a .env file in the same directory as the script and add the following variables:
+ URLPATH: the URL of the class login page
+ CLASS_DAY: the day of the week on which the class is scheduled (e.g. 0 for Monday, 1 for Tuesday, etc.)
+ CLASS_BEGIN: the start time of the class in HH:MM:SS format (e.g. 08:30:00 for 8:30 AM)
+ CLASS_DURATION: the duration of the class in seconds
+ INPUT_NAME: the name to be entered in the input field

Here's an example .env file:
```
URLPATH=https://www.example.com
CLASS_DAY=1
CLASS_BEGIN=08:30:00
CLASS_DURATION=3600
INPUT_NAME=John Doe
```
### License

This project is licensed under the MIT License - see the *[LICENSE](./LICENSE)* file for details.
