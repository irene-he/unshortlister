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
driver.find_element(By.ID, "userNameInput").send_keys(text_inputs[0]) # make line 1 of text-inputs.txt is your uwaterloo email
driver.find_element(By.ID, "nextButton").click()
driver.find_element(By.ID, "passwordInput").send_keys(text_inputs[1]) # make line 2 of text-inputs.txt is your uwaterloo password
driver.find_element(By.ID, "submitButton").click()
driver.switch_to.frame(driver.find_element(By.ID, "duo_iframe"))
time.sleep(1)
# if you have multiple duo devices uncomment line 23, run the script, inspect the duo devices dropdown element,
# and find which option value you would like to use (for ex the value of: <option value="phone1">iOS</option>, is phone1)
#time.sleep(100000)
# comment out lines 25-26 if you don't have multiple duo confirmation devices
driver.find_element(By.XPATH, "//select[@name='device']").click()
driver.find_element(By.XPATH, "//option[@value='___']").click() # change ___ to your option value
driver.find_element(By.XPATH, "__").click() # copy and change ___ to pasted XPATH of duo verification method at ___ (should look similar this: //*[@id='auth_methods']/fieldset[3]/div[1]/button)
time.sleep(8) # here you are given 8s to complete your duo confirmation
driver.find_element(By.XPATH, "//a[@href='/myAccount/co-op.htm']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='quickSearchCountsContainer']/table/tbody/tr[3]/td[2]/a").click()
empty = False
while not empty:
    try: 
        driver.find_element(By.XPATH, "//a[@class='favourite action btn btn-small buttonWidth']").click()
        time.sleep(1)
    except NoSuchElementException: empty = True
driver.close()
