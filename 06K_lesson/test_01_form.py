from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

RED = "rgba(248, 215, 218, 1)"
GREEN = "rgba(209, 231, 221, 1)"


service = EdgeService(EdgeChromiumDriverManager().install())

data_form = {
    'first-name': 'Иван',
    'last-name': 'Петров',
    'address': 'Ленина, 55-3',
    'zip-code': '',
    'city': 'Москва',
    'country': 'Россия',
    'e-mail': 'test@skypro.com',
    'phone': '+7985899998787',
    'job-position': 'QA',
    'company': 'SkyPro'
}


def test_form():
    try:
        browser = webdriver.Edge(service=service)
        browser.get(
                "https://bonigarcia.dev/selenium-webdriver-java/"
                "data-types.html"
        )

        for data, value in data_form.items():
            browser.find_element(By.NAME, data).send_keys(value)

        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait = WebDriverWait(browser, 40)
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".alert-danger, .alert-success")
            )
        )
    
        alerts = browser.find_elements(
            By.CSS_SELECTOR, ".alert-danger, .alert-success"
        )  

        for alert in alerts:
            color = alert.value_of_css_property("background-color")
        
            if alert.get_attribute("id") == "zip-code":
                assert color == RED, (
                    f"Ожидался красный, но цвет {color}"
                )
            else:
                assert color == GREEN, (
                    f"Ожидался зеленый, но цвет {color}"
                )
    finally:
        browser.quit()
