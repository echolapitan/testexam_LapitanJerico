from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

PATH = "C:\Program Files (x86)\drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.demo.bnz.co.nz/client/")
wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Menu')]")))
# driver.maximize_window()


menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Menu')]")))
menu.click()

payORTranfer = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Pay or transfer')]")))
payORTranfer.click()

fromAccount = wait.until(EC.element_to_be_clickable((By.XPATH, "//div//button[@data-monitoring-label='Transfer Form From Chooser']")))
fromAccount.click()

fromEveryday = wait.until(EC.element_to_be_clickable((By.XPATH, "//div//img[@alt='Everyday']")))
fromEveryday.click()

toAccount = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Choose account, payee, or someone new')]")))
toAccount.click()

accountSearch = wait.until(EC.element_to_be_clickable((By.XPATH, "//div//input[@placeholder='Search']")))
accountSearch.send_keys("Bills")

toBills = wait.until(EC.element_to_be_clickable((By.XPATH, "//div//div//img[@alt='Bills ']")))
toBills.click()

amount = wait.until(EC.presence_of_element_located((By.XPATH, "//div//span//input[@name='amount']")))
amount.send_keys("100")

transferBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div//button[@data-monitoring-label='Transfer Form Submit']")))
transferBtn.click()

successMsg = wait.until(EC.presence_of_element_located((By.XPATH, "//div//span[contains(text(),'Transfer successful')]")))
print("Transfer successful")


everydayBalanceValue = driver.find_element_by_xpath("//body/div[@id='YouMoney']/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[3]")
everydayBalanceValue = everydayBalanceValue.text
print("Everyday Balance Total:" + everydayBalanceValue)

billsBalanceValue = driver.find_element_by_xpath("//body/div[@id='YouMoney']/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/span[3]")
billsBalanceValue = billsBalanceValue.text
print("Bills Balance Total:" + billsBalanceValue)

time.sleep(3)
driver.close()