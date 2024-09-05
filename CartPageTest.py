import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

list = []
list2 =[]
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(by=By.CSS_SELECTOR,value="input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements(by=By.XPATH,value="//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements(by=By.XPATH,value="//div[@class='product-action']/button")

for button in buttons:
    list.append(button.find_element(by=By.XPATH,value="parent::div/parent::div/h4").text)
    button.click()
print(list)

driver.find_element(by=By.CSS_SELECTOR,value="img[alt='Cart']").click()
driver.find_element(by=By.XPATH,value="//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,7)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))

vegetables = driver.find_elements(by=By.CSS_SELECTOR,value="p.product-name")
for veg in vegetables:
    list2.append(veg.text)

print(list2)
assert list == list2
originalAmount = driver.find_element(by=By.CSS_SELECTOR,value=".discountAmt").text
driver.find_element(by=By.CLASS_NAME,value="promoCode").send_keys("rahulshettyacademy")
driver.find_element(by=By.CSS_SELECTOR,value=".promoBtn").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
discountAmount = driver.find_element(by=By.CSS_SELECTOR,value=".discountAmt").text

assert float(discountAmount) < int(originalAmount)

print(driver.find_element(by=By.CSS_SELECTOR,value="span.promoInfo").text)

amounts = driver.find_elements(by=By.XPATH,value="//tr/td[5]/p")
sum = 0

for amount in amounts:
    sum = sum + int(amount.text)


print(sum)

totalAmount = int(driver.find_element(by=By.CLASS_NAME,value="totAmt").text)
assert sum == totalAmount