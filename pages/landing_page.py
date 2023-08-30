from base.basepage import BasePage
import allure


class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Landing Page Locators:
    top_navigation_bar = "navbar-brand-centered"
    input_forms = "//*[@id='navbar-brand-centered']/ul[1]/li[1]/a"
    start_practising_btn = "btn_basic_example"

    @allure.step("Top Navigation bar displayed successfully")
    def is_displayed_top_navigation_bar(self):
        """
        To verify whether banana logo is displayed or not
        """
        return self.is_element_displayed(self.top_navigation_bar, "ID")

    @allure.step("Top Navigation bar elements")
    def top_navigation_bar_elements(self):
        """
        To verify whether banana logo is displayed or not
        """
        print(self.top_navigation_bar_elements.__doc__)
        return self.is_element_displayed(self.top_navigation_bar, "ID")

    @allure.step("Input Forms link")
    def input_forms_method(self):
        """
        Input Forms docstring
        """
        print(self.input_forms.__doc__)
        return self.click_element(self.input_forms, locator_type="xpath")

    @allure.step("Start Practicing Button")
    def click_start_practising_btn(self):
        """
        click action performed
        :return: None
        """
        self.scroll_down()
        return self.click_element(self.start_practising_btn, locator_type="id")


