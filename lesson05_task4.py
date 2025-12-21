from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(
        GeckoDriverManager().install()
    )
)

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.CSS_SELECTOR, "#username")
password = driver.find_element(By.CSS_SELECTOR, "#password")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

radius = driver.find_element(By.CSS_SELECTOR, ".radius")
radius.click()

flash_text = driver.find_element(By.CSS_SELECTOR, "#flash").text
print(flash_text)

driver.quit()
