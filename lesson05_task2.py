from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()
    )
)

driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")

button_blue = driver.find_element(By.CLASS_NAME, "btn-primary")
button_blue.click()
