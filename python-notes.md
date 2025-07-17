# Contents
- [Xpath Axes](#xpath-axes)
- [Select Class For Dropdowns](#select-class-for-dropdowns)
- [ActionChains Class](#actionchains-class---for-mouse-hover-interactions)
- [Javascript Alert](#javascript-alert)
- [Handle Alerts through Expected Conditions as EC](#handle-alerts-through-expected-conditions-as-ec)
- [Switching to Frames](#switching-to-frames)
- [Window Handles](#Window-handle)
- [Synchronisation Waits](#synchronisation-waits)
- [Cucumber Framework - BDD Framework (Behave)](#cucumber-framework---bdd-framework-behave)
- [API Testing: GET, POST, PUT, PATCH](#api-testing-get-post-put-patch)
- [GIT COMMANDS](#git-commands)
- [SET ENVIRONMENT VARIABLES](#set-environment-variables)
- [Selenium Grid](#selenium-grid)
- [PYTEST](#pytest)
- [SQL](#sql)
- [SOLID Principals](#solid-principals)
- [Python Basics](#python-basics)
- [Python Programs](#python-programs)
- [Playwright Notes](#playwright-notes)

****


- Using *`webdriver_manager`* is the most reliable and recommended approach. It ensures you have the compatible **`chromedriver`** version for your Chrome and avoids issues with multiple versions on your system.
    - pip install --upgrade webdriver-manager`
    - **`driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))`**
- If you're unsure which Chrome version you have, use `google-chrome --version` in your terminal to check.
- Check path for downloaded chromedriver from webdriver manager:
    - **`/home/shubham/.wdm/drivers/..`**

***
- **XPATH**:
    - `//tagname[@attribute='value']`
    - `//input[@id='username']`


- **XPATH by text:**
    - `//tagname[text()='value']`
    - `//span[text()='Admin']`
  

- **XPATH by contains : when xpath is dynamic**

    - `//tagname[contains(text(), 'value')]`
    - `//a[contains(text(),'Books')]`
    - `//a[contains(@id,'face')]`


- **SVG XPATH**
  
  - `//*[local-name()='svg']//*[name()='rect']`
  - `//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-tooltip"
                  "highcharts-color-undefined']//*[name()='text']//*[contains(text(),'Interest')]`

* * *

**Link Text and Partial Link Text:**

- `driver.find_element(By.LINK_TEXT, "Log in")` - take name from DOM

- `driver.find_element(By.PARTIAL_LINK_TEXT,"Log in")` - take name displayed in screen

* * *
## Xpath axes:

- `//td//following::input[1]` - may or may not be child
- `//td//preceding::input[2]` - may or may not be parent
- `//td/parent::input` or `//td/../input`  - directly use /.. for parent
- `//td[@id='']//following-sbiling::input`
- `//td[@id='']//preceding-sbiling::input`
- `//td[@id='']//child::input` or  `//td/input`- directly use / for child
* * *

**CSS Selectors: nth child pending**

- By id - use hash(#)
  - `tagname#id` > `input#username` or `#username`
- By class - use dot(.)
  - `tagname.class` > `input.password` or `.password`
- tag_name\[attribute='value'\]
    - `input[id='username']`
- `td[id='username'] nth-child(2)` or `first-child()` or `last-child()`

* * *
<h2 id="select-class-for-dropdowns">Select Class For Dropdowns:</h2>

[//]: # (## Select Class For Dropdowns: )

* https://www.selenium.dev/documentation/webdriver/support_features/select_lists/*

- `from selenium.webdriver.support.ui import Select`

- `element = driver.find_element("")`

- `select = Select(element)`

- `select.select_by_index(3)`

- `select.deselect_by_all()`\- when multi dropdown options are available - we can deselect them


* * *

## ActionChains Class - for mouse hover interactions:

- `element = driver.find_element("")`
- `action = ActionChains(driver)`
- `action.move_to_element(element).perform()` - moving to element
- `action.context_click(element).peform()` - Right click
- `source = driver.find_element(""), target = driver.find_element("")`
- `action.drag_and_drop(source, target).perform` - Drag and Drop
- `action.double_click(element).perform()` - Double click

* * *

## **Javascript Alert:**

- `alert = Alert (driver)`
- `alert.accept()` - to accept the alert
- `alert.dismiss()` - to dismiss the alert
- `alert.send_keys("")` - to send text to alerts

* * *

## **Handle Alerts through Expected Conditions as EC:**
```python
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
a = wait.until(EC.alert_is_present() # True/False
a.send_keys("")
a.accept()
```
* * *

**Scroll through ActionChains class:**

- `ActionChains(driver).scroll_to_element(element).perform()`

**Scroll through JavaScript executor:**

- Scroll to a specific position: use scrollTo()
    - `element.rect` - check **dimensions** (height, width) and **coordinates** (x,y) of the referenced element
    - `element.location` - provides x and y **coordinates**
    - `driver.execute_script("window.scrollTo(225, 3628);")` - scroll To specific position
    - `driver.execute_script("window.scrollTo(0, 0);")` - scroll To top
- Scroll to a specific element:  scrollIntoView()
    - `driver.execute_script("arguments[0].scrollIntoView();", element)`
- Clicking Elements: Click on an element that's not directly clickable:
    - `driver.execute_script("arguments[0].click();", element)`

* * *

## **Switching to Frames:**

- By Web-Element

    - `web_element = driver.find_element(By.XPATH, "//iframe[@# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")id= 'mce_0_ifr']")`

    - `driver.switch_to.frame(web_element)`

- By Index

    - `driver.switch_to.frame(0)`
- By id or name attribute

    - `driver.switch_to.frame("frame_id")`
- Switch back to main content

    - `driver.switch_to.default_content()`
- child to parent frame

    - `driver.switch_to_parent_frame()`

* * *

### **Window Handle:**
*https://www.selenium.dev/documentation/webdriver/interactions/windows/#windows-and-tabs*

- **Store the ID of the original window**

    - `original_window = driver.current_window_handle`
- **Click the link which opens in a new window**

    - `driver.find_element(By.XPATH, "(//div[@id='new_window']").click()`
- **Wait for the new window or tab**

    - `wait.until(EC.number_of_windows_to_be(2))`

- **Loop through until we find a new window handle**

```python
for child_window in driver.window_handles:
    if child_window != original_window:
        driver.switch_to.window(child_window)
        break
```
**OR write below line of code, it is in list comprehension way:**
```python
[child_window for child_window in driver.window_handles if child_window != original_window][0]:
driver.switch_to.window(child_window)

or

[driver.switch_to.window(child_window) for child_window in driver.window_handles if child_window != original_window][0]
``` 
- **Wait for the new tab to finish loading content**

    - `wait.until(EC.title_is("DEMOQA"))`
- **Switched back to main window**

    - `driver.switch_to.window(original_window)`
- **Get window size : Access each dimension individually**

    - `width = driver.get_window_size().get("width")`

    - `height = driver.get_window_size().get("height")`

- **Set window size: Restores the window and sets the window size.**

    - `driver.set_window_size(1024, 768)`
- **Get window position : Access each dimension individually**

    - `x = driver.get_window_position().get('x')`

    - `y = driver.get_window_position().get('y')`

- **Set window position : Move the window to the top left of the primary monitor**

    - `driver.set_window_position(0, 0)`
- **Fullscreen window**

    - `driver.fullscreen_window()`
- **Save Screenhot**

    - `driver.save_screenshot('./image.png')`
- **TakeElementScreenshot**

    - `ele = driver.find_element(By.CSS_SELECTOR, 'h1')`

      `ele.screenshot('./image.png')`


* * *

### **Synchronisation Waits:**

- **Implicit Waits**: An implicit wait value can be set either with the timeouts capability in the browser options, or with a driver method

  *https://www.selenium.dev/documentation/webdriver/drivers/options/#timeouts*

    - `options = webdriver.ChromeOptions()`  
      `options.timeouts = { 'implicit': 5000 }`  
      `driver = webdriver.Chrome(options=options)`

    - `driver.implicitly_wait(2)`

- **Explicit Wait:** 
*https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html*

    - `from selenium.webdriver.support import expected_conditions as EC`
    - `wait= WebDriverWait(driver, 10)`
- Passing Locator:

    - `locator = (By.NAME, "username")`
    - `wait.until(EC.visibility_of_element_located(locator)).send_keys("Admin")`
- Passing Web Element:

    - `element = driver.find_element(By.NAME, "username")`
    - `wait.until(EC.visibility_of(driver.find_element(locator[0],locator[1]))).send_keys("Admin")`
    - `# wait.until(EC.visibility_of(element))`
- *https://www.selenium.dev/documentation/webdriver/waits/*

- `errors = [NoSuchElementException, ElementNotInteractableException]`

- `wait = WebDriverWait(driver, 20, poll_frequency=.2, ignored_exceptions=errors)`


* * *

**Framework:**
```python
@pytest.mark.regression
@pytest.mark.login
def test_select_city(setup):
    pass

- pytest -m "not smoke" test_new.py  # run only smoke cases
- pytest -m "regression and login" test_new.py - test cases with both markers are executed
- pytest -m "regression or login" test_new.py - both regression and login cases will be executed
```
* * *

### **Allure Installation:** 
*https://allurereport.org/docs/install/*

- Download allure > Uncompressed the archive into an installation directory of your choice.

- Add allure's /bin path to environment variables according to Windows system but in Linux add it in permanent PATH, so that we can execute allure from anywhere

    - `nano ~/.bashrc` - edit `.bashrc` file and add path or directly run below command:

    - `export PATH=$PATH:/home/shubham/Shubham_QA/drivers/allure-2.22.0/bin`

    - `PATH="$PATH:$HOME/bin:$ALLURE_HOME"` - update PATH as well

    - `source ~/.bashrc` - refresh the `.bashrc` file

    - `echo $PATH` - print the paths

**OR if above steps won't work try below steps:**

- Create a Correct Symlink
```
- sudo ln -s /home/shubham/Shubham_QA/drivers/allure-2.22.0/bin/allure /usr/bin/allure`
```
- Verify Symlink
```
- ls -l /usr/bin/allure - to list symlink
- sudo rm /usr/bin/allure - to remove symlink
```
- Install below packages for allure
```
- allure-pytest
- allure-python-commons
```
- Commands to run allure
```
- pytest --alluredir=reports test2.py
- allure serve reports  - Run command in directory under which reports are generated
```
- Attach screenshot to allure
```
- allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
- request.node.name` - is used to fetch current test case name
```
* * *
### **Parameterization in pytest:**
```python
@pytest.mark.parametrize(argnames, argvalues)

Sample Example:
@pytest.mark.parametrize("input,expected", [(2, 4), (3, 9), (4, 16)])
def test_square(input, expected):
    assert input ** 2 == expected
```
* * *
```python
@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "admin123"), # Valid credentials
        ("invalid_user", "admin123"), # Invalid username
        ("Admin", "wrongpassword"), # Invalid password
        ("", ""), # Empty credentials
    ]
)

def test_login(params, username, password):
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(username)
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
```
* * *
### **Reading data from yaml file:**
```
- pip install pyyaml
```

- **Create config.yaml file in the project directory and add below data:**
```YAML
url: https://opensource-demo.orangehrmlive.com/
username: Admin
password: admin123
```

**Create separate fixture in conftest file for handling **YAML** file:**
```python
@pytest.fixture(scope="session")
def config_data():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file) # Returns the content as a dictionary

def test_example(params, config_data):
    # Use data from the YAML configuration
    url = config_data["url"]
    username = config_data["username"]
    password = config_data["password"]
    driver.get(url)
    time.sleep(2)
```
### **For JSON - add config.json file with below syntax:**
```json
{
  "url": "https://opensource-demo.orangehrmlive.com/",
  "username": "Admin",
  "password": "admin123"
}
```
 ### **JSON file handling function:**
 ```python
def config_data():
    with open("config.json", "r") as file:
        return json.load(file) # Returns the content as a dictionary
```


### Pytest:
- Hard Assertions: if hard assertion fails, remaining code fails to execute
- Soft Assertions: if soft assertion fails, remaining code keeps on executing

To use soft assertions in pytest, need to install below pkg
- pip install softest and use *(softest.TestCase)* in class_name 
- usage: *soft_assert(assertTrue, actual, value)*
- *assert_all()* is used to fail the test case if soft assertions are failed but keep on executing the test cases.

# Pytest Notes

- Pytest is a testing framework for Python, allowing you to write simple and scalable test cases.

1. **Installing Pytest**  
   Install pytest using pip:
   ```bash
   pip install pytest
   ```

2. **Basic Test Case**  
   Write a simple test function:
   ```python
   def test_addition():
       assert 1 + 1 == 2
   ```

3. **Running Tests**  
   Run tests in the current directory:
   ```bash
   pytest
   ```
   Run a specific test file:
   ```bash
   pytest test_file.py
   ```

4. **Using Pytest Markers**  
   ```python
   import pytest
   
   @pytest.mark.slow
   def test_slow_function():
       assert sum(range(100000)) == 4999950000
   ```
   Run tests with a specific marker:
   ```bash
   pytest -m slow
   ```

5. **Fixtures**  
   ```python
   import pytest
   
   @pytest.fixture
    def sample_data():
       return [1, 2, 3, 4, 5]
   
    def test_length(sample_data):
       assert len(sample_data) == 5
   ```

6. **Parametrize Tests**  
   ```python
   import pytest
   
   @pytest.mark.parametrize("num, square", [(2, 4), (3, 9), (4, 16)])
   def test_square(num, square):
       assert num ** 2 == square
   ```

7. **Skipping Tests**  
   ```python
   import pytest
   
   @pytest.mark.skip(reason="Skipping this test")
   def test_skipped():
       assert False
   ```

8. **Xfail Tests**  
   ```python
   import pytest
   
   @pytest.mark.xfail
   def test_expected_failure():
       assert 1 == 2
   ```

9. **Capturing Logs**  
   ```python
   import logging
   import pytest
   
   def test_logging(caplog):
       logging.warning("This is a warning!")
       assert "warning" in caplog.text
   ```

10. **Generating Reports**  
    Generate an HTML report:
    ```bash
    pytest --html=report.html
    ```

These notes cover basic and advanced pytest features to help write better test cases.


****

## Common Mistakes:

- Scan incorrect imports 
- __init__.py files are not placed at folder structure

***

### SQL:

# SQL Notes and Queries

- SQL (Structured Query Language) is used to interact with relational databases.

## 1. **Basic SQL Commands**
### Create a Database
```sql
CREATE DATABASE mydatabase;
```
### Use a Database
```sql
USE mydatabase;
```
### Create a Table
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50)
);
```
### Insert Data
```sql
INSERT INTO employees (id, name, age, department) 
VALUES (1, 'John Doe', 30, 'HR');
```
### Select Data
```sql
SELECT * FROM employees;
```
### Update Data
```sql
UPDATE employees SET age = 31 WHERE id = 1;
```
### Delete Data
```sql
DELETE FROM employees WHERE id = 1;
```

## 2. **DML (Data Manipulation Language)**
- `INSERT`, `UPDATE`, `DELETE`, `SELECT` are DML commands used for modifying data.

## 3. **DDL (Data Definition Language)**
- `CREATE`, `ALTER`, `DROP`, `TRUNCATE` are used for defining and modifying database structures.

## 4. **Joins & Subqueries**
### INNER JOIN
```sql
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department = departments.id;
```
### Subquery Example
```sql
SELECT name FROM employees 
WHERE age = (SELECT MAX(age) FROM employees);
```

## 5. **Functions and Operators**
### Aggregate Functions
```sql
SELECT COUNT(*) FROM employees;
SELECT AVG(age) FROM employees;
```
### String Functions
```sql
SELECT UPPER(name) FROM employees;
SELECT LENGTH(name) FROM employees;
```
### Mathematical Operators
```sql
SELECT age + 5 FROM employees;
SELECT age * 2 FROM employees;
```

These queries and notes provide an overview of fundamental SQL concepts and commands.


## Python Basics:


Installing Python and Selenium

Installing Python:

Windows : http://python.org/download/.

• Make sure you note Python Installation path in your machine.
It would be like below
logged in
• Set Python home in System Variables
• Check if Python is Successfully Installed
python --version

==========================================================================================================
## Class name
The class name should start with “Test”

## File name
File name in the suite should start or end with “test”. So the wildcard for this name is “test_*.py” or “*_test.py”

## Method or function name
Every function and method that is supposed to test something should have a name that starts with “test”

Example of the suite is:

test_for_login/
	test_signup.py
	login_test.py

test_for_checkout/
	test_cart.py
	test_form.py
	
===============================================================================================================================	
## What is PIP?
pip is the standard package manager for Python. It allows you to install and
manage additional packages that are not part of the Python standard library.
Java -
Selenium installing instructions official link
https://pypi.org/project/selenium/
• pip install selenium

• How to Verify if Package is installed
pip show <packageName»

4.pip install -U selenium
The optional –U flag will upgrade the existing version of the installed package

=====================================================================================================
## run the test case from the cmd
pytest -vs testCases\test_login.py -p no:logging

# How to create virtual environment?

- **Pre-requisites:**
    Python > 3.9, 
    PyCharm Community Edition 2021.3.2

Use Git Bash here on the project location
- python -m venv .env
- source .env/Scripts/activate (for windows)
- pip install -r requirements.txt


## pytest -vs --alluredir=allure-report/  testCases\*.py -p no:logging 
- for the run the test case with the log
- pytest -p no:logging


## run the test cases in the parellal
- install the pakage name ----pytest-xdist:run test cases in the parell mode.

## pytest -vs -n=2 testCases\test_login.py -p no:logging
- here n=2 for the number of the test cases for the run

## To run specific test case use -k flag
e.g py.test -k testCaseName 

## To run specifig mark test cases use -m as mark and -s for logs
py.test -m smoke 

## To Skip test case 
@pytest.mark.skip

## To generate HTML report in CMD 
py.test test.py --html=report.html


## Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#Method name should have sense
## -k stands for method names execution, -s logs in out put  -v stands for more info metadata
#you can run specific file with py.test <filename>
## you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixt
#fixture and make it available to all test cases (fixture name into parameters of method)
## datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end



## @staticmethod is used to call method from  anytwhere using classname
class testExcel
  @staticmethod
    def getTestData(test_case_name):
        Dict = {}
        book = openpyxl.load_workbook("D:\\PythonSelFramework\\PythonExcel.xlsx")
        sheet = book.active
        for i in range(1, sheet.max_row + 1):  # to get rows
            if sheet.cell(row=i, column=1).value == "testcase1":
                for j in range(1, sheet.max_column + 1):
                    # print(sheet.cell(row=i, column=j).value)
                    # store excel data into dict variable in json format
                    Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
        return[Dict]
	
to call it in method :
   testExcel.getTestData("testcase1")	

====================================================================================================
## genration of the python report 
- step 1- pip install allure-pytest
- step 2=allure generate
- step 3=pytest --alluredir=allure-report/     ---------------->this genrated the one folder as allure report in working dir.
- step 4=allure serve allure-report/               ----------------->this is publish the report to local server.

=====================================================================================================

### **Inheritance:**
#### Types - Single, Multiple, Multilevel, Hierarchical, and Hybrid
- MRO (Method Resolution Order) in case of  Multiple Inheritance
  - classname.mro()  # print(Employee.mro())

### **Polymorphism:**

#### **Overrding: Complie time polymorphism:**
- Override - parent class methods in child class, 
- print() is overridden by build-in function called __str__
- len() is overridden by __len__ function, like wise many more...

#### **Operator overloading: Run time polymorphism**:
- Like multiplication operator
- 10+20 , "hello"+"world", [1, 2]+[3, 4]=[1,2,3,4] , so each plus performs different operations according to datatype

#### **Method overloading: Run time polymorphism:**
- Needs to pass values at run time for example in case of add method

### **Encapsulation:**
- Binding everything in one unit. Class is best example as it binds methods, variables in one unit
- making variables private by __(double underscore) in-front of them so that can not be accessible outside the class

### **Abstraction:**
- python by default does not support abstraction, need to import ABC module for that
- from abc import ABC, abstractmethod
- An abstract method is a method that has a declaration but does not have an implementation.
- one methods needs to be abstract in abstract class
- if you inherit abstract class, you need to implement all abstract methods in your class

****
### **Set Datatype:**
```python
- Using curly braces **“{“ and “}”**
- Using set() method, set([iterabl]),  s = set(('1', '2', '3',(3,4)))
- Elements in a set in Python are immutable but a set, as a whole, is mutable.
- A Python set can’t contain duplicate elements.

- Adding items to set:
  - Using the add() method : allows to add only a single element to the set.
  - s.add(1)
  - Using the update() method : allows to add two or more elements to the set.
  - s = {3, 4} --->> s.update({1, 2, 7, 9}) --->> {1, 2, 3, 4, 7, 9}

- Removing Items from set:
  - s.remove('abc'), s.remove(1)
-  Using the clear() method: remove all elements from the set
  - s.clear()
- Using the pop() method : removes last element from the set
  - s.pop()
```
****
### Generators:

- Special type of function that returns an iterator object
- Instead of using return,  use yield to produce a series of results
- When called, this function doesn’t return a single value; instead, it returns a generator object that supports the iterator protocol
- allows function to generate values and pause its execution after each yield

```python
def generator(n):
    for val in range(n):
        yield val
d= 5  
for val in generator(d):
    print(val)
    
# output -->> 0 1 2 3 4
```
****
### Python Decorators:
- decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.
- The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.


****
## SOLID Principals:
Five principals of Object-Oriented class designs to make code more readable, maintainable, scalable, robust.

Helps in reducing tight coupling means group of classes are highly dependent on one another
### Single responsibility: 
- every class should have single job/responsibility/purpose
### Open/closed: 
- Software entities (classes, modules, functions, etc.) should be open for extension, but closed \
    for modification which means you should be able to extend a class behavior, without modifying it.
### Liskov's substitution: 
- objects of a superclass should be replaceable/substitutable with objects of its subclasses without affecting the correctness of the program. 
### Interface segregation: 
- split interface into smaller and specific ones 
### Dependency Inversion: 
- high level modules should not depend on low level modules, both should depend upon abstractions.

****

## TOPICS:
- Design Patterns - Singleton, POM

===========================================================================================================

## Selenium - webdriver methods in pytest :

1. `get(url)`: Loads a web page specified by the given URL.
2. `current_url`: Returns the URL of the current web page.
3. `title`: Returns the title of the current web page.
4. `find_element(by, value)`: Finds and returns a web element based on the specified locator strategy (e.g., "id", "name", "xpath", "css_selector") and value.
5. `find_elements(by, value)`: Finds and returns a list of web elements based on the specified locator strategy and value.
6. `send_keys(*value)`: Simulates typing into a web element or a text field.
7. `click()`: Clicks on a web element.
8. `clear()`: Clears the contents of a text field or an input element.
9. `submit()`: Submits a form element.
10. `get_attribute(name)`: Retrieves the value of the specified attribute of a web element.
11. `text`: Retrieves the visible text of a web element.
12. `is_displayed()`: Checks if a web element is visible on the web page.
13. `is_enabled()`: Checks if a web element is enabled.
14. `is_selected()`: Checks if a web element is selected (e.g., checkbox, radio button).
15. `get_cookies()`: Returns all cookies of the current session.
16. `add_cookie(cookie_dict)`: Adds a cookie to the current session.
17. `delete_cookie(name)`: Deletes a cookie by name.
18. `delete_all_cookies()`: Deletes all cookies of the current session.
19. `execute_script(script, *args)`: Executes JavaScript code on the current web page.
20. `switch_to.frame(frame_reference)`: Switches the focus to the specified frame on the web page.
21. `switch_to.default_content()`: Switches the focus back to the default content (main frame) from a nested frame.
22. `switch_to.parent_frame()`: Switches the focus to the parent frame from a nested frame.
23. `switch_to.alert`: Switches the focus to an alert dialog.
24. `switch_to.window(window_name)`: Switches the focus to a different browser window or tab.
25. `back()`: Navigates back to the previous page.
26. `forward()`: Navigates forward to the next page.
27. `refresh()`: Refreshes the current page.
28. `close()`: Closes the current window or tab.
29. `quit()`: Quits the WebDriver instance and closes all windows or tabs.
30. `maximize_window()`: Maximizes the current window.
31. `set_window_size(width, height)`: Sets the size of the current window.
32. `get_screenshot_as_file(filename)`: Takes a screenshot and saves it to the specified file.
33. `get_screenshot_as_png()`: Takes a screenshot and returns it as a PNG image.
34. `get_screenshot_as_base64()`: Takes a screenshot and returns it as a base64 encoded string.
35. `page_source`: Returns the source code of the current web page.

These methods cover a wide range of actions and interactions with web elements and the browser. Remember to import the necessary modules and instantiate the WebDriver object before using these methods in your pytest-selenium tests.



## Access Modifiers:
Python doesn't have strict access modifiers like some other languages (e.g., public, private, protected). However, it uses naming conventions to indicate the visibility of attributes and methods.

### Public: No special symbol. Accessible from anywhere.
Protected: Use a single underscore _ prefix. Suggests that an attribute or method should not be accessed directly from outside the class, but it's not enforced.

### Private: Use a double underscore __ prefix. The attribute or method name gets name-mangled to include the class name, making it more difficult to accidentally override in subclasses.

- class MyClass:
    def __init__(self):
        self.public_var = 10       # Public attribute
        self._protected_var = 20   # Protected attribute
        self.__private_var = 30    # Private attribute

    def public_method(self):
        pass  # Public method

    def _protected_method(self):
        pass  # Protected method

    def __private_method(self):
        pass  # Private method

## Abstraction : 

Abstract Base Classes (ABCs):
Python provides a module named abc which allows you to create abstract base classes. These classes can have abstract methods that must be overridden by subclasses.

In this example, the Shape class is defined as an abstract base class using the ABC metaclass. The @abstractmethod decorator ensures that any concrete subclass of Shape must implement the area() method.

## from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2

==================================================================================================================

# Python Programs

- Here are some commonly asked Python coding interview questions along with brief descriptions:

1. **Reverse a String**  
   Write a Python function to reverse a given string.

   ```python
   def reverse_string(s):
       return s[::-1]
   
   print(reverse_string("hello"))  # Output: "olleh"
   ```

2. **Find the Factorial of a Number**  
   Write a function to compute the factorial of a number using recursion.

   ```python
   def factorial(n):
       if n == 0:
           return 1
       return n * factorial(n - 1)
   
   print(factorial(5))  # Output: 120
   ```

3. **Check if a Number is Prime**  
   Write a function to check whether a number is a prime number.

   ```python
   def is_prime(n):
       if n <= 1:
           return False
       for i in range(2, n):
           if n % i == 0:
               return False
       return True
   
   # Test the function with some numbers
   print(is_prime(29))  # Output: True
   print(is_prime(30))  # Output: False
   ```

4. **Find the Largest Element in a List**  
   Write a Python program to find the largest element in a list.

   ```python
   def find_max(lst):
       return max(lst)
   
   print(find_max([10, 25, 3, 98, 56]))  # Output: 98
   ```

5. **Fibonacci Sequence**  
   Write a Python function to generate the Fibonacci sequence up to `n` terms.

   ```python
   def fibonacci(n):
       a, b = 0, 1
       result = []
       for _ in range(n):
           result.append(a)
           a, b = b, a + b
       return result
   
   print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
   ```

6. **Check if a String is a Palindrome**  
   Write a Python function to check whether a string is a palindrome or not.

   ```python
   def is_palindrome(s):
       return s == s[::-1]
   
   print(is_palindrome("racecar"))  # Output: True
   ```

7. **Remove Duplicates from a List**  
   Write a Python program to remove duplicates from a list.

   ```python
   def remove_duplicates(lst):
       return list(set(lst))
   
   print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
   ```

8. **Find the Second Largest Number in a List**  
   Write a Python program to find the second largest number in a list.

   ```python
   def second_largest(lst):
       unique_lst = list(set(lst))
       unique_lst.sort()
       return unique_lst[-2]
   
   print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
   ```

9. **Merge Two Sorted Lists**  
   Write a Python function to merge two sorted lists into a single sorted list.

   ```python
   def merge_sorted_lists(list1, list2):
       return sorted(list1 + list2)
   
   print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
   ```

10. **Find the GCD of Two Numbers**  
    Write a Python program to find the greatest common divisor (GCD) of two numbers.

    ```python
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    print(gcd(48, 18))  # Output: 6
    ```

11. **Find the Smallest Number in a List**  
    ```python
    def find_smallest(lst):
        if not lst:
            raise ValueError("List cannot be empty")
        
        smallest = lst[0]
        for num in lst[1:]:
            if num < smallest:
                smallest = num
        
        return smallest
    
    numbers = [15, 10, 24, 76, 23, 12]
    result = find_smallest(numbers)
    print(f"The smallest number is: {result}")
    ```

12. **Find the Maximum Number in a List**  
    ```python
    def find_max(lst):
        if not lst:
            raise ValueError("List cannot be empty")
        
        max_val = lst[0]
        for num in lst[1:]:
            if num > max_val:
                max_val = num
        
        return max_val
    
    numbers = [15, 10, 24, 76, 23, 12]
    result = find_max(numbers)
    print(f"The maximum number is: {result}")
    ```

13. **Find Odd and Even Numbers in a List**  
    ```python
    l = [1, 2, 3, 5, 4, 6, 7]
    even = [x for x in l if x % 2 == 0]
    odd = [x for x in l if x % 2 != 0]
    
    print(even)
    print(odd)
    ```

14. **Find Character Count in a String**  
    ```python
    str = "SHUBHAM"
    d = {}
    
    for i in str:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    print(d)
    ```

15. **Check if Two Strings are Anagrams**  
    ```python
    str1 = 'EARTH'
    str2 = 'HEART'
    
    if sorted(str1) == sorted(str2):
        print("It's an anagram")
    else:
        print("It's not an anagram")
    ```

========================================================================================================

# Playwright Notes

## What is Playwright

Free & open source Framework for web automation testing I Created by Microsoft
Applications - Web browser apps I Mobile web apps I API
Languages - JavaScript, TypeScript, Java, Python, .NET (C#)
Browsers - all modern engines Chromium, WebKit, and Firefox (headless or headed)
OS - Windows, MacOS, Linux I Supports Cl runs
https://playwright.dev/
https://github.com/microsoft/playwright

==========================================================================================================================

### Features of Playwright:


Free I Open Source
Multi-Browser I Multi-Language I Multi-OS
Easy Setup and Configuration
Functional I API I Accessibility testing
Built-in Reporters I Custom Reporters
Cl CD I Docker support
Recording I Debugging I Explore selectors
Parallel testing
auto wait
Built-in assertions I Less Flaky tests
Test retry, logs, screenshots, videos
Multi-tab and multi-window
Frames I Shadow DOM
Emulate mobile devices, geolocations

==============================================================================================================================

### Prerequisites:

Node JS
IDE ( VS Code )
node-v npm -v

==================================================================================================================

### Installation:

### Install using command as npm package::

Step 1 - Create a new folder and open in VS Code
Step 2 - Goto Terminal and run command - npm init playwright@latest
Step 3 - Following will be added
- package.json - node project management file
- playwright.config.js - Configuration file
- tests folder - basic example test
- tests-examples folder - detail@d example tests
- .gitignore - to be used during git commit and push
- playwright.yml - to be used during ci cd pipeline 

Step 4 - Check playwright added - npm playwright -v
Step 5 - Check playwright command options - npx playwright -h

### Using VS Code extension::

step 1 -
Create a new folder and open in VS Code
Step 2 - Goto Extensions section and install Playwright extension from Microsoft
step 3 -
Goto View > Command Palette and type playwright > select install playwright
Step 4 -
Select the browsers and click 0k
step 5
- It will install the libraries and create the project folders

==============================================================================================================================================
## Running Test:


- npx playwright test === runs all tests on all browsers in headless mode
- npx playwright test —workers 3 === runs with 3 workers in parallel
- npx playwright test one.spec.js === runs a specific test file
- npx playwright test one.spec.js two.spec.js === runs the files specified
- npx playwright test one two == runs files that have one or two in the file name
- npx playwright test -g "check title" == runs test with the title
- npx playwright test —project=chromium  === runs on specific browser
- npx playwright test --headed === runs tests in headed mode
- npx playwright test —debug == debug tests
- npx playwright test example.spec.js —debug === debug starting from specific line where test starts


=====================================================================================================================================================



## How to write tests:


- Step 1 - Create a new file under test folder
- Step 2 - Add module 'playwright/test'
const {test, expect}
require() is a node js built-in function used
to load modules present in separate files
Here we are loading test and expect
modules from playwright package
= require ('@playwright/test')
import {test, expect} from '@playwright/test'
Playwright Test provides a test function to declare tests and expect function to write assertions
- Step 3 - Create a test block - test(title, testFunction)

test( 'My First Test',
async ( {page}) => {
await page . goto( 'https : //google.com' )
await expect (page) .toHaveTit1e( 'Google' )

})


- The keyword async before a function makes the function return a promise
- The keyword await before a function makes the function wait for a promise

========================================================================================================	
## 					How to get the page title

consol.log(await page.title());

========================================================================================================
## 					How Get Html text
console.log(await page.locator('div.errortext').textContent());

========================================================================================================
##					 Asseration for text verifcation
await expect(page.locator('div.errortext')).toContainText('Invalid')

========================================================================================================
##				How to get the one element out of multiple webElement
console.log(await page.locator(".card-body a").nth(3).textContent())
console.log(await page.locator(".card-body a").first().textContent())

========================================================================================================		
##			If the api is hit then the following syntex is
await page.waitForLoadState('networkidle');

========================================================================================================
##			If api is not hit then following method is to be used

await Promise.all(
[

           page.waitForNavigation(),
           loginButton.click()   
 ])

=========================================================================================================		
##			DropDown opation selection
const selectionOfType=page.locator('select.form-control');//select type tag name
await selectionOfType.selectOption("teach");//list of option in select tag name "value"

========================================================================================================	
##					For the open the debugg mode
await page.pause();

========================================================================================================
##					Radio button selection
Directly inspect and the select the options
For the apply asseration for the radio button is check or not
expect(locator).last().toBeChecked();
above method used for the verfiaction 
for the get the properties in the boolean format there is another method present
await locator.isChecked();

========================================================================================================
##					ChekBox Selection
Similar method like the Radio button we are able to click that so it will be check
uncheck method is present for the unchecked selected 
Also there is no asseration for the unchecked
For the verifaction of the unchecked there is no method present 
expect(locator.isChecked).toBeFalsy
//toBeFalsy return the false
//toBeTruthy return the true

========================================================================================================
##					Attribute Asserations
for the check the attribute value is present or not 
await expect(locater).toHaveAttribute(“Class”,”Attribute value”)

========================================================================================================			
##			Child windows Handle
For the change the focus of the browser from the main window to child browser
So before click on the child browser link we need to do following things
intialized the browser with the new contex
test('2nd test',async ({browser}) => {
   const context=await browser.newContext();
   const page=await context.newPage();
//before the click we need to do the new season
const [newPage]	=await Promise.all([
	context.waitForEvent(‘page’),
	locator.click(),
])
now for the new  page we are able to handle it

========================================================================================================
##			Codegen tool To recored the test script
npx playwright codegen

========================================================================================================
##				How to generate the traces and the screenShots 
for the log,traces and go to the 
playwright.config.js 
inside the use write the traces and screenshot 
 screenshot:'on',
    trace: 'on',

If we want the traces only on failure 
trace:’retain-on-failure’

========================================================================================================
##				For the verifaction of the webelement or the any 
				      locator is presnet on the screen or not.
expect(await page.locator(css/xpath).isVisible()).toBeTruthy();

========================================================================================================
##				For the navigation of the webPage
page.goBack();
page.goForword();

========================================================================================================
##				For the verifaction webElement is in the visible mode or not
await expect((page.locator("locater")).toBeVisible();

========================================================================================================
##				For the verifaction of the webelement is hidden or not
await expect((page.locator("locater")).toBeHidden();

========================================================================================================
##			How to handle the alert pop up
Whenever the pop up is open then the event is going to occers
for that event write the following syntex for the handle that event'
await page.on('dialog',dialog=>dialog.accept())
above syntex is active when the any event is going to occers

========================================================================================================
##				If you want the webelemnt is hover 
await expect((page.locator("locater")).hover();

========================================================================================================
##				How to handle the frames in the playwright
const framePage=page.frameLoctaor("locator")
framePage.locator("locator:visible").click();
:visible is the way to call the webelement is in the visible mode

========================================================================================================
##				For the api testing
inject the request in the 
const { test, expect,request} = require('@playwright/test');
const token;
request is the libary
const apiContext=await request.newContext();

----------------------------------
const loginResponce=
(method) APIRequestContext.get(url: string, options?: {
    failOnStatusCode?: boolean | undefined;
    headers?: {
        [key: string]: string;
    } | undefined;
    ignoreHTTPSErrors?: boolean | undefined;
    params?: {
        [key: string]: string | number | boolean;
    } | undefined;
    timeout?: number | undefined;
} | undefined): Promise<...>)

---------------------------------
for the verifaction of the status code 
expect(
const loginResponce.ok()
-------------------------------------
const loginResponceJson=loginResponce.json()
 token=loginResponceJson.token;
-----------------------------------------------------

## Half of the part is done then we need to set the token in the application parameter
For the add the token 
page.addinitScript(value=>{

window.localStorge.setItem('token',value//nothing but the agrument value)


},token ///the above one)

========================================================================================================	
##				For the api automation if the more cookies and other things are hit

let webContext;
//webContext is the object stored the all the preloaded cookies
test.beforeAll(async ({browser})=>{

    const context= await browser.newContext();
    const page=await context.newPage();
    await page.goto("https://eagle.creatingwow.in/");
    await page.locator("#Google").click();
    await page.locator("input[type='email']").fill("pruthvirajsing.rajput@infobeans.com")
    const nextButton=page.locator("(//span[@class='VfPpkd-vQzf8d'])[2]");
    await nextButton.click();
    await page.locator("input[type='password']").fill("1Pruthvir@j")
    await nextButton.click();
    console.log(await page.locator("div[style='width:100%']").textContent());


   //make the new instance of the context 
    await context.storageState({path:'state.json'})

//state.json==is the folder to catch the all the json file i.e.cookies etc.
    webContext= await browser.newContext({storageState:'state.json'});
in the newContext --we are able to store the all the api calls
})
test('click on the three dot ',async () => {
//with help of the new webContext start the new page for that instance

    const page=await webContext.newPage();
    await page.pause();
    await page.goto("https://eagle.creatingwow.in/");

});

=======================================================================================================
##				for the debug the api call as well
1.go to the pakage.json
inside the pakage.json---in the scripts 

{
"test": "npx playwright test --headed"

2.ctrl+shift+p
And after that 

3.add the debug point and
debug the npm script

========================================================================================================
##			for the traces 
go to the playwright.config.js
traces:'on'
and after that in the test o/p
we are able to see the zip file
-----https://trace.playwright.dev/
inside this open the traces to see the which the request is going to be hit and what is going to happed in that

========================================================================================================
##				Intercept/alter the network responce
Make it before to hit that webelement --->

for the alter the page api
const fakeRespond=proivde the responce that the dont have the api hit
await page.route("URL",async route=>{

const reponce=await  page.request.featch(route.request())
//this steps for the api testing helper
let body=fakeRespond
route.fulfill({
responce,
body
})
//fullfill-is the method is send the responce send back to the browser


})

========================================================================================================
##				How to block any Network calls
for the block the network call
page.route('**/*.css',route.abort());
for the img route 
page.route('**/*.{jpg,png}',route=>route.abort());

========================================================================================================
##				To print the api log into the o/p
page.on('request',request=>console.log(request.url()));
//for the responce 
page.on('responce',responce=>console.log(responce.url(),responce.status()))

========================================================================================================
##				for the take the screenshot at any line of code
await page.screenshot({path:'screenshot.png'})

----------------------------------------------------------------------
##				for the take the screen shot on the locator
await page.locator('xpath/css').screenshot({path:'name.type'})

========================================================================================================
## To perform the visual testing /it will be check the UI base things
await page.goto("Url");
expect(await page.screenshot()).toMatchSnapshot('name.png');

========================================================================================================


