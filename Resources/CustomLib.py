from random import randint

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.String import String
from robot.api.deco import keyword
from robot.api import logger

username = ''
randomPassword = ''

class CustomLib(object):

    def __init__(self):
        self.methodObj = Methods()
        self.built = BuiltIn()
        self.sl = BuiltIn().get_library_instance('SeleniumLibrary')
    
    def _validate_message(self, locator, expectedMsg):
        logger.info("Validating Recieved Message")
        recievedMsg = self.sl.get_text(locator)
        self.built.should_be_equal_as_strings(recievedMsg, expectedMsg)
        logger.info(recievedMsg)

    @keyword("Get Driver Path")
    def get_Chromedriver_Path(self, browser):
        if browser.casefold() == 'chrome'.casefold():
            driver_path = ChromeDriverManager().install()
        elif browser.casefold() == 'firefox'.casefold():
            driver_path = GeckoDriverManager().install()
        elif browser.casefold() == 'ie'.casefold():
            driver_path = IEDriverManager().install()
        
        return(driver_path)
    
    @keyword("Start Browser Window")
    def start_browser_window(self, url, browserName):
        self.sl.open_browser(url, browserName)
        self.sl.maximize_browser_window
    
    @keyword("Click Register Link")
    def click_register_link(self, locator):
        self.sl.page_should_contain_link(locator)
        self.sl.click_link(locator)
    
    @keyword("Select Gender Radiobutton")
    def select_gender_radiobutton(self, name, value):
        self.sl.page_should_contain_radio_button(name)
        self.sl.select_radio_button(name, value)
        self.sl.radio_button_should_be_set_to(name, value)

    @keyword("Input First Name")
    def input_first_name(self, locator, firstname):
        self.sl.element_should_be_visible(locator)
        self.sl.input_text(locator, firstname)

    @keyword("Input Last Name")
    def input_last_name(self, locator, lastname):
        self.sl.element_should_be_visible(locator)
        self.sl.input_text(locator, lastname)

    @keyword("Input Email")
    def input_email(self, locator, email):
        logger.console('Entered Email is : %s' %email)
        self.sl.element_should_be_visible(locator)
        self.sl.input_text(locator, email)
        return email

    @keyword("Input Random Email")
    def input_random_email(self, locator, name):
        randomEmail = self.methodObj.getRandomEmail(name)
        logger.console('Random Generated Email is : %s' %randomEmail)
        self.sl.element_should_be_visible(locator)
        self.sl.input_text(locator, randomEmail)
        return randomEmail
    
    @keyword("Input Random Password")
    def input_random_password(self, locator, name, errorLocator, expectedErrorMsg):
        global randomPassword 
        randomPassword = self.methodObj.getRandomPassword(name)
        logger.console('Random Generated Password is : %s' %randomPassword)
        self.sl.element_should_be_visible(locator)
        self.sl.input_text(locator, randomPassword)
        if(len(randomPassword) < 6):
            self._validate_message(errorLocator, expectedErrorMsg)
        return randomPassword

    @keyword("Input Confirm Password")
    def input_confirm_password(self, locator, errorLocator, expectedErrorMsg):
        confirmPassword = randomPassword
        self.sl.element_should_be_visible(locator)
        self.sl.input_text(locator, confirmPassword)
        if(confirmPassword != randomPassword):
            self._validate_message(errorLocator, expectedErrorMsg)

    @keyword("Click Register Button")
    def click_register_button(self, locator):
        self.sl.page_should_contain_button(locator)
        self.sl.element_should_be_enabled(locator)
        self.sl.click_button(locator)

    @keyword("Register Page Title")
    def register_page_title(self, registerPageTitle):
        self.sl.get_title()
        self.sl.title_should_be(registerPageTitle)
    
    @keyword("Success Register Message")
    def success_register_message(self, locator, expectedMsg):
        self.sl.element_should_be_visible(locator)
        self._validate_message(locator, expectedMsg)

    @keyword("Email Exist Error")
    def email_exist_error(self, locator, expectedMsg):
        self.sl.element_should_be_visible(locator)
        self._validate_message(locator, expectedMsg)

    @keyword("Close Browser Window")
    def close_browser_window(self):
        self.sl.close_browser

class Methods(object):

    randomPart = randint(10,99)

    def __init__(self):
        super().__init__()

    def getRandomEmail(self, name):
        global username
        username = name + str(self.randomPart)
        email = username + '@gmail.com'
        return email

    def getRandomPassword(self, name):
        password = "pass" + name + str(self.randomPart)
        return password