import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class BasePage():
    # TODO: decide weather or not to use cookies for auth
    def __init__(self):
        load_dotenv()
        self.driver = webdriver.Chrome()
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASS')

    def login(self):
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
        sleep(2)

    def close(self):
        self.driver.close()
