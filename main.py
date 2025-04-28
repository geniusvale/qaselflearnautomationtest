from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time

class SauceDemoLoginPage:
    #Initiate Option for Edge Browser and add argument
    chromeOptions = Options()
    #edgeOptions.add_argument("--edge-skip-compat-layer-relaunch")
    chromeOptions.add_argument("--headless")

    #Initiate WebDriver Instance
    driver = webdriver.Chrome(
        options=chromeOptions,
    )

    saucedemourl = "https://www.saucedemo.com"

    #Goto websites
    driver.get(saucedemourl)

    #Defining Locator
    usernameField = driver.find_element(By.ID, "user-name")
    passwordField = driver.find_element(By.ID, "password")
    loginButton = driver.find_element(By.ID, "login-button")

    #Login Function
    def login(self):
        self.usernameField.send_keys("standard_user")
        self.passwordField.send_keys("secret_sauce")
        self.loginButton.click()
        time.sleep(5)
        if self.driver.current_url != self.saucedemourl:
            print("Login Success")
        else:
            print("Login Failed")
        time.sleep(5)
        self.driver.close()
    
loginPage = SauceDemoLoginPage()
loginPage.login()