
import pytest
from pages.OrangeHrmPage import OrangeHrmPage
from pages.myInfoPage import MyInfoPage


@pytest.mark.usefixtures("before_method")
class TestBase:

    @pytest.fixture(autouse="true")
    def class_objects(self):
        self.myInfoPage_obj = MyInfoPage(self.driver)
        self.orangeHrm_obj = OrangeHrmPage(self.driver)