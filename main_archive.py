import time
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import dotenv_values


def open_browser(url: str):
    browser = webdriver.Firefox()
    try:
        browser.get(url)
        btn_guest_element = WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.ID, 'btn_guest')))
        btn_guest_element.click()
        browser.maximize_window()
        return browser
    except TimeoutException as error:
        print("ERROR >>>> TimeoutException")
        browser.close()
        print("<<<< Browser closed >>>>")
        return
    except WebDriverException as error:
        print("ERROR >>>> WebDriverException")
        browser.close()
        print("<<<< Browser closed >>>>")
        return


def close_browser(browser, close_time):
    c_time = 10
    while close_time >= 0:
        print(f"Browser is close in {close_time} seconds")
        time.sleep(c_time)
        close_time = close_time-c_time
    browser.close()


def fill_input(browser):
    try:
        input_element = WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'full-width')))
        input_element.send_keys(config["INPUT_NAME"])
        input_element.send_keys(Keys.ENTER)
        return browser
    except TimeoutException as error:
        print("ERROR >>>> TimeoutException")
        browser.close()
        print("<<<< Browser closed >>>>")
        return
    except WebDriverException as error:
        print("ERROR >>>> WebDriverException")
        browser.close()
        print("<<<< Browser closed >>>>")
        return


def capture_to_start():
    current_date = datetime.today()
    while True:
        if current_date.weekday() == int(class_day):
            current_date = datetime.today()
            if current_date.hour < class_begin.hour:
                delta = class_begin-current_date
                print(f"Time is {current_date.isoformat(timespec='auto')}")
                print(f"Sleep for {delta.seconds-60} seconds")
                time.sleep(delta.seconds-600)
            elif current_date.hour == class_begin.hour:
                if current_date.minute < (class_begin.minute-1):
                    delta = class_begin-current_date
                    print(f"Time is {current_date.isoformat(timespec='auto')}")
                    print(f"Sleep for {delta.seconds-60} seconds")
                    time.sleep(delta.seconds)
                else:
                    delta = current_date-class_begin
                    return int(config["CLASS_DURATION"])-delta.seconds
            else:
                delta = current_date-class_begin
                if delta.seconds > 3000:
                    print(f"{delta.seconds} seconds past the class ")
                    return
                else:
                    delta = current_date-class_begin
                    return int(config["CLASS_DURATION"])-delta.seconds
        else:
            print(f"Today is {current_date.strftime('%A')}")
            return
            # delta = class_begin-current_date
            # print(f"Sleep for {delta.seconds-3600} seconds") #this code sleep for along many days
            # time.sleep(delta.seconds)


if __name__ == "__main__":
    config = dotenv_values(".env")
    class_day = config["CLASS_DAY"]
    class_begin = datetime.strptime(config["CLASS_BEGIN"], '%H:%M:%S')
    delay = 10
    close_time = capture_to_start()
    if close_time:
        print("<<<< Opening Browser >>>>")
        browser = open_browser(url=str(config["URLPATH"]))
        if browser:
            browser = fill_input(browser)
        if browser:
            close_browser(browser, close_time)
