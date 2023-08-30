
from os import name
import pytest
import utilities.custom_logger as cl
from tests.test_base import TestBase
from utilities.read_properties import *


class TestLogin(TestBase):
    read_json =read_json('jsonData1')

    @pytest.mark.smoke  
    def test_Validate_title(self):
        driver = self.driver
        log =cl.custom_logger()
        log.info("Enter orange HRM cred and login to homePage")
        self.orangeHrm_obj.loginToHomePage(self.read_json['credential'])
        assert driver.title == "OrangeHRM"
        log.debug(self.read_json['testJson'])

    @pytest.mark.smoke      
    def test_Validate_Url(self):
        driver = self.driver
        # self.log.info("Enter orange HRM cred and login to homePage")
        self.orangeHrm_obj.loginToHomePage(self.read_json['credential'])
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"  

  
    @pytest.mark.smoke  
    def test_validate_leave(self):
        driver = self.driver
        # self.log.info("Enter orange HRM cred and login to homePage")
        homePage_Obj =  self.orangeHrm_obj.loginToHomePage(self.read_json['credential'])
        # self.log.info("get all sidebar elemenets")
        homePage_Obj.getSideBarElements("Leave")
        txtLeave = homePage_Obj.getLeaveList().text
        assert txtLeave == "Leave List"
        
     
     
    def test_fillInfoForm(self):
         driver=self.driver 
         homePage_Obj= self.orangeHrm_obj.loginToHomePage(self.read_json['credential'])
         homePage_Obj.getSideBarElements("My Info")
         self.myInfoPage_obj.enter_user_info(read_properties('MONTH'),read_properties('YEAR'),read_properties('DAY'))