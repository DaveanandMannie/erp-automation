# TODO: INSTEAD OF RELYING ON AUTO COMPLUTE USE THE LINK TEXT

# pyright: reportUnknownMemberType=false
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class SaleOrder(BasePage):
    """This class is used to create mock sales orders"""
    def __init__(self, *args: str):
        super().__init__(*args)
        self.driver.implicitly_wait(5)
        self.actions: ActionChains = ActionChains(self.driver)

    def _wait_invisibility(
            self,
            find_args: tuple[str, str] | WebElement = (By.CLASS_NAME, 'o-autocomplete--dropdown-menu')):  # noqa: E501
        """
        A wrapper func for wait -> invisibility of element located
        Default: (By.CLASS_NAME, 'o-autocomplete--dropdown-menu')
        """
        elem: WebElement | bool = WebDriverWait(self.driver, 3, 0.3).until(
            EC.invisibility_of_element_located(find_args)
        )
        return elem

    def _wait_visibility(
        self,
        find_args: tuple[str, str] = (By.CLASS_NAME, 'o-autocomplete--dropdown-menu')  # noqa: E501
    ):
        """
        A wrapper func for wait -> visibility of element located
        Default: (By.CLASS_NAME, 'o-autocomplete--dropdown-menu')
        """
        elem: WebElement = WebDriverWait(self.driver, 3, 1).until(
            EC.visibility_of_element_located(find_args)
        )
        sleep(0.8)
        return elem

    def _set_customer(self, customer: str):
        "Looks for test client 'Dave Test (Pb)"
        input: WebElement = self.driver.find_element(By.ID, 'partner_id_0')
        input.send_keys(customer)
        _ = self._wait_visibility()
        # input.send_keys(Keys.ARROW_DOWN)
        input.send_keys(Keys.RETURN)

    # TODO: this is problematic
    def _set_price_list(self, price_list: str):
        "Default price list and address: Canva, Can be set to anohter"
        input: WebElement = self.driver.find_element(By.ID, 'pricelist_id_0')
        input.click()
        input.clear()
        input.send_keys(price_list)
        _ = self._wait_visibility()
        input.send_keys(Keys.RETURN)

    def _set_invoice_address(self, client: str):
        "Default invoice address: Canva this maychange if invoice list changes"
        sleep(1)
        input: WebElement = self.driver.find_element(
            By.ID, 'partner_invoice_id_0'
        )
        input.click()
        input.clear()
        input.send_keys(client)
        _ = self._wait_visibility()
        input.send_keys(Keys.ARROW_DOWN)
        sleep(1.5)
        input.send_keys(Keys.RETURN)

    def _set_service_lvl(self, level: str):
        "Sets service level, default: standard"
        input: WebElement = self.driver.find_element(
            By.ID, 'service_level_id_0'
        )
        input.clear()
        input.send_keys(level)
        _ = self._wait_visibility()
        input.send_keys(Keys.RETURN)

    def _set_receipt(self, id: str):
        """Sets the sale order's receipt"""
        input: WebElement = self.driver.find_element(By.ID, 'receipt_id_0')
        input.send_keys(id)
        input.send_keys(Keys.RETURN)

    # ============== setting orderlines ============== #

    def _set_details(self):
        """Sets printing details for an order line"""
        def _get_row(index: int = 0) -> WebElement:
            table_div: WebElement = self.driver.find_element(
                By.NAME, 'printing_details_ids'
            )
            table: WebElement = table_div.find_element(By.TAG_NAME, 'tbody')
            rows: list[WebElement] = table.find_elements(By.TAG_NAME, 'tr')
            return rows[index]

        self.driver.find_element(By.LINK_TEXT, 'Add a line').click()
        row: WebElement = _get_row()

        row.find_element(By.NAME, 'location').find_element(
            By.TAG_NAME, 'input').send_keys('FR')

        # row.find_element(By.NAME, 'offset_x').find_elem

    def _add_products(self, products: list[str]):
        """Adds product from a list of products"""
        # save_button: WebElement = self.driver.find_element(
        #     By.CLASS_NAME, 'o_form_button_save'
        # )
        def _get_row(index: int) -> WebElement:
            table_div: WebElement = self.driver.find_element(
                By.NAME, 'order_line'
            )
            table: WebElement = table_div.find_element(By.TAG_NAME, 'tbody')
            rows: list[WebElement] = table.find_elements(By.TAG_NAME, 'tr')
            return rows[index]

        # TODO: this is hell
        for index, product in enumerate(products):
            row: WebElement = _get_row(index)
            row.find_element(By.LINK_TEXT, 'Add a product').click()

            product_div: WebElement = self._wait_visibility(
                (By.CLASS_NAME, 'o_selected_row')
            )
            product_div.find_element(By.TAG_NAME, 'input').click()
            _ = self._wait_visibility()
            self.driver.find_element(By.LINK_TEXT, 'Search More...').click()

        # ========= Modal interaction ========= #
            _ = self._wait_visibility((By.CLASS_NAME, 'modal-dialog'))

            self.driver.find_element(
                By.CLASS_NAME, 'o_searchview_dropdown_toggler'
            ).click()

            self.driver.find_element(
                By.CLASS_NAME, 'o_add_custom_filter'
            ).click()

            rule: str = self.driver.find_element(
                By.CLASS_NAME, 'o_model_field_selector_chain_part'
            ).text

            if rule != 'ID':
                raise Exception('Filter rule is not "ID"')
            rules_row: WebElement = self.driver.find_element(
                By.CLASS_NAME, 'o_tree_editor_condition'
            )

            sleep(1)

            input: WebElement = rules_row.find_element(By.TAG_NAME, 'input')
            input.click()
            input.send_keys(Keys.BACKSPACE)
            input.send_keys(product)

            modal_2: WebElement = self.driver.find_element(
                By.CSS_SELECTOR,
                '.modal.d-block.o_technical_modal:not(.o_inactive_modal)'
            )
            modal_2.find_element(By.CLASS_NAME, 'btn-primary').click()
            _ = self._wait_invisibility(modal_2)

            self.driver.find_element(
                By.CLASS_NAME, 'o_technical_modal'
            ).find_element(By.CLASS_NAME, 'o_row_draggable').click()

            _ = self._wait_invisibility((By.CLASS_NAME, 'o_technical_modal'))
            # save_button.click()
            # WebDriverWait(self.driver, 3).until(
            #     EC.invisibility_of_element_located(save_button)
            # )
            #
            # row: WebElement = _get_row(index)
            # row.find_element(By.NAME, 'printing_details').click()
            # self._set_details()

    def create_sale_order(
        self,
        products: list[str],
        customer: str = 'Dave Test (PB)',
        client: str = 'Canva',
        service_level: str = 'standard',
        reciept_id: str = 'Selenium Test',
    ):
        self._set_customer(customer)
        self._set_invoice_address(client)
        # self._set_price_list(client)
        self._set_service_lvl(service_level)
        self._set_receipt(reciept_id)
        self._add_products(products)
