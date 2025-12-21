from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()
    )
)

browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/"
    "loading-images.html"
)


wait = WebDriverWait(browser, 40)

wait.until(
    EC.visibility_of_all_elements_located(
        (
           By.CSS_SELECTOR, "#image-container img:nth-of-type(4)"
        )
    )
)

images = browser.find_elements(By.CSS_SELECTOR, "#image-container img")

assert len(images) == 4, f"Должно быть 4 картинки, а найдено {len(images)}"

print(images[2].get_attribute("src"))

browser.quit()
