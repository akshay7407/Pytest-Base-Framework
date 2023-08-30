import time
from base.basepage import BasePage
import allure


class DatePickerPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Input Forms Page Locators:
    date_picker_btn_xpath = "//a[@class='dropdown-toggle' and contains(text(), 'Date pickers')]"
    date_picker_dropdown_xpath = "(//*[@id='navbar-brand-centered']/ul[1]/li[2]/ul/li)"

    @allure.step("Click on Date Picker option")
    def click_date_picker_btn(self):
        return self.click_element(self.date_picker_btn_xpath)

    @allure.step("Fetch all elements of drop down")
    def date_picker_all_elements(self):
        drop_down_elements = []
        for x in range(0, 2):   # TO DO: Remove hard coding for length
            test_string = self.get_element_text(locator_value=self.date_picker_dropdown_xpath+"["+str(x+1)+"]")
            drop_down_elements.append(test_string)
        return drop_down_elements


class BootStrapDatePicker(DatePickerPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Date Picker Page Locators:
    bootstrap_date_picker_btn_xpath = "(//*[@id='navbar-brand-centered']/ul[1]/li[2]/ul/li)[1]"
    select_date_textbox_xpath = "//*[@id='sandbox-container1']/descendant::input[@type='text']"

    @allure.step("Click on Bootstrap Date Picker option")
    def click_bootstrap_date_picker_btn(self):
        return self.click_element(self.bootstrap_date_picker_btn_xpath)

    def click_select_date_field(self):
        return self.click_element(self.select_date_textbox_xpath)







