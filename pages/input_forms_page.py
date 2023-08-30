import time
from base.basepage import BasePage
import allure


class InputFormsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Input Forms Page Locators:
    input_forms_btn_xpath = "//a[@class='dropdown-toggle' and contains(text(), 'Input Forms')]"
    input_forms_dropdown_xpath = "(//*[@id='navbar-brand-centered']/ul[1]/li[1]/ul/li)"

    @allure.step("Click on Input Forms")
    def click_input_forms_btn(self):
        return self.click_element(self.input_forms_btn_xpath)

    @allure.step("Fetch all elements of drop down")
    def input_forms_all_elements(self):
        drop_down_elements = []
        for x in range(0, 7):   # TO DO: Remove hard coding for length
            test_string = self.get_element_text(locator_value=self.input_forms_dropdown_xpath+"["+str(x+1)+"]")
            drop_down_elements.append(test_string)
        return drop_down_elements


class SimpleFormDemo(InputFormsPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Simple form demo locators
    simple_form_demo_btn_xpath = "//*[@id='navbar-brand-centered']/descendant::a[text()='Simple Form Demo']"
    enter_message_text_xpath = "//input[@id='user-message']"
    show_message_btn_xpath = "//form[@id='get-input']/button[@class='btn btn-default']"
    text_verification_xpath = "//div[@id='user-message']/span"
    first_input_field_xpath = "//input[@id='sum1']"
    second_input_field_xpath = "//input[@id='sum2']"
    get_total_btn_xpath = "//button[text()='Get Total']"
    total_verification_xpath = "//span[@id='displayvalue']"

    @allure.step("Perform operations on single input field")
    def single_input_field(self):
        self.click_element(self.input_forms_btn_xpath)
        self.click_element(locator_value=self.simple_form_demo_btn_xpath)
        self.send_text("Test Message", locator_value=self.enter_message_text_xpath)
        self.click_element(locator_value=self.show_message_btn_xpath)
        return self.get_element_text(locator_value=self.text_verification_xpath)

    @allure.step("Perform operations on two input fields")
    def two_input_fields(self):
        self.send_text("5", locator_value=self.first_input_field_xpath)
        self.send_text("3", locator_value=self.second_input_field_xpath)
        self.click_element(locator_value=self.get_total_btn_xpath)
        return self.get_element_text(locator_value=self.total_verification_xpath)


class CheckBoxDemo(InputFormsPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Checkbox demo locators
    checkbox_demo_xpath = "//*[@id='navbar-brand-centered']/descendant::a[text()='Checkbox Demo']"
    single_checkbox_xpath = "//input[@id='isAgeSelected']"
    checkbox_success_message_xpath = "//div[@id='txtAge']"
    multiple_check_all_btn_xpath = "//input[@id='check1']"
    verification_checked_xpath = "//input[@id='isChkd']"

    @allure.step("Single checkbox selected")
    def checkbox_demo(self):
        self.click_element(locator_value=self.input_forms_btn_xpath)
        self.click_element(locator_value=self.checkbox_demo_xpath)
        self.click_element(locator_value=self.single_checkbox_xpath)
        return self.get_element_text(locator_value=self.checkbox_success_message_xpath)

    @allure.step("Clicked on Check All button to verify the attribute")
    def multiple_checkbox_demo(self):
        self.click_element(locator_value=self.multiple_check_all_btn_xpath)
        element = self.driver.find_element_by_xpath(self.verification_checked_xpath)
        self.driver.execute_script("$(arguments[0]).click();", element)
        return self.get_hidden_element_attribute(locator_value=self.verification_checked_xpath, attribute_name="value")


class RadioButtonDemo(InputFormsPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Radio button demo locators
    radio_button_demo_xpath = "//*[@id='navbar-brand-centered']/descendant::a[text()='Radio Buttons Demo']"
    single_radio_btn_xpath = "(//input[@type='radio' and @value='[OPTION]'])[1]"
    get_checked_value_btn_xpath = "//button[@id='buttoncheck']"
    radio_button_verification_text_xpath = "//p[@class='radiobutton']"
    group_radio_btn_gender_xpath = "//input[@name='gender' and @value='[OPTION]']"
    group_radio_btn_age_xpath = "//input[@name='ageGroup' and @value='[OPTION]']"
    get_values_btn_xpath = "//button[text()='Get values']"
    group_radio_btn_verification_text_xpath = "//p[@class='groupradiobutton']"

    @allure.step("Radio Button Demo")
    def radio_button_demo(self):
        self.click_element(locator_value=self.input_forms_btn_xpath)
        self.click_element(locator_value=self.radio_button_demo_xpath)

    @allure.step("Select the values")
    def select_radio_button_value(self, radio_button_value):
        self.click_element(self.single_radio_btn_xpath.replace('[OPTION]', radio_button_value))
        self.click_element(locator_value=self.get_checked_value_btn_xpath)
        return self.get_element_text(locator_value=self.radio_button_verification_text_xpath)

    @allure.step("Group Radio button demo")
    def group_radio_button_demo(self, option1, option2):
        self.click_element(self.group_radio_btn_gender_xpath.replace('[OPTION]', option1))
        self.click_element(self.group_radio_btn_age_xpath.replace('[OPTION]', option2))
        self.click_element(locator_value=self.get_values_btn_xpath)
        return self.get_element_text(locator_value=self.group_radio_btn_verification_text_xpath)
