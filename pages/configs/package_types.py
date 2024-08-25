from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BasePage


class PackageTypes(BasePage):
    def __init__(self, *args: str):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def _nav_product_tab(self):
        tab_elem: WebElement = self.driver.find_element(
            By.NAME,
            'product_detail'
        )
        tab_elem.click()
        sleep(0.3)

    def get_name(self) -> str | None:
        name_elem = self.driver.find_element(By.ID, 'name_0')
        name: str | None = name_elem.get_attribute('value')
        return name

    def get_dimensions(self) -> list[str | None]:
        dim_list: list[str | None] = []
        len_elem: WebElement = self.driver.find_element(
            By.ID,
            'packaging_length_0'
        )
        width_elem: WebElement = self.driver.find_element(
            By.ID,
            'width_0'
        )
        height_elem: WebElement = self.driver.find_element(
            By.ID,
            'height_0'
        )

        length: str | None = len_elem.get_attribute('value')
        width: str | None = width_elem.get_attribute('value')
        height: str | None = height_elem.get_attribute('value')
        dim_list.append(length)
        dim_list.append(width)
        dim_list.append(height)
        return dim_list

    def get_weight(self) -> str | None:
        weight_elem: WebElement = self.driver.find_element(
            By.ID,
            'base_weight_0'
        )
        weight: str | None = weight_elem.get_attribute('value')
        return weight

    def get_max_weight(self) -> str | None:
        mweight_elem: WebElement = self.driver.find_element(
            By.ID,
            'max_weight_0'
        )
        mweight: str | None = mweight_elem.get_attribute('value')
        return mweight

    def get_barcode(self) -> str | None:
        bar_elem: WebElement = self.driver.find_element(
            By.ID,
            'barcode_0'
        )
        bar: str | None = bar_elem.get_attribute('value')
        return bar

    def get_price(self) -> str | None:
        price_elem: WebElement = self.driver.find_element(
            By.ID,
            'price_0'
        )
        price: str | None = price_elem.get_attribute('value')
        return price

    def get_product(self) -> str | None:
        product_elem: WebElement = self.driver.find_element(
            By.ID,
            'product_id_0'
        )
        product: str | None = product_elem.get_attribute('value')
        return product

    def get_related_to_client(self) -> bool:
        related_elem: WebElement = self.driver.find_element(
            By.ID,
            'related_to_client_company_0'
        )
        related: bool = related_elem.is_selected()
        return related

    def opt_get_companies(self) -> list[str]:
        company_list: list[str] = []
        table_div: WebElement = self.driver.find_element(
            By.NAME,
            'client_company_ids'
        )
        table_elem: WebElement = table_div.find_element(By.TAG_NAME, 'tbody')
        rows: list[WebElement] = table_elem.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            add_line_row: list[WebElement] = row.find_elements(
                By.CLASS_NAME,
                'o_field_x2many_list_row_add'
            )

            if add_line_row:
                break

            name_elem: WebElement = row.find_element(By.TAG_NAME, 'td')
            company_list.append(name_elem.text)

        return company_list

    def get_package_rules(self) -> list[list[str]]:
        rules: list[list[str]] = []
        table_div: WebElement = self.driver.find_element(
            By.NAME,
            'stock_package_rule_ids'
        )
        table_elem: WebElement = table_div.find_element(By.TAG_NAME, 'tbody')
        rows: list[WebElement] = table_elem.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            temp_list: list[str] = []
            add_line_row: list[WebElement] = row.find_elements(
                By.CLASS_NAME,
                'o_field_x2many_list_row_add'
            )

            if add_line_row:
                break

            categ_elem: WebElement = row.find_element(
                By.NAME,
                'product_category_id'
            )
            on_elem: WebElement = row.find_element(By.NAME, 'applicable_on')
            min_elem: WebElement = row.find_element(By.NAME, 'min_value')
            max_elem: WebElement = row.find_element(By.NAME, 'max_value')

            temp_list.append(categ_elem.text)
            temp_list.append(on_elem.text)
            temp_list.append(min_elem.text)
            temp_list.append(max_elem.text)
            rules.append(temp_list)

        return rules

    def get_product_details(self) -> None:
        self._nav_product_tab()
        raise NotImplementedError

    def get_storage_cap(self) -> None:
        raise NotImplementedError
