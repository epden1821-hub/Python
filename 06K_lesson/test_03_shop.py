from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

service = FirefoxService(GeckoDriverManager().install())


def test_shop():
    browser = webdriver.Firefox(service=service)
    browser.get(
        "https://www.saucedemo.com/"
    )

    user = browser.find_element(By.CSS_SELECTOR, "#user-name")
    password = browser.find_element(By.CSS_SELECTOR, "#password")
    login_btn = browser.find_element(By.CSS_SELECTOR, "#login-button")

    user.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()

    produts_id = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    for product in produts_id:
        browser.find_element(By.CSS_SELECTOR, "#" + product).click()

    browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    browser.find_element(By.CSS_SELECTOR, "#checkout").click()

    data_form = {
        'first-name': 'Денис',
        'last-name': 'Епифанов',
        'postal-code': '350047'
    }

    for data, value in data_form.items():
        item = browser.find_element(By.CSS_SELECTOR, "#" + data)
        item.send_keys(value)

    browser.find_element(By.CSS_SELECTOR, "#continue").click()

    total = browser.find_element(
        By.CSS_SELECTOR, ".summary_total_label"
    ).text

    browser.quit()

    assert total == "Total: $58.29", (
        f"Ожидалось $58.29, а получили {total}"
    )
