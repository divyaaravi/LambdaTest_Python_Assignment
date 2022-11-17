import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import unittest

test_site = "https://www.lambdatest.com/selenium-playground/"

username = str(os.environ.get("m1084211"))
access_key = str(os.environ.get("YVAMtT2aKeOLFA1EBy0Z4TTxFZYjgDMFmtERDKCh9LZxrJpkY5"))
gridUrl = "hub.lambdatest.com/wd/hub"

class LambdaTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'LT:Options': {
                "user": username,
                "accessKey": access_key,
                "build": "Assignment",
                "name": "LambdaTest",
                "platformName": "Windows 10",
            },
            "browserName": "Chrome",
            "browserVersion": "latest",
        }
        url = "https://" + "m1084211" + ":" + "YVAMtT2aKeOLFA1EBy0Z4TTxFZYjgDMFmtERDKCh9LZxrJpkY5"+ "@" + gridUrl
        self.driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=desired_caps)


    def test_scenario_one(self):
        driver = self.driver

        driver.get(test_site)
        driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
        validate_url = driver.current_url
        assert "simple-form-demo" in validate_url

        enter_text = "Welcome to Lambda Test"
        driver.find_element(By.XPATH, "//*[@id='user-message']").send_keys(enter_text)
        driver.find_element(By.ID, "showInput").click()
        actual_text = driver.find_element(By.ID, "message").text
        assert enter_text == actual_text, print("text message does not match the entered text")


    def test_scenario_two(self):
        driver = self.driver
        driver.get(test_site)
        driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click()
        source_element = driver.find_element(By.XPATH, "//*[@id='rangeSuccess']")

        target_element = driver.find_element(By.XPATH, "//*[@id='rangeSuccess']")
        action = ActionChains(driver)

        action.drag_and_drop(source_element, target_element)

        action.perform()
        print("Successfully executed")


    def test_scenarion_three(self):
        driver = self.driver
        driver.get(test_site)
        driver.find_element(By.LINK_TEXT, "Input Form Submit").click()

        assert "Please fill out this field" in "Please fill out this field"

        driver.find_element(By.ID, "name").send_keys("XYZ")

        driver.find_element(By.ID, "inputEmail4").send_keys("abc@gmail.com")
        driver.find_element(By.ID, "inputPassword4").send_keys("abc123")
        driver.find_element(By.NAME, "company").send_keys("Mindtree")
        driver.find_element(By.NAME, "website").send_keys("www.mindtree.com")

        select = Select(driver.find_element(By.NAME, 'country'))
        select.select_by_visible_text('India')
        driver.find_element(By.ID, "inputCity").send_keys("Bangalore")
        driver.find_element(By.NAME, "address_line1").send_keys("1st main 7th cross")
        driver.find_element(By.ID, "inputAddress2").send_keys("Brookfield")
        driver.find_element(By.ID, "inputState").send_keys("Karnataka")
        driver.find_element(By.ID, "inputZip").send_keys("560018")

        driver.find_element(By.CSS_SELECTOR, "#seleniumform > div.text-right.mt-20 > button").click()
        time.sleep(5)
        message = driver.find_element(By.XPATH, "//*[@id='__next']/div/section[3]/div/div/div[2]/div/p")
        assert "Thanks for contacting us, we will get back to you shortly", message

        print("Test scenario passed succssefully")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()