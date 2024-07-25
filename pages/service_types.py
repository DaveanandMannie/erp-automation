from selenium.webdriver.remote.webelement import WebElement
from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ServiceType(BasePage):
    def __init__(self, *args):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def get_name(self) -> str:
        name_elem: WebElement = self.driver.find_element(By.ID, 'name')
        name: str = name_elem.get_attribute('value')  # type: ignore
        return name

    def get_code(self) -> str:
        code_elem: WebElement = self.driver.find_element(By.ID, 'code')
        code: str = code_elem.get_attribute('value')  # type: ignore
        return code

    def get_look_up(self) -> str:
        look_elem: WebElement = self.driver.find_element(By.ID, 'look_up')
        look_up: str = look_elem.get_attribute('value')  # type: ignore
        return look_up

    def get_provider(self) -> str:
        provider_elem: WebElement = self.driver.find_element(By.ID, 'delivery_type')  # noqa: E501
        selected_provider: WebElement = Select(provider_elem).first_selected_option  # noqa: E501
        provider: str = selected_provider.text
        return provider
