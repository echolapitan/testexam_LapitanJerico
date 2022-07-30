from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

PATH = "C:\Program Files (x86)\drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.demo.bnz.co.nz/client/")
# driver.maximize_window()
4
try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "button"))
    )
    element.click()

    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//body/div[@id='YouMoney']/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/section[1]/div[2]/nav[1]/ul[1]/li[3]/a[1]"))
    )
    element.click()

    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Payees')]"))
    )
except:
    time.sleep(4)
finally:
    print("Payees Page Has Loaded")
    driver.close()


