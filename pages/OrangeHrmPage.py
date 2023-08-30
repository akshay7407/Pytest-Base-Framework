from base.basepage import BasePage
from pages.hrm_HomePage import HrmHomePage
from utilities.read_properties import *
import utilities.custom_logger as cl


class OrangeHrmPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log =cl.custom_logger()    
    tfUserName = "//input[@name='username']"
    tfPassword = "//input[@name='password']"
    btnSubmit =  "//button[@type='submit']"
    
    def loginToHomePage(self,input):
        self.log.info("Enter userName and password")
        self.log.info(f"Enter username :"+ input['username'])
        self.send_text(input['username'],self.tfUserName )
        self.log.info(f"Enter password :"+ input['password'])
        self.send_text(input['password'],self.tfPassword)
        self.click_element(self.btnSubmit)
        hrmHomePage_obj = HrmHomePage(self.driver)
        return hrmHomePage_obj