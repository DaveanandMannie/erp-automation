from base import BasePage
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ShippingMethods(BasePage):
    def __init__(self):
        super().__init__()
        WebDriverWait(self.driver, 2)


    def navigate(self, url: str):
        self.driver.get(url)
        return


    def get_shipping_provider(self):
        provider_elem = self.driver.find_element(By.ID, 'delivery_type')
        if not provider_elem:
            raise Exception('Element error: Not Found')
        provider: str = provider_elem.get_attribute('value')  # type: ignore
        print(provider)
        raise NotImplementedError

test = ShippingMethods()
test.login()
test.navigate('https://staging.odoo.printgeek.ca/web#id=4&cids=1&menu_id=356&action=609&model=delivery.carrier&view_type=form')
test.get_shipping_provider()

