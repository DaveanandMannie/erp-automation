from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


# TODO: port to Odoo 17
class ManifestSettings(BasePage):
    def __init__(self, *args):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def navigate_settings_location(self):
        settings_tab: WebElement = self.driver.find_element(
            By.CSS_SELECTOR,
            "div.tab[data-key='mrp'] span.app_name"
        )
        settings_tab.click()
        return

    def get_manifest_fields(self) -> list:
        field_list: list = []
        list_div: WebElement = self.driver.find_element(
            By.NAME,
            'artwork_field_ids'
        )
        spans: list[WebElement] = list_div.find_elements(By.TAG_NAME, 'span')
        for span in spans:
            field_list.append(span.get_attribute('title'))
        return field_list
