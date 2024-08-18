from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ManifestSettings(BasePage):
    def __init__(self, *args):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def navigate_settings_location(self):
        settings_tab: WebElement = self.driver.find_element(
            By.CSS_SELECTOR,
            '[data-key="mrp"]'
        )
        settings_tab.click()
        return

    def get_manifest_fields(self) -> list[str]:
        list_div: WebElement = self.driver.find_element(
            By.NAME,
            'artwork_field_ids'
        )
        field_list: list[str] = list_div.text.split('\n')
        return field_list
