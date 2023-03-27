from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from utils import login, password, url, wait_time_for_the_meeting, meeting_time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def dont_remember_me():
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input"))).click()

def enter_credentials(login_field, passwd_field=None):
    login_field.send_keys(login)
    if passwd_field:
        passwd_field.send_keys(password)
        passwd_field.send_keys(Keys.RETURN)
        return
    login_field.send_keys(Keys.RETURN)

def enter_meeting():
    WebDriverWait(driver, wait_time_for_the_meeting).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/middle-messages-stripe/div/messages-header/div[2]/div/message-pane/div/div[1]/div/div/calling-persistent-indicator/div/div/div/ul/li/calling-persistent-indicator-item/div/div/calling-join-button/button"))).click()
    time.sleep(15)
    element = driver.switch_to.active_element
    element.send_keys(Keys.TAB)
    element.send_keys(Keys.TAB)
    element.send_keys(Keys.TAB)
    element.send_keys(Keys.TAB)
    element.send_keys(Keys.RETURN)


def log_in():
    driver.get(url)
    login_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]")))
    enter_credentials(login_field)

    login_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/form/div[1]/div[1]/input")))
    passwd_field = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/form/div[1]/div[2]/input")
    enter_credentials(login_field, passwd_field)
    dont_remember_me()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    log_in()
    enter_meeting()
    time.sleep(meeting_time)
    driver.close()
