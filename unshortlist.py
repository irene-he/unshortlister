from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()

with open("text-inputs.txt") as f:
    text_inputs = f.read().splitlines() 

driver.get("https://waterlooworks.uwaterloo.ca/")
driver.find_element(By.XPATH, "//a[@href='https://waterlooworks.uwaterloo.ca/waterloo.htm?action=login']").click()
time.sleep(1)
driver.find_element(By.ID, "userNameInput").send_keys(text_inputs[0])
driver.find_element(By.ID, "nextButton").click()
driver.find_element(By.ID, "passwordInput").send_keys(text_inputs[1])
driver.find_element(By.ID, "submitButton").click()
driver.switch_to.frame(driver.find_element(By.ID, "duo_iframe"))
time.sleep(1)
driver.find_element(By.XPATH, "//select[@name='device']").click()
driver.find_element(By.XPATH, "//option[@value='phone3']").click()
driver.find_element(By.XPATH, "//*[@id='auth_methods']/fieldset[3]/div[1]/button").click()
time.sleep(8)
driver.find_element(By.XPATH, "//a[@href='/myAccount/co-op.htm']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='quickSearchCountsContainer']/table/tbody/tr[3]/td[2]/a").click()
empty = False
while not empty:
    try: 
        driver.find_element(By.XPATH, "//a[@class='favourite action btn btn-small buttonWidth']").click()
        time.sleep(1)
    except NoSuchElementException: empty = True