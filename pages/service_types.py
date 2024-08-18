from selenium.webdriver.remote.webelement import WebElement
from pages.base import BasePage
from selenium.webdriver.common.by import By


# TODO: Rethink all life choices until this point in time
class ServiceType(BasePage):
    def __init__(self, *args):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def get_service_struct(self) -> list[list[str]]:
        service_struct: list[list[str]] = []
        table: WebElement = self.driver.find_element(By.TAG_NAME, 'tbody')
        rows: list[WebElement] = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            temp = row.text.split('\n')
            service_struct.append(temp)
        return service_struct
