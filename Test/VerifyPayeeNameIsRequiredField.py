from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.demo.bnz.co.nz/client/")
wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Menu')]")))
# driver.maximize_window()


menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Menu')]")))
menu.click()

payees = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Payees')]")))
payees.click()

addPayees = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Add')]")))
addPayees.click()

addPayeesAddBtn = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//body/div[@id='YouMoney']/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[2]/button[3]")))
addPayeesAddBtn.click()

addPayeesName = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='ComboboxInput-apm-name']")))
addPayeesName.click()

def find_errormessage():
    return driver.find_element_by_xpath(
        "//div//input[@aria-label='Payee Name is a required field. Please complete to continue.']")

if find_errormessage():
    print("Payee Name is Required")
else:
    print("No Errors Found")

addPayeesName = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='ComboboxInput-apm-name']")))
addPayeesName.send_keys("error validation")
addPayeesName.send_keys(Keys.ENTER)

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='apm-bank']"))
)
element.send_keys("00")

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='apm-branch']"))
)
element.send_keys("0000")

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='apm-account']"))
)
element.send_keys("0000000")

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='apm-suffix']"))
)
element.send_keys("000")

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//body/div[@id='YouMoney']/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[2]"))
)
def find_errormessageagain():
    return driver.find_element_by_xpath(
        "//body/div[@id='YouMoney']/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[2]").click()

if find_errormessageagain():
    print("Payee Name is Required")
else:
    print("No Errors Found")

time.sleep(3)
driver.close()