from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from pages.configs.base import BasePage


class ShippingMethods(BasePage):
    def __init__(self, *args):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def navigate_tab_destination(self):
        tab_elem = self.driver.find_element(
            By.LINK_TEXT, 'Destination Availability'
        )
        tab_elem.click()
        return

    def navigate_tab_extra(self):
        tab_elem = self.driver.find_element(By.LINK_TEXT, 'Extra')
        tab_elem.click()
        return

    def navigate_tab_credentials(self):
        tab_elem = self.driver.find_element(
            By.LINK_TEXT, 'Canada Post Credentials'
        )
        tab_elem.click()
        return

    def navigate_tab_product_attrib(self):
        tab_elem = self.driver.find_element(
            By.LINK_TEXT, 'Product Attribute Configuration'
        )
        tab_elem.click()

# =============== Regular page =============== #

    def get_name(self) -> str:
        name_elem: WebElement = self.driver.find_element(By.ID, 'name_0')
        name: str = name_elem.get_attribute('value')  # type: ignore
        return name

    def get_shipping_provider(self) -> str:
        provider_elem: WebElement = self.driver.find_element(
            By.ID,
            'delivery_type_0'
        )
        provider: str = Select(provider_elem).first_selected_option.text
        return provider

    def get_integration(self) -> str | None:
        integ_div: WebElement = self.driver.find_element(
            By.NAME,
            'integration_level'
        )
        radios: list[WebElement] = integ_div.find_elements(
            By.CLASS_NAME,
            'form-check'
        )
        for radio in radios:
            on: bool = radio.find_element(
                By.TAG_NAME,
                'input'
            ).is_selected()
            if on:
                name = radio.find_element(By.TAG_NAME, 'label').text
                return name

    def get_routes(self) -> str | None:
        route_elem: WebElement = self.driver.find_element(By.ID, 'route_ids_0')
        route: str | None = route_elem.get_attribute('value')
        return route

    def get_margin(self) -> str | None:
        margin_elem: WebElement = self.driver.find_element(By.NAME, 'margin')
        margin: str | None = margin_elem.find_element(
            By.CLASS_NAME,
            'o_input'
        ).get_attribute('value')
        return margin

    def get_add_margin(self) -> str | None:
        add_elem: WebElement = self.driver.find_element(
            By.ID,
            'fixed_margin_0'
        )
        return add_elem.get_attribute('value')

    def get_free_order(self) -> bool:
        on: bool = self.driver.find_element(By.ID, 'free_over_0').is_selected()
        return on

    def get_product_category(self) -> str | None:
        prod_cat: WebElement = self.driver.find_element(
            By.ID,
            'product_category_id_0'
        )
        cat: str | None = prod_cat.get_attribute('value')
        return cat

    def get_delivery_product(self) -> str | None:
        delivery_product: WebElement = self.driver.find_element(
            By.ID,
            'product_id_0'
        )
        dt_name: str | None = delivery_product.get_attribute('value')
        return dt_name

    def get_invoice_policy(self) -> str | None:
        integ_div: WebElement = self.driver.find_element(
            By.NAME,
            'invoice_policy'
        )
        radios: list[WebElement] = integ_div.find_elements(
            By.CLASS_NAME,
            'form-check'
        )
        for radio in radios:
            on: bool = radio.find_element(
                By.TAG_NAME,
                'input'
            ).is_selected()
            if on:
                name = radio.find_element(By.TAG_NAME, 'label').text
                return name

    def get_related_company(self) -> bool:
        related_elem: WebElement = self.driver.find_element(
            By.ID,
            'related_to_client_company_0'
        )
        is_on: bool = related_elem.is_selected()
        return is_on

    def opt_company_names(self) -> list[str]:
        company_names: list[str] = []
        table_div: WebElement = self.driver.find_element(By.NAME, 'client_company_id')  # noqa: E501
        table_elem: WebElement = table_div.find_element(By.TAG_NAME, 'tbody')
        rows: list[WebElement] = table_elem.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            add_line_row: list[WebElement] = row.find_elements(
                By.CLASS_NAME,
                'o_field_x2many_list_row_add'
            )
            if add_line_row:
                break

            name: str = row.find_element(By.NAME, 'display_name').text
            company_names.append(name)
        #   company_names.sort()
        return company_names

# =============== Destination Availability=============== #
    # TODO: I feel like this will run faster the element list check
    # other page classes and perf test
    def get_countries(self) -> list[str]:
        country_badges: WebElement = self.driver.find_element(
            By.NAME,
            'country_ids'
        )
        country_list: list[str] = country_badges.text.split('\n')
        return country_list

    def get_states(self) -> list[str]:
        state_badges: WebElement = self.driver.find_element(
            By.NAME,
            'state_ids'
        )
        state_list: list[str] = state_badges.text.split('\n')
        return state_list

    def get_zip_prefix(self) -> list:
        zip_badges: WebElement = self.driver.find_element(
            By.NAME,
            'zip_prefix_ids'
        )
        prefix_list: list = zip_badges.text.split('\n')
        return prefix_list

# =============== Credential =============== #
    def get_dev_username(self) -> str | None:
        user_elem: WebElement = self.driver.find_element(
            By.ID,
            'canpost_test_username_0'
        )
        user: str | None = user_elem.get_attribute('value')
        return user

    def get_dev_password(self) -> str | None:
        password_elem: WebElement = self.driver.find_element(
            By.ID,
            'canpost_test_password_0'
        )
        password: str | None = password_elem.get_attribute('value')
        return password

    def get_prod_username(self) -> str | None:
        user_elem: WebElement = self.driver.find_element(
            By.ID,
            'canpost_production_username_0'
        )
        user: str | None = user_elem.get_attribute('value')
        return user

    def get_prod_password(self) -> str | None:
        password_elem: WebElement = self.driver.find_element(
            By.ID,
            'canpost_production_password_0'
        )
        password: str | None = password_elem.get_attribute('value')
        return password

# =============== Extra tab =============== #

    def get_default_weight(self) -> str | None:
        def_weight_elem: WebElement = self.driver.find_element(
            By.ID,
            'default_product_weight_0'
        )
        def_weight: str | None = def_weight_elem.get_attribute('value')
        return def_weight

    def get_shipping_uom(self) -> str | None:
        uom_elem: WebElement = self.driver.find_element(By.ID, 'uom_id_0')
        ship_uom: str | None = uom_elem.get_attribute('value')
        return ship_uom

    def get_packaging(self) -> str | None:
        package_elem: WebElement = self.driver.find_element(
            By.ID,
            'packaging_id_0'
        )
        package: str | None = package_elem.get_attribute('value')
        return package

    def get_void_ship(self) -> bool:
        void_elem: WebElement = self.driver.find_element(
            By.ID,
            'void_shipment_0'
        )
        void: bool = void_elem.is_selected()
        return void

    def get_service_type(self) -> str | None:
        service_elem: WebElement = self.driver.find_element(
            By.ID,
            'canpost_service_type_1'
        )
        service: str | None = service_elem.get_attribute('value')
        return service

    def get_service_option(self) -> str | None:
        option_elem = self.driver.find_element(By.ID, 'canpost_option_type_0')
        option: str | None = option_elem.get_attribute('value')
        return option

    def get_customer_type(self) -> str:
        cust_type_elem: WebElement = self.driver.find_element(
            By.ID,
            'canpost_quote_type_0'
        )
        customer_type: str = Select(cust_type_elem).first_selected_option.text
        return customer_type

    def get_customer_number(self) -> str | None:
        cust_num_elem: WebElement = self.driver.find_element(
            By.ID, 'canpost_customer_number_0'
        )
        customer_number: str | None = cust_num_elem.get_attribute('value')
        return customer_number

    def get_contract_id(self) -> str | None:
        contract_elem: WebElement = self.driver.find_element(
            By.ID,
            'canpost_contract_id_0'
        )
        contract: str | None = contract_elem.get_attribute('value')
        return contract

    def get_promo_code(self) -> str | None:
        promo_elem: WebElement = self.driver.find_element(
            By.ID,
            'canpost_promo_code_0'
        )
        promo: str | None = promo_elem.get_attribute('value')
        return promo

    def get_payment_method(self) -> str | None:
        pay_meth_elem: WebElement = self.driver.find_element(
            By.ID, 'canpost_method_of_payment_0'
        )
        payment_method: str | None = pay_meth_elem.get_attribute('value')
        return payment_method

    def get_mailed_on_behalf(self) -> str | None:
        behalf_elem = self.driver.find_element(
            By.ID,
            'canpost_mailed_on_behalf_of_0'
        )
        behalf: str | None = behalf_elem.get_attribute('value')
        return behalf

# =============== Include / exclude  tab =============== #
    # TODO: I feel like this will run faster the element list check
    # other page classes and perf test
    def get_excluded_attribs(self) -> list[str]:
        excluded_attributes_spans = self.driver.find_element(
            By.NAME, 'excluded_attribute_ids'  # TODO: re-eval after viveks changes  # noqa: E501
        )
        excluded_attribs = excluded_attributes_spans.text.split('\n')
        return excluded_attribs
