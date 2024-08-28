import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    # TODO: decide weather or not to use cookies for auth
    def __init__(self, *args: str):
        _ = load_dotenv()
        self.chrome_opts = Options()
        for arg in args:
            self.chrome_opts.add_argument(arg)
            if arg == 'headless':
                self.chrome_opts.add_argument('--window-size=1920x1080')
        self.driver = webdriver.Chrome(options=self.chrome_opts)
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASS')

    def login_staging(self):
        self.driver.get('https://staging.odoo.printgeek.ca')
        email_box: WebElement = self.driver.find_element(By.ID, 'login')
        password_box: WebElement = self.driver.find_element(By.ID, 'password')
        login_button: WebElement = self.driver.find_element(
            By.XPATH, "//button[@type='submit' and contains(text(), 'Log in')]"
        )

        if self.email:
            for char in self.email:
                email_box.send_keys(char)
        if self.password:
            for char in self.password:
                password_box.send_keys(char)
        login_button.click()

    def login_prod(self):
        self.driver.get('https://odoo.printgeek.ca')
        email_box: WebElement = self.driver.find_element(By.ID, 'login')
        password_box: WebElement = self.driver.find_element(By.ID, 'password')
        login_button: WebElement = self.driver.find_element(
            By.XPATH, "//button[@type='submit' and contains(text(), 'Log in')]"
        )

        if self.email:
            for char in self.email:
                email_box.send_keys(char)
        if self.password:
            for char in self.password:
                password_box.send_keys(char)
        login_button.click()

    def login_uat(self):
        self.driver.get('https://uat.odoo.printgeek.ca')
        email_box: WebElement = self.driver.find_element(By.ID, 'login')
        password_box: WebElement = self.driver.find_element(By.ID, 'password')
        login_button: WebElement = self.driver.find_element(
            By.XPATH, "//button[@type='submit' and contains(text(), 'Log in')]"
        )
        if self.email:
            for char in self.email:
                email_box.send_keys(char)

        if self.password:
            for char in self.password:
                password_box.send_keys(char)
        login_button.click()

    def navigate(self, url: str):
        self.driver.get(url)
        return

    def close(self):
        self.driver.close()
