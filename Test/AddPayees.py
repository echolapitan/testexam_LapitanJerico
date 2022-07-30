from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.demo.bnz.co.nz/client/")
# driver.maximize_window()

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.TAG_NAME, "button"))
)
element.click()

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.TAG_NAME, "a"))
)
element.click()

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Payees')]"))
)
element.click()

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Add')]"))
)
element.click()

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='ComboboxInput-apm-name']"))
)
element.send_keys("Echo Lapitan")
element.send_keys(Keys.ENTER)

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
element.click()

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//body/div[@id='YouMoney']/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[2]/button[3]"))
)
element.click()

element = WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(),'Payee added')]"))
)
print("Payee is added")

time.sleep(3)
driver.close()