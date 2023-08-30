
from base.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.read_properties import *


class MyInfoPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver =driver
        
    tfFirstName ="//input[@name='firstName']"
    tfLastName = "//input[@name='lastName']"
    calendar = "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]"
    ddMonth ="//div[@class='oxd-calendar-selector-month-selected']"
    ddYear ="//div[@class='oxd-calendar-selector-year-selected']"
    months_locator = (By.XPATH,"//li[contains(@class, 'oxd-calendar-dropdown--option')]")
    ddDay = "//div[contains(text(), '{value}')]"
    tfNickname="//label[text()='Nickname']/../following::div[1]//input"
    tfEmployeeId ="//label[text()='Employee Id']/../following::div[1]//input"
    countryNames ="div.oxd-select-option span"
    ddNationality ="(//div[contains(@class,'oxd-form-row')]//div[contains(@class,'oxd-select-text-input')])[1]"
    ddMartialStatus =(By.XPATH ,"(//div[contains(@class,'oxd-form-row')]//div[contains(@class,'oxd-select-text-input')])[2]")
    ddValue="//span[text()='{value}']/.."
    popUpmsg ="//p[text()='Successfully Updated']"
    btnSave ="(//button[@type='submit'])[1]"
   
    
    
    def enter_user_info(self,month ,year,day ):
        self.send_text(read_properties("FIRSTNAME"),self.tfFirstName)
        self.send_text(read_properties("LASTNAME"),self.tfLastName) 
        self.send_text(read_properties("NICKNAME"),self.tfNickname)
        self.send_text(read_properties("EMPID"),self.tfEmployeeId)
        self.click_element(self.calendar) 
        self.click_element(self.ddMonth)  
        self.select_calendar_dropdownValues(month)
        self.click_element(self.ddYear) 
        self.select_calendar_dropdownValues(year)
        self.click_element(self.ddDay.format(value=day))
        self.click_element(self.ddNationality)
        self.click_element(self.ddValue.format(value="Indian"))
        self.clickOnMartialStatus()
        self.click_element(self.ddValue.format(value="Married"))
        self.click_element(self.btnSave)
        assert self.is_element_displayed(self.popUpmsg) == True
    
    def select_calendar_dropdownValues(self , value):
        dropdown_locator = (By.CLASS_NAME, "oxd-calendar-selector")
        dropdown_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(dropdown_locator))
        dropdown_element.click()
        option_locator = (By.XPATH, f"{self.months_locator[1]}[text()='{value}']")
        option_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(option_locator))
        option_element.click()
    
    def clickOnMartialStatus(self):
        return self.driver.find_element(*self.ddMartialStatus).click()
 