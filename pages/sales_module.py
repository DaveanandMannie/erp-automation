from typing import cast

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BasePage

type SaleData = list[dict[str, str | list[dict[str, str]]]]
type PrintingDetails = list[dict[str, str]]


class SaleOrder(BasePage):
    """This class is used to create mock sales orders"""
    def __init__(self, *args: str):
        super().__init__(*args)
        self.driver.implicitly_wait(5)
        self.actions: ActionChains = ActionChains(self.driver)

    def _set_customer(self, customer: str):
        "Looks for test client 'Dave Test (PB)'"
        input: WebElement = self.driver.find_element(By.ID, 'partner_id_0')
        input.send_keys(customer)
        cust: WebElement = self._wait_visibility((By.LINK_TEXT, customer))
        cust.click()

    def _set_price_list(self, price_list: str, currency: str):
        "Default price list and address: Canva, Can be set to anohter"
        display: str = f'{price_list} ({currency})'
        input: WebElement = self.driver.find_element(By.ID, 'pricelist_id_0')
        input.click()
        input.clear()
        input.clear()
        input.send_keys(price_list)
        plist: WebElement = self._wait_visibility((By.LINK_TEXT, display))
        plist.click()

    def _set_invoice_address(self, client: str):
        "Default invoice address: Canva this maychange if invoice list changes"
        input: WebElement = self.driver.find_element(
            By.ID, 'partner_invoice_id_0'
        )
        input.click()
        input.clear()
        input.clear()
        input.send_keys(client)
        address: WebElement = self._wait_visibility((By.LINK_TEXT, client))
        address.click()

    def _set_service_lvl(self, level: str):
        "Sets service level, default: standard"
        input: WebElement = self.driver.find_element(
            By.ID, 'service_level_id_0'
        )
        input.clear()
        input.send_keys(level)
        lvl: WebElement = self._wait_visibility((By.LINK_TEXT, level))
        lvl.click()

    def _set_receipt(self, id: str):
        """Sets the sale order's receipt"""
        input: WebElement = self.driver.find_element(By.ID, 'receipt_id_0')
        input.send_keys(id)
        input.send_keys(Keys.RETURN)

    # ============== setting orderlines ============== #
    def _get_rows(self, key: str) -> list[WebElement]:
        table_div: WebElement = self.driver.find_element(By.NAME, key)
        table: WebElement = table_div.find_element(By.TAG_NAME, 'tbody')
        rows: list[WebElement] = table.find_elements(By.TAG_NAME, 'tr')
        return rows

    def _get_row(self, key: str, index: int = 0) -> WebElement:
        table_div: WebElement = self.driver.find_element(By.NAME, key)
        table: WebElement = table_div.find_element(By.TAG_NAME, 'tbody')
        rows: list[WebElement] = table.find_elements(By.TAG_NAME, 'tr')
        return rows[index]

    def _set_details(self, details: PrintingDetails):
        """Sets printing details for an order line"""
        def _set_field(element_name: str, value: str):
            input: WebElement = row.find_element(
                By.NAME, element_name).find_element(By.TAG_NAME, 'input')
            if element_name == 'location':
                input.click()
                input.send_keys(value)
                _ = self._wait_visibility()
                row.find_element(By.LINK_TEXT, value).click()
                _ = self._wait_invisibility()
            else:
                input.send_keys(value)

        for data in details:
            self.driver.find_element(By.LINK_TEXT, 'Add a line').click()
            row: WebElement = self._wait_visibility(
                find=(By.CLASS_NAME, 'o_selected_row'),
                wait_time=60,
                poll=0.2
            )
            _set_field('location', data['location'])
            _set_field('offset_x', data['x_offset'])
            _set_field('offset_y', data['y_offset'])
            _set_field('artwork_img', data['artwork'])
            _set_field('mockup_image_128', data['mockup'])
            _set_field('artwork_image_64', data['artwork'])
            _set_field('artwork_url', data['url'])
            _set_field('setup', data['profile'])
            _set_field('pallet', data['pallet'])

        self.driver.find_element(
            By.CSS_SELECTOR,
            '.modal.d-block.o_technical_modal:not(.o_inactive_modal)'
        ).find_element(
            By.CSS_SELECTOR,
            "button[special='save']"
        ).click()

        _ = self._wait_invisibility(
            find=(By.CLASS_NAME, 'modal'),
            wait_time=60,
            poll=0.5
        )

    def _add_products(self, products: SaleData):
        """Adds product from a list of products"""
        save_button: WebElement = self.driver.find_element(
            By.CLASS_NAME, 'o_form_button_save'
        )
        row: WebElement

        # FIXME: this is hell
        for index, data in enumerate(products):
            product: str = cast(str, data['ID'])
            row = self._get_row('order_line', index)
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

            _ = self._wait_invisibility(
                (By.CLASS_NAME, 'o_technical_modal'),
                wait_time=25,
                poll=0.5
            )

            save_button.click()

            _ = self._wait_invisibility(save_button)
            row = self._get_row('order_line', index)
            row.find_element(By.NAME, 'printing_details').click()
            _ = self._wait_invisibility()

            details = cast(PrintingDetails, data['details'])
            self._set_details(details)

    def confirm(self) -> str:
        """Clicks the save button on an edited SO and returns SO number"""
        self.driver.find_element(By.NAME, 'action_confirm').click()
        return self.get_title()

    def get_title(self) -> str:
        """Returns the SO number if the driver is on a saved SO"""
        return self.driver.find_element(By.CLASS_NAME, 'oe_title').text

    def get_manufacturing_orders(self) -> list[str]:
        "Retruns MO IDs in a SO from a SO page"
        rows: list[WebElement] = self._get_rows('order_line')
        mos: list[str] = []
        for index, row in enumerate(rows):
            add_line_row: list[WebElement] = row.find_elements(
                By.CLASS_NAME, 'o_field_x2many_list_row_add'
            )
            if add_line_row and index == 0:
                raise Exception('No Sales order lines')
            if add_line_row:
                break

            mo: str = row.find_element(By.NAME, 'manufacturing_order_id').text
            if mo:
                mos.append(mo)
        return mos

    def create_sale_order(self,
                          products: SaleData,
                          customer: str = 'Dave Test (PB)',
                          client: str = 'Canva',
                          currency: str = 'CAD',
                          service_level: str = 'standard',
                          reciept_id: str = 'Selenium Test',
                          ):

        self._set_customer(customer)
        self._set_invoice_address(client)
        self._set_price_list(client, currency)
        self._set_service_lvl(service_level)
        self._set_receipt(reciept_id)
        self._add_products(products)
