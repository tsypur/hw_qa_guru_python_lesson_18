from selene import browser, have


class CartPage():

    def open(self):
        browser.open('/cart')

    def add_cookie(self, session):
        for cookie in session.cookies:
            browser.driver.add_cookie({
                'name': cookie.name,
                'value': cookie.value,
                'path': '/'
            })
        browser.driver.refresh()

    def check_product_name(self, product_name):
        browser.element('.product-name').should(have.text(product_name))


    def check_quantity(self, quantity):
        browser.element('.qty-input').should(have.value(quantity))

    def check_product_total_price(self, total_price):
        browser.element('.product-subtotal').should(have.text(total_price))