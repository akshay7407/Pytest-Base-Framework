from operator import index
import os
import time
from isort import file
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


driver = None
environment =None

# from utilities import read_properties as cp


@pytest.fixture(scope='function', autouse ="true")
def before_method(base_url ,request):
    global  driver 
    browser_name = request.config.getoption("--browser_name")
    environment = request.config.getoption("--environment")
    driver_path = os.path.join(os.getcwd(),"chromedriver.exe")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized") 
        # Set up Chrome WebDriver with version 116 and the specified options
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "IE":
        print("IE driver")
    driver.implicitly_wait(20)
    driver.get(base_url)
    if request.cls is not None:
         request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='class')
def mock_fixture():
    print("Mock")

def pytest_addoption(parser):
    parser.addoption("--browser_name", default="chrome", help="browser name")
    parser.addoption( "--environment",action="store", default="dev",  help="Specify the test environment (dev, staging, production)."
    )

#@pytest.fixture()
def retry(func, retries=5):
    def retry_wrapper(*args, **kwargs):
        attempts = 0
        while attempts < retries:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
                time.sleep(2)
                attempts += 1

    return retry_wrapper

def take_screenshot(name):
     driver.get_screenshot_as_file(name)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            index =file_name.index("test_")
            file_name = file_name[index:]
            file_path = "./reports/"+file_name
            take_screenshot(file_path)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        

@pytest.fixture(scope="session")
def base_url(request):
    environment = request.config.getoption("--environment")
    
    if environment == "dev":
        return "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    elif environment == "staging":
        return "http://staging.example.com"
    elif environment == "production":
        return "http://example.com"
    else:
        raise ValueError(f"Invalid environment: {environment}")
   