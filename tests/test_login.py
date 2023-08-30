
from os import name
import time
import utilities.custom_logger as cl
from tests.test_base import TestBase
from utilities.read_properties import *


class TestLogin(TestBase):
    # log = None
      
    def test_Validate_title(self):
        driver = self.driver
        json =read_json('jsonData1')
        log =cl.custom_logger()
        log.info("Enter orange HRM cred and login to homePage")
        self.orangeHrm_obj.loginToHomePage()
        assert driver.title == "OrangeHRM"
        log.debug(json['testJson'])
        
    def test_Validate_Url(self):
        driver = self.driver
        # self.log.info("Enter orange HRM cred and login to homePage")
        self.orangeHrm_obj.loginToHomePage()
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"  

    def test_read_json_files(self):
        log =cl.custom_logger()
        json_data = read_multiple_json_files()
        
        assert len(json_data) == 2
        # Assert specific values from the first JSON file
        log.info(json_data[0]['name'])
         # Assert specific values from the second JSON file
        log.info(json_data[1]['id'])
        log.info(json_data[1]['title'])


        
        # Other assertions or further processing on the JSON data
  

    def test_validate_leave(self):
        driver = self.driver
        # self.log.info("Enter orange HRM cred and login to homePage")
        homePage_Obj =  self.orangeHrm_obj.loginToHomePage()
        # self.log.info("get all sidebar elemenets")
        homePage_Obj.getSideBarElements("Leave")
        txtLeave = homePage_Obj.getLeaveList().text
        assert txtLeave == "Leave List"
        
     
     
    def test_fillInfoForm(self):
         driver=self.driver 
         homePage_Obj= self.orangeHrm_obj.loginToHomePage()
         homePage_Obj.getSideBarElements("My Info")
         self.myInfoPage_obj.enter_user_info(read_properties('MONTH'),read_properties('YEAR'),read_properties('DAY'))