from base.basepage import BasePage
from pages.hrm_HomePage import HrmHomePage
from utilities.read_properties import *


class OrangeHrmPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    tfUserName = "//input[@name='username']"
    tfPassword = "//input[@name='password']"
    btnSubmit =  "//button[@type='submit']"
    
    def loginToHomePage(self):
        # self.driver.g
        self.send_text(read_properties('USERNAME'),self.tfUserName )
        self.send_text(read_properties('PASS'),self.tfPassword)
        self.click_element(self.btnSubmit)
        hrmHomePage_obj = HrmHomePage(self.driver)
        return hrmHomePage_obj