import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from time import sleep

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASS = os.getenv('PASS')

driver = webdriver.Chrome()
driver.get('https://staging.odoo.printgeek.ca')
email_box = driver.find_element(By.ID, 'login')
password_box = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Log in')]")
if EMAIL:
    for char in EMAIL:
        email_box.send_keys(char)
if PASS:
    for char in PASS:
        password_box.send_keys(char)
login_button.click()
sleep(2)
# driver.get('https://staging.odoo.printgeek.ca/web#id=5&menu_id=356&cids=1&action=609&model=delivery.carrier&view_type=form')
driver.get('https://staging.odoo.printgeek.ca/web#id=4&cids=1&menu_id=356&action=609&model=delivery.carrier&view_type=form')
# driver.get('https://staging.odoo.printgeek.ca/web#id=14&cids=1&menu_id=356&action=609&model=delivery.carrier&view_type=form')
sleep(5)

# for shipping  provider
# provider_el = driver.find_element(By.XPATH, "//div[@name='delivery_type' and contains(@class, 'o_field_widget')]/select[@id='delivery_type']")
provider_el = driver.find_element(By.ID, 'delivery_type')
provider = provider_el.get_attribute('value')
provider_text = provider_el.text
if provider:
    print(f'Provider: {provider}')
else:
    print('No Provider')

# for shipping provider
# product_el = driver.find_element(By.XPATH, "//div[@class='o-autocomplete dropdown']/input[@id='product_id']")
product_el = driver.find_element(By.ID, 'product_id') 
product = product_el.get_attribute('value')
print(f'Deleviery product: {product}')

# for  related client company this is to check the bool
r_company_el = driver.find_element(By.ID, 'related_to_client_company')
company = r_company_el.get_attribute('value')
print(f'Related to company: {company}')

# this next one should only run if above works rows of companies
rows = driver.find_elements(By.XPATH, "//tr[@class='o_data_row']")
company_names = []
for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    for cell in cells:
        if cell.get_attribute('name') == 'display_name':
            company_name = cell.get_attribute('data-tooltip')
            company_names.append(company_name)
print(f'Connected companies: {company_names}')

# this is for countries
country_badges = driver.find_elements(By.NAME, 'country_ids')
country_list = country_badges[0].text.split('\n')
print(f'List of country: {country_list}')

# this is for "states"
state_badges = driver.find_elements(By.NAME, 'state_ids')
state_list = state_badges[0].text.split('\n')
print(f'List of states: {state_list}')

# this would be fore the zip prefex -> pulling all the badges in the div
zip_badges = driver.find_elements(By.NAME, 'zip_prefix_ids')
badge_list =  zip_badges[0].text.split('\n')  # -> weird its a long string with \n seperators
print(f'List of prefix: {badge_list}')

print('===============Extra Tab===============')
# clicking destination tab
extra_tab = driver.find_element(By.LINK_TEXT, 'Extra')
extra_tab.click()
sleep(0.5)

# get the deafult weight
default_weight_el = driver.find_element(By.ID, 'default_product_weight')
default_weight = default_weight_el.get_attribute('value')
print(f'Default weight: {default_weight}')

# get shipping uom:
shipping_uom_el = driver.find_element(By.ID, 'uom_id')
shipping_uom = shipping_uom_el.get_attribute('value')
print(f'Shipping UOM: {shipping_uom}')

# get packaging
package_el = driver.find_element(By.ID, 'packaging_id')
package = package_el.get_attribute('value')
print(f'Default package: {package}')

# is void ship on
void_shipment_el = driver.find_element(By.ID, 'void_shipment')
void_shipment = void_shipment_el.get_attribute('value')
print(f'void shipping: {void_shipment}')

# get service type
service_type_el = driver.find_element(By.ID, 'canpost_service_type')
service_type = service_type_el.get_attribute('value')
print(f'Service type: {service_type}')

# get service options
desired_options_el = driver.find_element(By.ID, 'canpost_option_type')
desired_options = desired_options_el.get_attribute('value')
print(f'Desired options: {desired_options}')

# get customer_type -> weird instance of double quotes
customer_type_el = driver.find_element(By.ID, 'canpost_quote_type')
customer_type = customer_type_el.get_attribute('value')
print(f'Customer type: {customer_type}')

# get customer number
customer_number_el = driver.find_element(By.ID, 'canpost_customer_number')
customer_number = customer_number_el.get_attribute('value')
print(f'Customer number: {customer_number}')

# get contract ID
contract_id_el = driver.find_element(By.ID, 'canpost_contract_id')
contract_id = contract_id_el.get_attribute('value')
print(f'Contract ID: {contract_id}')

# get promo code
promo_code_el= driver.find_element(By.ID, 'canpost_promo_code')
promo_code = promo_code_el.get_attribute('value')
print(f'Promo code: {promo_code}')

# get payment_method
payment_method_el = driver.find_element(By.ID, 'canpost_method_of_payment')
payment_method = payment_method_el.get_attribute('value')
print(f'Payment method: {payment_method}')

# get mailed on behalf of 
behalf_el = driver.find_element(By.ID, 'canpost_mailed_on_behalf_of')
behalf = behalf_el.get_attribute('value')
print(f'Mailed on Behalf of: {behalf}')

print('===============Product Attrib Tab===============')
# clicking on Product Attribute Configuration
product_attrib_tab = driver.find_element(By.LINK_TEXT, 'Product Attribute Configuration')
product_attrib_tab.click()
sleep(1)


# included/excluded tests

included_attributes_spans = driver.find_element(By.NAME,'included_attribute_ids')
included_attribs = included_attributes_spans.text.split('\n')
print(f'Included Attributes: {included_attribs}')

excluded_attributes_spans = driver.find_element(By.NAME,'excluded_attribute_ids')
excluded_attribs = excluded_attributes_spans.text.split('\n')
print(f'Excluded Attributes: {excluded_attribs}')

print('===============Barebones Scrape Completed===============')

print(
    'Please keep in mind this is not a full validation. This a high level check to see if the most relevent fields are filled in'
)

driver.close()
