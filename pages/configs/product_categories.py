from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from pages.base import BasePage


class ProductCategory(BasePage):
    def __init__(self, *args):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def get_name(self) -> str | None:
        name_elem: WebElement = self.driver.find_element(By.ID, 'name_0')
        name: str | None = name_elem.get_attribute('value')
        return name

    def get_parent_category(self) -> str | None:
        category_elem: WebElement = self.driver.find_element(
            By.ID,
            'parent_id_0'
        )
        category: str | None = category_elem.get_attribute('value')
        return category

    def get_general_category(self) -> bool:
        category_elem: WebElement = self.driver.find_element(
            By.ID,
            'is_general_category_0'
        )
        category: bool = category_elem.is_selected()
        return category

    def get_require_pallet(self) -> bool:
        pallet_elem: WebElement = self.driver.find_element(
            By.ID,
            'required_pallet_type_0'
        )
        pallet: bool = pallet_elem.is_selected()
        return pallet

    def get_require_profile(self) -> bool:
        profile_elem: WebElement = self.driver.find_element(
            By.ID, 'required_print_profile_0'
        )
        profile: bool = profile_elem.is_selected()
        return profile

    def get_require_batching(self) -> bool:
        batching_elem: WebElement = self.driver.find_element(
            By.ID,
            'is_batching_required_0'
        )
        batching: bool = batching_elem.is_selected()
        return batching

    def get_require_binning(self) -> bool:
        binning_elem: WebElement = self.driver.find_element(
            By.ID,
            'is_binning_required_0'
        )
        binning: bool = binning_elem.is_selected()
        return binning

    def get_bin_by(self) -> str:
        by_el: WebElement = self.driver.find_element(By.ID, 'product_bin_by_0')
        by_option = Select(by_el).first_selected_option
        by: str = by_option.text
        return by

    # ============ Logistcs ============ #

    def get_routes(self) -> list[str]:
        routes_elem: WebElement = self.driver.find_element(
            By.NAME,
            'route_ids'
        )
        routes: list[str] = routes_elem.text.split('\n')
        return routes

    def get_total_routes(self) -> list:
        total_elem: WebElement = self.driver.find_element(
            By.NAME,
            'total_route_ids'
        )
        total_routes: list = total_elem.text.split('\n')
        return total_routes

    def get_removal_strategy(self) -> str | None:
        strat_elem: WebElement = self.driver.find_element(
            By.ID,
            'removal_strategy_id_0'
        )
        strat: str | None = strat_elem.get_attribute('value')
        return strat

    # ============ inventory valuation ============ #

    def get_costing_methods(self) -> str:
        cost_elem: WebElement = self.driver.find_element(
            By.ID,
            'property_cost_method_0'
        )
        cost_option = Select(cost_elem).first_selected_option
        cost: str = cost_option.text
        return cost

    def get_valuation(self) -> str:
        val_elem: WebElement = self.driver.find_element(
            By.ID,
            'property_valuation_0'
        )
        selected_val = Select(val_elem).first_selected_option
        val: str = selected_val.text
        return val

    # ============ printing details ============ #

    def get_print_profile(self) -> str | None:
        profile_elem: WebElement = self.driver.find_element(
            By.ID,
            'print_profile_0'
        )
        profile: str | None = profile_elem.get_attribute('value')
        return profile

    def get_pallet_type(self) -> str | None:
        pal_elem: WebElement = self.driver.find_element(By.ID, 'pallet_type_0')
        pallet: str | None = pal_elem.get_attribute('value')
        return pallet

    def get_file_name(self) -> str | None:
        # its spelt wrong on the back end so this may fail if they type check
        file_elem: WebElement = self.driver.find_element(
            By.ID,
            'artwork_naming_formate_0'
        )
        file: str | None = file_elem.get_attribute('value')
        return file
