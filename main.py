from datetime import datetime, timedelta
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import dotenv_values


def handle_error(error, browser):
    print(f"ERROR >>>> {error.__class__.__name__}")
    if browser:
        browser.close()
        print("<<<< Browser closed >>>>")
        exit()


def open_browser(url: str):
    browser = webdriver.Firefox()
    try:
        print("<<<< Opening Browser >>>>")
        browser.get(url)
        btn_guest_element = WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.ID, 'btn_guest')))
        btn_guest_element.click()
        browser.maximize_window()
        return browser
    except (TimeoutException, WebDriverException) as error:
        handle_error(error, browser)
        return None


def close_browser(browser, close_delay):
    print(f"Browser is close in {close_delay} seconds")
    WebDriverWait(browser, close_delay).until(lambda _: False)
    browser.close()


def fill_input(browser):
    try:
        input_element = WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'full-width')))
        input_element.send_keys(config["INPUT_NAME"])
        input_element.send_keys(Keys.ENTER)
        return True
    except (TimeoutException, WebDriverException) as error:
        handle_error(error, browser)
        return False


def delay_to_close(browser):
    while True:
        current_date_time = datetime.today()
        if current_date_time < (class_date_time-timedelta(minutes=1)):
            delta = class_date_time-current_date_time-timedelta(minutes=1)
            print(
                f"Time is {current_date_time.strftime('%H:%M:%S')}")
            print(f"Sleep for {delta.seconds} seconds")
            WebDriverWait(browser, delta.seconds).until(lambda _: False)
        else:
            delta = current_date_time-class_date_time
            print(
                f"Time is {current_date_time.strftime('%H:%M:%S')}")
            if delta.days == -1:
                return int(config["CLASS_DURATION"])
            return int(config["CLASS_DURATION"])-delta.seconds


if __name__ == "__main__":
    config = dotenv_values(".env")
    class_day = config["CLASS_DAY"]
    current_day = datetime.today()
    current_weekday = current_day.weekday()
    class_begin_time = datetime.strptime(
        config["CLASS_BEGIN"], '%H:%M:%S').time()
    class_date_time = datetime.combine(current_day.date(), class_begin_time)
    delay = 10
    if current_weekday == int(class_day):
        browser = open_browser(url=str(config["URLPATH"]))
    else:
        print(f"Today is {current_weekday}")
        sys.exit()
    close_delay = delay_to_close(browser)
    if close_delay < 2700:
        print(
            f"""{int(config["CLASS_DURATION"])-close_delay} seconds past the class""")
        browser.close()
        exit()
    browser = fill_input(browser)
    close_browser(browser, close_delay)
