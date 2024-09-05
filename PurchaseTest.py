from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(by=By.CSS_SELECTOR,value="a[href*='shop']").click()
products = driver.find_elements(by=By.XPATH,value="//div[@class='card h-100']")

for product in products:
    productName = product.find_element(by=By.XPATH, value="div//h4/a").text
    if productName == "Blackberry":
        #add item into cart
        product.find_element(by=By.XPATH, value="div/button").click()


driver.find_element(by=By.CSS_SELECTOR,value="a[class*='btn-primary']").click()
driver.find_element(by=By.XPATH, value="//button[@class='btn btn-success']").click()
driver.find_element(by=By.ID,value="country").send_keys("ban")

wait = WebDriverWait(driver,7)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Bangladesh")))

driver.find_element(by=By.LINK_TEXT,value="Bangladesh").click()
driver.find_element(by=By.XPATH, value="//div[@class='checkbox checkbox-primary']").click()
driver.find_element(by=By.CSS_SELECTOR,value="[type='submit']").click()


successText = driver.find_element(by=By.CLASS_NAME, value="alert-success").text
assert "Success! Thank you!" in successText
driver.get_screenshot_as_file("screen.png")