import logging
import time

import allure
import requests
from allure_commons.types import AttachmentType

from pages.cart_page import CartPage

from selene import browser

API_URL = "https://demowebshop.tricentis.com/"


@allure.title('Проверка добавления 1 товара в корзину')
@allure.description('Добавление 1 товара через API. Проверка заполнения корзины через UI')
def test_add_laptop_to_cart(browser_setup):
    session = requests.Session()

    with allure.step('Добавляем товар через API'):
        response = session.post(API_URL + "addproducttocart/catalog/31/1/1")
        body = response.json()
        nop_customer = session.cookies.get("Nop.customer")

        allure.attach(body=str(body), name="Response", attachment_type=AttachmentType.JSON)
        allure.attach(body=str(nop_customer), name="ID пользователя из Cookie", attachment_type=AttachmentType.TEXT)

        logging.info(f"URL: {response.request.url}")
        logging.info(f"Status Code: {response.status_code}")
        logging.info(f"Response text: {response.text}")

    assert response.status_code == 200
    assert body["success"] is True

    cart = CartPage()

    with allure.step('Открываем корзину'):
        cart.open()

    with allure.step('Переносим сессию из запроса API в браузер'):
        cart.add_cookie(session)
        png = browser.driver.get_screenshot_as_png()
        allure.attach(body=png, name='Заполненная корзина', attachment_type=AttachmentType.PNG, extension='.png')

    with allure.step('Проверяем название товара'):
        cart.check_product_name("14.1-inch Laptop")

    with allure.step('Проверяем количество товара'):
        cart.check_quantity("1")

    with allure.step('Проверяем итоговую стоимость товара'):
        cart.check_product_total_price("1590.0")


@allure.title('Проверка добавления 1 товара в корзину 2 раза')
@allure.description('Добавление 1 товара 2 раза через API. Проверка заполнения корзины через UI')
def test_add_build_own_cheap_computer_to_cart(browser_setup):
    session = requests.Session()

    with allure.step('Добавляем товар через API 1 раз'):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        payload = ("product_attribute_72_5_18=52&product_attribute_72_6_19=54&"
                   "product_attribute_72_3_20=57&addtocart_72.EnteredQuantity=1")

        response = session.post(API_URL + "addproducttocart/details/72/1",
                                headers=headers,
                                data=payload)
        body = response.json()
        nop_customer = session.cookies.get("Nop.customer")

        allure.attach(body=payload, name="Payload", attachment_type=AttachmentType.TEXT)
        allure.attach(body=str(body), name="Response", attachment_type=AttachmentType.JSON)
        allure.attach(body=str(nop_customer), name="ID пользователя из Cookie", attachment_type=AttachmentType.TEXT)

        logging.info(f"URL: {response.request.url}")
        logging.info(f"Status Code: {response.status_code}")
        logging.info(f"Response text: {response.text}")

    assert response.status_code == 200
    assert body["success"] is True

    with allure.step('Добавляем товар через API 2 раз'):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        payload = ("product_attribute_72_5_18=52&product_attribute_72_6_19=54&"
                   "product_attribute_72_3_20=57&addtocart_72.EnteredQuantity=1")

        response = session.post(API_URL + "addproducttocart/details/72/1",
                                headers=headers,
                                data=payload)
        body = response.json()
        nop_customer = session.cookies.get("Nop.customer")

        allure.attach(body=payload, name="Payload", attachment_type=AttachmentType.TEXT)
        allure.attach(body=str(body), name="Response", attachment_type=AttachmentType.JSON)
        allure.attach(body=str(nop_customer), name="ID пользователя из Cookie", attachment_type=AttachmentType.TEXT)

        logging.info(f"URL: {response.request.url}")
        logging.info(f"Status Code: {response.status_code}")
        logging.info(f"Response text: {response.text}")

    assert response.status_code == 200
    assert body["success"] is True

    cart = CartPage()

    with allure.step('Открываем корзину'):
        cart.open()

    with allure.step('Переносим сессию из запроса API в браузер'):
        cart.add_cookie(session)
        png = browser.driver.get_screenshot_as_png()
        allure.attach(body=png, name='Заполненная корзина', attachment_type=AttachmentType.PNG, extension='.png')

    with allure.step('Проверяем название товара'):
        cart.check_product_name("Build your own cheap computer")

    with allure.step('Проверяем количество товара'):
        cart.check_quantity("2")

    with allure.step('Проверяем итоговую стоимость товара'):
        cart.check_product_total_price("1600.0")