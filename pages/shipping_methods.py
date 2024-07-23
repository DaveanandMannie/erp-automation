from pages.base import BasePage
from selenium.webdriver.common.by import By


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

    def navigate_tab_canpost_credentials(self):
        tab_elem = self.driver.find_element(
            By.LINK_TEXT, 'Canada Post Credentials'
        )
        tab_elem.click()
        return

    def navigate_tab_pb_credentials(self):
        tab_elem = self.driver.find_element(
            By.LINK_TEXT, 'Pitney Bowes Credentials'
        )
        tab_elem.click()
        return

    def navigate_tab_product_attrib(self):
        tab_elem = self.driver.find_element(
            By.LINK_TEXT, 'Product Attribute Configuration'
        )
        tab_elem.click()

# =============== Destination Availability=============== #
    def get_shipping_provider(self) -> str:
        provider_elem = self.driver.find_element(By.ID, 'delivery_type')
        provider: str = provider_elem.get_attribute('value')  # type: ignore
        provider = provider.replace('"', '')
        return provider

    def get_name(self) -> str:
        name_elem = self.driver.find_element(By.ID, 'name')
        name: str = name_elem.get_attribute('value')  # type: ignore
        return name

    def get_related_company(self) -> str:
        related_elem = self.driver.find_element(
            By.ID, 'related_to_client_company'
        )
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

    def get_delivery_product(self) -> str:
        delivery_product = self.driver.find_element(By.ID, 'product_id')
        delivery_product_name: str = (
                delivery_product.get_attribute('value')
        )  # type: ignore
        return delivery_product_name

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

# =============== Credential =============== #
    def get_canpost_dev_username(self) -> str:
        user_elem = self.driver.find_element(By.ID, 'canpost_test_username')
        user: str = user_elem.get_attribute('value')  # type: ignore
        return user

    def get_canpost_dev_password(self) -> str:
        password_elem = self.driver.find_element(
            By.ID, 'canpost_test_password'
        )
        password: str = password_elem.get_attribute('value')  # type: ignore
        return password

    def get_canpost_prod_username(self) -> str:
        user_elem = self.driver.find_element(
            By.ID, 'canpost_production_username'
        )
        user: str = user_elem.get_attribute('value')  # type: ignore
        return user

    def get_canpost_prod_password(self) -> str:
        password_elem = self.driver.find_element(
            By.ID, 'canpost_production_password'
        )
        password: str = password_elem.get_attribute('value')  # type: ignore
        return password

    def get_pb_dev_url(self) -> str:
        user_elem = self.driver.find_element(By.ID, 'url')
        username: str = user_elem.get_attribute('value')  # type: ignore
        return username

    def get_pb_dev_api_key(self) -> str:
        key_elem = self.driver.find_element(By.ID, 'api_key')
        key: str = key_elem.get_attribute('value')  # type: ignore
        return key

    def get_pb_dev_api_secret(self) -> str:
        secret_elem = self.driver.find_element(By.ID, 'api_secret')
        secret: str = secret_elem.get_attribute('value')  # type: ignore
        return secret

    def get_pb_dev_shipper_id(self) -> str:
        id_elem = self.driver.find_element(By.ID, 'shipper_id')
        id: str = id_elem.get_attribute('value')  # type: ignore
        return id

    def get_pb_dev_token(self) -> str:
        token_elem = self.driver.find_element(By.ID, 'shipper_id')
        token: str = token_elem.get_attribute('value')  # type: ignore
        return token

# =============== Extra tab =============== #
    def get_default_weight(self) -> str:
        def_weight_elem = self.driver.find_element(
            By.ID, 'default_product_weight'
        )
        def_weight: str = def_weight_elem.get_attribute('value')  # type:ignore
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
        service_elem = self.driver.find_element(
            By.ID, 'canpost_service_type_1'
        )
        service: str = service_elem.get_attribute('value')  # type: ignore
        return service

    def get_service_option(self) -> str:
        option_elem = self.driver.find_element(By.ID, 'canpost_option_type')
        option: str = option_elem.get_attribute('value')  # type: ignore
        return option

    def get_customer_type(self) -> str:
        customer_type_elem = self.driver.find_element(
            By.ID, 'canpost_quote_type'
        )
        customer_type: str | None = customer_type_elem.get_attribute('value')
        customer_type = customer_type.replace('"', '')  # type: ignore
        return customer_type  # type: ignore

    def get_customer_number(self) -> str:
        customer_number_elem = self.driver.find_element(
            By.ID, 'canpost_customer_number'
        )
        customer_number: str = (
                customer_number_elem.get_attribute('value')  # type: ignore
        )
        return customer_number

    def get_contract_id(self) -> str:
        contract_elem = self.driver.find_element(By.ID, 'canpost_contract_id')
        contract: str = contract_elem.get_attribute('value')  # type: ignore
        return contract

    def get_promo_code(self) -> str:
        promo_elem = self.driver.find_element(By.ID, 'canpost_promo_code')
        promo: str = promo_elem.get_attribute('value')  # type: ignore
        return promo

    def get_payment_method(self) -> str:
        payment_method_elem = self.driver.find_element(
            By.ID, 'canpost_method_of_payment'
        )
        payment_method: str | None = payment_method_elem.get_attribute('value')
        return payment_method  # type: ignore

    def get_mailed_on_behalf(self) -> str:
        behalf_elem = self.driver.find_element(
            By.ID, 'canpost_mailed_on_behalf_of'
        )
        behalf: str = behalf_elem.get_attribute('value')  # type: ignore
        return behalf

# =============== Include / exclude  tab =============== #
    def get_included_attribs(self) -> list:
        included_attributes_spans = self.driver.find_element(
            By.NAME, 'included_attribute_ids'
        )
        included_attribs: list = included_attributes_spans.text.split('\n')
        return included_attribs

    def get_excluded_attribs(self) -> list:
        excluded_attributes_spans = self.driver.find_element(
            By.NAME, 'excluded_attribute_ids'
        )
        excluded_attribs = excluded_attributes_spans.text.split('\n')
        return excluded_attribs
