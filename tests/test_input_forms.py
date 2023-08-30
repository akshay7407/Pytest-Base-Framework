import pytest
import time
from tests.test_base import TestBase
# import utilities.custom_logger as cl
from utilities.read_properties import read_yaml


# The test cases in here read test data by parameterization

class TestInputFormsPage(TestBase):

    def test_all_forms(self):
        self.input_forms_obj.click_input_forms_btn()
        assert (read_yaml('Input Forms') == self.input_forms_obj.input_forms_all_elements())

    @pytest.mark.parametrize("test_string, test_total",
                             [("Test Message", "8"),
                              pytest.param("test Message", "8", marks=pytest.mark.xfail),
                              pytest.param("Test Message", "9", marks=pytest.mark.xfail),
                              pytest.param("test Message", "18", marks=pytest.mark.xfail)
                              ])
    def test_simple_form_demo(self, test_string, test_total):
        assert (test_string == self.input_forms_obj.single_input_field())
        time.sleep(2)
        assert (test_total == self.input_forms_obj.two_input_fields())
        time.sleep(2)

    def test_checkbox_demo(self):
        assert (read_yaml('CHECKBOX_SUCCESS_MESSAGE') == self.checkbox_demo_obj.checkbox_demo())
        assert ("true" == self.checkbox_demo_obj.multiple_checkbox_demo())

    @pytest.mark.parametrize("radio_button_option",
                             ["Male", "Female"
                              ])
    def test_radio_button_demo(self, radio_button_option):
        self.radio_button_obj.radio_button_demo()
        assert (read_yaml('RADIO_BUTTON_SUCCESS_MESSAGE').replace("'Male'", "'" + radio_button_option + "'") ==
                self.radio_button_obj.select_radio_button_value(radio_button_option))

    @pytest.mark.parametrize("radio_button_option1, radio_button_option2",
                             [("Male", "0 - 5"),
                              ("Female", "0 - 5"),
                              ("Male", "5 - 15"),
                              ("Female", "5 - 15"),
                              ("Male", "15 - 50"),
                              ("Female", "15 - 50"),
                              ])
    def test_radio_button_demo(self, radio_button_option1, radio_button_option2):
        self.radio_button_obj.radio_button_demo()
        assert ("Sex : " + radio_button_option1 + "\n" + "Age group: " + radio_button_option2 ==
                self.radio_button_obj.group_radio_button_demo(radio_button_option1, radio_button_option2))
