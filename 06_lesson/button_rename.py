from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()
    )
)

browser.get("http://uitestingplayground.com/textinput")


our_input = browser.find_element(By.CSS_SELECTOR, ".form-control")
our_button = browser.find_element(By.CSS_SELECTOR, "#updatingButton")

our_input.send_keys("SkyPro")
our_button.click()

print(our_button.text)

browser.quit()
