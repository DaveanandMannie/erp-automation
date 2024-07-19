import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class BasePage:
    # TODO: decide weather or not to use cookies for auth
    def __init__(self, *args):
        load_dotenv()
        self.chrom_opts = Options()
        for arg in args:
            self.chrom_opts.add_argument(arg)
        self.driver = webdriver.Chrome(options=self.chrom_opts)
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASS')

    def login_staging(self):
        self.driver.get('https://staging.odoo.printgeek.ca')
        email_box = self.driver.find_element(By.ID, 'login')
        password_box = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Log in')]")

        if self.email:
            for char in self.email:
                email_box.send_keys(char)
        if self.password:
            for char in self.password:
                password_box.send_keys(char)
        login_button.click()

    def login_prod(self):
        self.driver.get('https://odoo.printgeek.ca')
        email_box = self.driver.find_element(By.ID, 'login')
        password_box = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Log in')]")

        if self.email:
            for char in self.email:
                email_box.send_keys(char)
        if self.password:
            for char in self.password:
                password_box.send_keys(char)
        login_button.click()

    def close(self):
        self.driver.close()


class ShippingMethods(BasePage):
    def __init__(self, *args):
        super().__init__(*args)
        self.driver.implicitly_wait(5)

    def navigate(self, url: str):
        self.driver.get(url)
        return

    def navigate_tab_destination(self):
        tab_elem = self.driver.find_element(By.LINK_TEXT, 'Destination Availability')
        tab_elem.click()
        return

    def navigate_tab_extra(self):
        tab_elem = self.driver.find_element(By.LINK_TEXT, 'Extra')
        tab_elem.click()
        return

    def navigate_tab_product_attrib(self):
        tab_elem = self.driver.find_element(By.LINK_TEXT, 'Product Attribute Configuration')
        tab_elem.click()

    def get_shipping_provider(self) -> str:
        provider_elem = self.driver.find_element(By.ID, 'delivery_type')
        provider: str = provider_elem.get_attribute('value').replace('"', '')  # type: ignore
        return provider

    def get_name(self) -> str:
        name_elem = self.driver.find_element(By.ID, 'name')
        name: str = name_elem.get_attribute('value')  # type: ignore
        return name

    # TODO: decide weather to turn this into a bool in order to detect following list validation
    def get_related_company(self) -> str:
        related_elem = self.driver.find_element(By.ID, 'related_to_client_company')
        if not related_elem:
            raise Exception('Element error: Not Found')
        is_on: str = related_elem.get_attribute('value')  # type: ignore
        return is_on

    def get_company_names(self) -> list:
        rows = self.driver.find_elements(By.XPATH, "//tr[@class='o_data_row']")
        company_names: list = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            for cell in cells:
                if cell.get_attribute('name') == 'display_name':
                    company_name = cell.get_attribute('data-tooltip')
                    company_names.append(company_name)
        return company_names

    def get_countries(self) -> list:
        country_badges = self.driver.find_elements(By.NAME, 'country_ids')
        country_list: list = country_badges[0].text.split('\n')
        return country_list

    def get_states(self) -> list:
        state_badges = self.driver.find_elements(By.NAME, 'state_ids')
        state_list: list = state_badges[0].text.split('\n')
        return state_list

    def get_zip_prefix(self) -> list:
        zip_badges = self.driver.find_elements(By.NAME, 'zip_prefix_ids')
        prefix_list: list = zip_badges[0].text.split('\n')
        return prefix_list

    def get_default_weight(self) -> str:
        def_weight_elem = self.driver.find_element(By.ID, 'default_product_weight')
        def_weight: str = def_weight_elem.get_attribute('value')  # type: ignore
        return def_weight

    def get_shipping_uom(self) -> str:
        uom_elem = self.driver.find_element(By.ID, 'uom_id')
        ship_uom: str = uom_elem.get_attribute('value')  # type: ignore
        return ship_uom

    def get_packaging(self) -> str:
        package_elem = self.driver.find_element(By.ID, 'packaging_id')
        package: str = package_elem.get_attribute('value')  # type: ignore
        return package

    def get_void_ship(self) -> str:
        void_elem = self.driver.find_element(By.ID, 'void_shipment')
        void: str = void_elem.get_attribute('value')  # type: ignore
        return void

    def get_service_type(self) -> str:
        service_elem = self.driver.find_element(By.ID, 'canpost_service_type_1')
        service: str = service_elem.get_attribute('value')  # type: ignore
        return service

    def get_service_option(self) -> str:
        option_elem = self.driver.find_element(By.ID, 'canpost_option_type')
        option: str = option_elem.get_attribute('value')  # type: ignore
        return option

    def get_customer_type(self) -> str:
        customer_type_elem = self.driver.find_element(By.ID, 'canpost_quote_type')
        customer_type: str = customer_type_elem.get_attribute('value').replace('"', '')  # type: ignore
        return customer_type

    # TODO: handle type int vs str
    def get_customer_number(self) -> str:
        customer_number_elem = self.driver.find_element(By.ID, 'canpost_customer_number')
        customer_number: str = customer_number_elem.get_attribute('value')  # type: ignore
        return customer_number

    def get_contract_id(self) -> str:
        contract_elem = self.driver.find_element(By.ID, 'canpost_contract_id')
        contract: str = contract_elem.get_attribute('value')  # type: ignore
        return contract

    def get_promo_code(self) -> str:
        promo_elem = self.driver.find_element(By.ID, 'canpost_promo_code')
        promo: str = promo_elem.get_attribute('value')  # type: # pyright: ignore
        return promo

    def get_payment_method(self) -> str:
        payment_method_elem = self.driver.find_element(By.ID, 'canpost_method_of_payment')
        payment_method: str = payment_method_elem.get_attribute('value')  # type: ignore
        return payment_method

    def get_mailed_on_behalf(self) -> str:
        behalf_elem = self.driver.find_element(By.ID, 'canpost_mailed_on_behalf_of')
        behalf: str = behalf_elem.get_attribute('value')  # type: ignore
        return behalf

    def get_included_attribs(self) -> list:
        included_attributes_spans = self.driver.find_element(By.NAME, 'included_attribute_ids')
        included_attribs: list = included_attributes_spans.text.split('\n')
        return included_attribs

    def get_excluded_attribs(self) -> list:
        excluded_attributes_spans = self.driver.find_element(By.NAME, 'excluded_attribute_ids')
        excluded_attribs = excluded_attributes_spans.text.split('\n')
        return excluded_attribs
