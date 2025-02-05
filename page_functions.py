from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


def wait_until_page_load(driver, method):
    url_before_load = driver.current_url
    method()
    while driver.current_url == url_before_load:
        continue
    WebDriverWait(driver, 15).until(presence_of_element_located((By.TAG_NAME, "body")))


def get_product_list(product_name, min_price=0, max_price=0):
    driver = webdriver.Firefox()
    url = 'https://www.mercadolivre.com.br/'
    wait_until_page_load(driver, lambda: driver.get(url))

    element = driver.find_element(By.ID, "cb1-edit")
    wait_until_page_load(driver, lambda: element.send_keys(product_name, Keys.ENTER))

    if max_price != 0 != min_price:
        max_box = driver.find_element(By.CSS_SELECTOR, "[data-testid='Maximum-price']")
        min_box = driver.find_element(By.CSS_SELECTOR, "[data-testid='Minimum-price']")
        max_box.send_keys(max_price)
        wait_until_page_load(driver, lambda: min_box.send_keys(min_price, Keys.ENTER))

    product_tiles = driver.find_elements(By.XPATH, '/html/body/main/div/div[2]/section/ol/li')

    product_list = []

    for tile in product_tiles:
        name = tile.find_element(By.XPATH, ".//h2[@class='ui-search-item__title shops__item-title']").text

        price_parts = tile.find_element(
            By.XPATH,
            ".//div[@class='ui-search-price ui-search-price--size-medium shops__price']"
            "//span[@class='price-tag ui-search-price__part shops__price-part']"
            "/span[@class='price-tag-amount']").text.split("\n")
        price = float(f"{price_parts[1].replace('.', '')}.{price_parts[3] if len(price_parts) == 4 else 0}")

        link = tile.find_element(
            By.XPATH,
            ".//a[@class='ui-search-item__group__element shops__items-group-details ui-search-link']") \
            .get_attribute("href")

        product_data = {"name": name, "preco": price, "link": link}

        product_list.append(product_data)

    return product_list


# CEP
def get_cep_result():
    driver = webdriver.Firefox()
    url = 'https://www.mercadolivre.com.br/'
    wait_until_page_load(driver, lambda: driver.get(url))

    cep_box = driver.find_element(By.XPATH,
                                  ".//div[@class='nav-header-plus-cp-wrapper nav-area nav-bottom-area nav-left-area']")
    cep_box.click()

    driver.implicitly_wait(6)
    iframe = driver.find_element(By.CSS_SELECTOR,
                                 "iframe[src*='https://www.mercadolivre.com.br/navigation/addresses-hub?go=']")
    driver.implicitly_wait(4)
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(4)
    cep_input = driver.find_element(By.CSS_SELECTOR, "input[name='zipcode']")
    cep_input.clear()
    cep_input.send_keys(f'{123:0>8}', Keys.ENTER)

    return
