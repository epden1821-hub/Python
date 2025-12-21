from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()
    )
)


browser.implicitly_wait(20)

browser.get("http://uitestingplayground.com/ajax")

browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

result = browser.find_element(By.CSS_SELECTOR, ".bg-success").text

print(result)

browser.quit()
