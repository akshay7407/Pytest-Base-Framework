from base.basepage import BasePage
from selenium.webdriver.common.by import By



class HrmHomePage(BasePage):
    
     def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
     allSidebarLinks =  "//a[@class='oxd-main-menu-item']/descendant::span"
     txtLeaveList = "//h5[text()='Leave List']"
     
    
    
     def getSideBarElements(self , elementValue):
         self.click_element_with_text(By.XPATH,self.allSidebarLinks,elementValue,timeout=20)
     
     def getLeaveList(self):
         return self.get_element(self.txtLeaveList)