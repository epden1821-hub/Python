from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = ChromeService(ChromeDriverManager().install())


def test_calc():
    browser = webdriver.Chrome(service=service)
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    delay = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys("45")

    buttons = ["7", "+", "8", "="]

    for btn in buttons:
        browser.find_element(
            By.XPATH, f"//span[text()='{btn}']"
        ).click()

    wait = WebDriverWait(browser, 50)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"
        )
    )

    result = browser.find_element(By.CSS_SELECTOR, ".screen").text

    assert result == "15", (f"Ожидалось 15, а получили {result}")

    browser.quit()
