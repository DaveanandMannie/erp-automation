from pages.base import BasePage
from selenium.webdriver.common.by import By


class ProductCategory(BasePage):
    def __init__(self, *args):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def get_name(self) -> str:
        name_elem = self.driver.find_element(By.ID, 'name')
        name: str = name_elem.get_attribute('value')  # type: ignore
        return name

    def get_parent_category(self) -> str:
        category_elem = self.driver.find_element(By.ID, 'parent_id')
        category: str = category_elem.get_attribute('value')  # type: ignore
        return category

    def get_general_category(self) -> bool:
        category_elem = self.driver.find_element(By.ID, 'is_general_category')
        category: bool = category_elem.is_selected()
        return category

    def get_require_pallet(self) -> bool:
        pallet_elem = self.driver.find_element(By.ID, 'required_pallet_type')
        pallet: bool = pallet_elem.is_selected()
        return pallet

    def get_require_profile(self) -> bool:
        profile_elem = self.driver.find_element(
            By.ID, 'required_print_profile'
        )
        profile: bool = profile_elem.is_selected()
        return profile

    def get_require_batching(self) -> bool:
        batching_elem = self.driver.find_element(By.ID, 'is_batching_required')
        batching: bool = batching_elem.is_selected()
        return batching

    def get_require_binning(self) -> bool:
        binning_elem = self.driver.find_element(By.ID, 'is_binning_required')
        binning: bool = binning_elem.is_selected()
        return binning

    def get_bin_by(self) -> str:
        by_elem = self.driver.find_element(By.ID, 'product_bin_by')
        by: str = by_elem.get_attribute('value')  # type: ignore
        return by

    # ============ Logistcs ============ #

    def get_routes(self) -> list:
        routes_elem = self.driver.find_element(By.NAME, 'route_ids')
        routes: list = routes_elem.text.split('\n')
        return routes

    def get_total_routes(self) -> list:
        total_elem = self.driver.find_element(By.NAME, 'total_route_ids')
        total_routes: list = total_elem.text.split('\n')
        return total_routes

    def get_removal_strategy(self) -> str:
        strat_elem = self.driver.find_element(By.ID, 'removal_strategy_id')
        strat: str = strat_elem.get_attribute('value')  # type: ignore
        return strat

    # ============ inventory valuation ============ #

    def get_costing_methods(self) -> str:
        cost_elem = self.driver.find_element(By.ID, 'property_cost_method')
        cost: str = cost_elem.text
        return cost

    def get_valuation(self) -> str:
        val_elem = self.driver.find_element(By.ID, 'property_valuation')
        val: str = val_elem.text
        return val

    # ============ printing details ============ #

    def get_print_profile(self) -> str:
        profile_elem = self.driver.find_element(By.ID, 'print_profile')
        profile: str = profile_elem.get_attribute('value')   # type: ignore
        return profile

    def get_pallet_type(self) -> str:
        pallet_elem = self.driver.find_element(By.ID, 'pallet_type')
        pallet: str = pallet_elem.get_attribute('value')  # type: ignore
        return pallet

    def get_file_name(self) -> str:
        # its spelt wrong on the back end so this may fail if they type check
        file_elem = self.driver.find_element(By.ID, 'artwork_naming_formate')
        file: str = file_elem.get_attribute('value')  # type: ignore
        return file
