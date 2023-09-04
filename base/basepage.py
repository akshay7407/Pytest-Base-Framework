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
      
        element = None
        wait = WebDriverWait(self.driver, 20)
        try:
            element = wait.until(EC.element_to_be_clickable((getattr(By,locator_type), locator_value)))
            return element
        except Exception as e:
            self.log.info("Element not found with given locator type:", e)
        return element
    
    def get_element(self, locator_value, locator_type="XPATH"):
        """
        method to get element on the page
        """
        element = None
        try:
            element = self.wait_for_element(locator_value, locator_type)
        except Exception as e:
            self.log.info(f"Element not found with given value {locator_value} ", e)
            assert False
        return element
    
    def wait_for_elements(self, locator_value, locator_type='XPATH'):
        """
        method for  wait for an elements
        """
        element = None
        wait = WebDriverWait(self.driver, 20)
        try:
            element = wait.until(EC.visibility_of_all_elements_located((getattr(By,locator_type), locator_value)))
            return element
        except Exception as e:
            self.log.info("Element not found with given locator type:", e)
            pass
        return element
    
    def check_elements_presence(self, locator_value, locator_type="XPATH"):
        """
        method to check if at least one element with the given locator type and value is present
        """
        elements = None
        try:
            elements = self.wait_for_elements(locator_value, locator_type)
            if len(elements) > 0:
                return True
            else:
                return False
        except Exception as e:
            return False
        
    def scroll_into_view(self, locator_value, locator_type="XPATH"):
        """
        method to scroll an element into view using JavaScript executor
        """
        element = self.get_element(locator_value, locator_type)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        else:
            self.log.info(f"Cannot scroll into view for element with value {locator_value} and type {locator_type}") 

    def get_element_text_using_js(self, locator_value, locator_type="XPATH"):
        """
        method to get the text of an element using JavaScript
        """
        element = self.get_element(locator_value, locator_type)
        if element:
            return self.driver.execute_script("return arguments[0].textContent;", element)
        else:
            self.log.info(f"Cannot get text for element with value {locator_value} and type {locator_type}")
            return None           
    
    
    def get_element_attribute(self, locator_value, locator_type="XPATH", attribute_name=""):
        """
        method to get an attribute from an element
        """
        element = self.get_element(locator_value, locator_type)
        if element:
            if attribute_name:
                return element.get_attribute(attribute_name)
            else:
                print("Attribute name not provided.")
        else:
            print(f"Cannot retrieve attribute from element with value {locator_value} and type {locator_type}")
        return None
    
    def get_elements(self, locator_value, locator_type="XPATH"):
        """
        method to get elements on the page
        """
        element = None
        try:
            element = self.wait_for_elements(locator_value, locator_type)
        except Exception as e:
            self.log.info(f"Element not found with given value {locator_value} ", e)
            assert False
        return element

    def click_element(self, locator_value, locator_type="XPATH"):
        """
        method to click an element
        """
        element = None
        try:
            element = self.get_element(locator_value, locator_type)
            element.click()
            self.log.info(f"Clicked on  element with given value {locator_value}")
        except Exception as e:
            self.log.info(f"Element cannot be clicked at: {locator_value} ", e)
            assert False

    def send_text(self, text, locator_value, locator_type="XPATH"):
        """
        method to write text into the element
        """
        element = None
        try:
          
            element = self.get_element(locator_value, locator_type)
            element.click()
            element.clear() 
            element.send_keys(text)
            self.log.info(f"Send text to element with given value {locator_value}")
        except Exception as e:
            self.log.info(f"Unable to send text to element with given value {locator_value} ", e)
            assert False

    def is_element_displayed(self, locator_value, locator_type="XPATH"):
        """
        method to verify element is displayed or not
        """
        element = None
        try:
          
            element = self.get_element(locator_value, locator_type)
            element.is_displayed()
            self.log.info(f"Displayed Element with given value {locator_value}")
            return True
        except Exception as e:
            self.log.info(f"Element with locator value: {locator_value} is not displayed. ", e)
            return False

    def is_element_enabled(self, locator_value, locator_type="XPATH"):
        """
        method to verify element is enabled or not
        """
        element = None
        try:
          
            element = self.get_element(locator_value, locator_type)
            element.is_enabled()
            return True
        except Exception as e:
            self.log.info(f"Element with locator value: {locator_value} is not enabled. ", e)
            return False
        
    def is_element_selected(self, locator_value, locator_type="XPATH"):
        """
        method to check if an element is selected
        """
        element = self.get_element(locator_value, locator_type)
        if element:
            return element.is_selected()
        else:
            self.log.info(f"Cannot determine if element with value {locator_value} and type {locator_type} is selected.")
            return False    
        
    def scroll_to_element(self, locator_value, locator_type="XPATH"):
        """
        method to scroll to an element using ActionChains
        """
        element = self.get_element(locator_value, locator_type)
        if element:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        else:
            self.log.info(f"Cannot scroll to element with value {locator_value} and type {locator_type}")    

    def get_element_text(self, locator_value, locator_type="XPATH"):
        """
        Method for get element text
        """
        try:
          
            element = self.wait_for_element(locator_value, locator_type)
        except Exception as e:
            self.log.info(f"Element not found with given value {locator_value}", e)
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
          
            element = self.driver.find_element_by_xpath(locator_value)
            attribute_value = element.get_attribute(attribute_name)
        except Exception as e:
            self.log.info(f"Element not found with given value {locator_value} ", e)
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

