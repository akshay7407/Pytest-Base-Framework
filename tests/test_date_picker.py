import pytest
import time

# from tests.conftest import retry
from tests.test_base import TestBase
# import utilities.custom_logger as cl
from utilities.read_properties import read_yaml


# The test cases in here read test data by parameterization

class TestDatePickerPage(TestBase):

    # @retry
    def test_date_picker_dropdown(self):
        self.date_picker_obj.click_date_picker_btn()
        assert (read_yaml('Date pickers') == self.date_picker_obj.date_picker_all_elements())

    def test_bootstrap_date_picker_01(self):
        self.date_picker_obj.click_date_picker_btn()
        self.bootstrap_date_picker_obj.click_bootstrap_date_picker_btn()
        self.bootstrap_date_picker_obj.click_select_date_field()
        time.sleep(4)
