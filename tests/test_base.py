
import pytest
from pages.OrangeHrmPage import OrangeHrmPage
from pages.landing_page import LandingPage
from pages.input_forms_page import InputFormsPage
from pages.input_forms_page import SimpleFormDemo
from pages.input_forms_page import CheckBoxDemo
from pages.input_forms_page import RadioButtonDemo
from pages.date_pickers_page import DatePickerPage
from pages.date_pickers_page import BootStrapDatePicker
from pages.myInfoPage import MyInfoPage


@pytest.mark.usefixtures("before_method")
class TestBase:

    @pytest.fixture(autouse="true")
    def class_objects(self):
        self.myInfoPage_obj = MyInfoPage(self.driver)
        self.orangeHrm_obj = OrangeHrmPage(self.driver)
        self.landing_obj = LandingPage(self.driver)
        self.input_forms_obj = InputFormsPage(self.driver)
        self.simple_form_obj = SimpleFormDemo(self.driver)
        self.checkbox_demo_obj = CheckBoxDemo(self.driver)
        self.radio_button_obj = RadioButtonDemo(self.driver)
        self.date_picker_obj = DatePickerPage(self.driver)
        self.bootstrap_date_picker_obj = BootStrapDatePicker(self.driver)
