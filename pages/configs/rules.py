from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from pages.base import BasePage


class Rules(BasePage):
    def __init__(self, *args):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def get_name(self) -> str:
        name_elem: WebElement = self.driver.find_element(By.ID, 'name_0')
        name: str = name_elem.get_attribute('value')  # type: ignore
        return name

    def get_action(self) -> str:
        action_elem: WebElement = self.driver.find_element(
            By.ID,
            'action_0'
        )
        action_select: WebElement = Select(action_elem).first_selected_option
        action: str = action_select.text
        return action

    def get_opt_type(self) -> str:
        opt_elem: WebElement = self.driver.find_element(
            By.ID,
            'picking_type_id_0'
        )
        opt: str = opt_elem.get_attribute('value')  # type: ignore[AssignmentReport]  # noqa E501
        return opt

    def get_src_location(self) -> str:
        src_elem: WebElement = self.driver.find_element(
            By.ID,
            'location_src_id_0'
        )
        src: str = src_elem.get_attribute('value')  # type: ignore[AssignmentReport]  # noqa E501
        return src

    def get_dest_location(self) -> str:
        dest_elem: WebElement = self.driver.find_element(
            By.ID,
            'location_dest_id_0'
        )
        dest: str = dest_elem.get_attribute('value')  # type: ignore[AssignmentReport]  # noqa E501
        return dest

    def get_supply_method(self) -> str:
        supply_elem: WebElement = self.driver.find_element(
            By.ID,
            'procure_method_0'
        )
        supply_select: WebElement = Select(supply_elem).first_selected_option
        supply: str = supply_select.text
        return supply

    def get_route(self) -> str:
        route_elem: WebElement = self.driver.find_element(
            By.ID,
            'route_id_0'
        )
        route: str = route_elem.get_attribute('value')  # type: ignore[AssignmentReport]  # noqa E501
        return route

    def get_partner_address(self) -> str:
        addy_elem: WebElement = self.driver.find_element(
            By.ID,
            'partner_address_id_0'
        )
        addy: str = addy_elem.get_attribute('value')  # type: ignore[AssignmentReport]  # noqa E501
        return addy

    def get_lead_time(self) -> str:
        time_elem: WebElement = self.driver.find_element(
            By.ID,
            'delay_0'
        )
        time: str = time_elem.get_attribute('value')  # type: ignore[AssignmentReport]  # noqa E501
        return time
