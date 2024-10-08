from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BasePage


class Routes(BasePage):
    def __init__(self, *args: str):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def get_name(self) -> str | None:
        name_elem: WebElement = self.driver.find_element(By.ID, 'name_0')
        name: str | None = name_elem.get_attribute('value')
        return name

# ============= applicable on ============== #

    def get_product_category_bool(self) -> bool:
        cat_elem: WebElement = self.driver.find_element(
            By.ID,
            'product_categ_selectable_0'
        )
        selected: bool = cat_elem.is_selected()
        return selected

    def get_products_bool(self) -> bool:
        prods_elem: WebElement = self.driver.find_element(
            By.ID,
            'product_selectable_0'
        )
        selected: bool = prods_elem.is_selected()
        return selected

    def get_warehouses_bool(self) -> bool:
        warehouse_elem: WebElement = self.driver.find_element(
            By.ID,
            'warehouse_selectable_0'
        )
        selected: bool = warehouse_elem.is_selected()
        return selected

    def opt_get_warehouse_ids(self) -> list[str]:
        ids: list[str] = []
        container_elem: WebElement = self.driver.find_element(
            By.NAME,
            'warehouse_ids'
        )
        spans: list[WebElement] = container_elem.find_elements(
            By.TAG_NAME,
            'span'
        )
        for span in spans:
            if span.text != '':
                ids.append(span.text)
        return ids

    def get_sales_lines_bool(self) -> bool:
        sales_elem: WebElement = self.driver.find_element(
            By.ID,
            'sale_selectable_0'
        )
        selected: bool = sales_elem.is_selected()
        return selected

# ============= Rules ============== #

    def get_rules(self) -> list[list[str]]:
        final_list: list[list[str]] = []
        table_div: WebElement = self.driver.find_element(
            By.NAME,
            'rule_ids'
        )
        table_elem: WebElement = table_div.find_element(By.TAG_NAME, 'tbody')
        rows: list[WebElement] = table_elem.find_elements(
            By.TAG_NAME,
            'tr'
        )

        for row in rows:
            add_line_row: list[WebElement] = row.find_elements(
                By.CLASS_NAME,
                'o_field_x2many_list_row_add'
            )

            if add_line_row:
                break

            temp_list: list[str] = []

            action_elem: WebElement = row.find_element(By.NAME, 'action')
            temp_list.append(action_elem.text)

            src_elem: WebElement = row.find_element(By.NAME, 'location_src_id')
            temp_list.append(src_elem.text)

            des_elem: WebElement = row.find_element(
                By.NAME,
                'location_dest_id'
            )
            temp_list.append(des_elem.text)
            final_list.append(temp_list)

        return final_list
