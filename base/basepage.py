from allure_commons.types import AttachmentType
import allure
import pytest
import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    log = cl.custom_logger()

    def __init__(self, driver):
        self.driver = driver
        
    def wait_for_element(self, locator_value, locator_type='XPATH'):
        """
        method for explicit wait for an element
        """
        locator_type = locator_type.lower()
        element = None
        wait = WebDriverWait(self.driver, 20)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, locator_value)))
            return element
        except Exception as e:
            print("Element not found with given locator type:", e)
        return element

    def get_element(self, locator_value, locator_type="XPATH"):
        """
        method to get element on the page
        """
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
        except Exception as e:
            self.log.info(f"Element not found with given value {locator_value} ", e)
            self.take_screenshot(locator_type)
            assert False
        return element

    def click_element(self, locator_value, locator_type="XPATH"):
        """
        method to click an element
        """
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.click()
            self.log.info(f"Clicked on  element with given value {locator_value}")
        except Exception as e:
            self.log.info(f"Element cannot be clicked at: {locator_value} ", e)
            self.take_screenshot(locator_type)
            assert False

    def send_text(self, text, locator_value, locator_type="XPATH"):
        """
        method to write text into the element
        """
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.click()
            element.clear() 
            element.send_keys(text)
            self.log.info(f"Send text to element with given value {locator_value}")
        except Exception as e:
            self.log.info(f"Unable to send text to element with given value {locator_value} ", e)
            self.take_screenshot(locator_type)
            assert False

    def is_element_displayed(self, locator_value, locator_type="XPATH"):
        """
        method to verify element is displayed or not
        """
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.is_displayed()
            self.log.info(f"Displayed Element with given value {locator_value}")
            return True
        except Exception as e:
            self.log.info(f"Element with locator value: {locator_value} is not displayed. ", e)
            self.take_screenshot(locator_type)
            return False

    def is_element_enabled(self, locator_value, locator_type="XPATH"):
        """
        method to verify element is enabled or not
        """
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.is_enabled()
            return True
        except Exception as e:
            self.log.info(f"Element with locator value: {locator_value} is not enabled. ", e)
            self.take_screenshot(locator_type)
            return False

    def take_screenshot(self, text):
        """
        method to take screenshots for allure report
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def get_element_text(self, locator_value, locator_type="XPATH"):
        """
        Method for get element text
        """
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
        except Exception as e:
            self.log.info(f"Element not found with given value {locator_value}", e)
            self.take_screenshot(locator_type)
            assert False
        return element.text

    def scroll_down(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_hidden_element_attribute(self, locator_value, locator_type="xpath", attribute_name=None):
        """
        method to get element on the page
        """
        element = None
        wait = WebDriverWait(self.driver, 10)
        try:
            locator_type = locator_type.lower()
            element = self.driver.find_element_by_xpath(locator_value)
            attribute_value = element.get_attribute(attribute_name)
        except Exception as e:
            self.log.info(f"Element not found with given value {locator_value} ", e)
            self.take_screenshot(locator_type)
            assert False
        return attribute_value
    
    def click_element_with_text(self , locator_strategy, locator_value, expected_text, timeout=10):
         locator = (locator_strategy, locator_value)
         elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    
         for element in elements:
          element_text = element.text.strip()
          if element_text == expected_text:
            element.click()
            return True
    
         print(f"Element with text '{expected_text}' not found.")
         return False
     
    
    
    def move_and_click_element(driver, locator_type, locator_value):
        element = None
        try:
            if locator_type == "id":
                element = driver.find_element_by_id(locator_value)
            elif locator_type == "class":
                element = driver.find_element_by_class_name(locator_value)
            elif locator_type == "xpath":
                element = driver.find_element_by_xpath(locator_value)
            elif locator_type == "css":
                element = driver.find_element_by_css_selector(locator_value)
                
            if element is not None:
                actions = ActionChains(driver)
                actions.move_to_element(element).click().perform()
            else:
                raise ValueError(f"Element not found: {locator_type}={locator_value}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")

