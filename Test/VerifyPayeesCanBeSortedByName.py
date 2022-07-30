from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

PATH = "C:\Program Files (x86)\drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.demo.bnz.co.nz/client/")
wait = WebDriverWait(driver, 10)
# driver.maximize_window()


menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Menu')]")))
menu.click()

payees = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Payees')]")))
payees.click()

def verifyPayeeName_ascendingOrder():
    return driver.find_element_by_xpath(
        "//div//h3[@aria-label='Sort by payee name A to Z selected. Select again to reverse order.']")

if verifyPayeeName_ascendingOrder():
    print("Payees Name is sort by A-Z: Ascending Order")
else:
    print("error")

payeesName = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Name')]")))
payeesName.click()

def verifyPayeeName_ascendingOrder():
    return driver.find_element_by_xpath(
        "//div//h3[@aria-label='Sort by payee name Z to A selected. Select again to reverse order.']")

if verifyPayeeName_ascendingOrder():
    print("Payees Name is sort by Z-A: Descending Order")
else:
    print("error")


time.sleep(3)
driver.close()