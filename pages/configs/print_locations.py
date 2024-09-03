from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BasePage


class PrintLocations(BasePage):
    def __init__(self, *args: str):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def _is_checked(self, element: WebElement, check_div: str) -> str:
        """Finds a input elem inside a td given a tr and div name"""
        div: WebElement = element.find_element(By.NAME, check_div)
        is_checked: bool = div.find_element(By.TAG_NAME, 'input').is_selected()
        return str(is_checked)

    def get_locations(self) -> list[list[str]]:
        """
        Returns a list per printing location
        [
          [ID, Code, Location, ProductCategory, avail in filter, printing perm]
        ]
        """
        location_struct: list[list[str]] = []
        table: WebElement = self.driver.find_element(By.TAG_NAME, 'tbody')
        rows: list[WebElement] = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            temp = row.text.split('\n')
            avail_filter: str = self._is_checked(
                row, 'available_in_printing_filter'
            )
            print_perm: str = self._is_checked(
                row, 'artwork_printing_permission'
            )
            temp.append(avail_filter)
            temp.append(print_perm)
            location_struct.append(temp)
        return location_struct
