class Locators(object):

    def __init__(self):
        super().__init__()

    def locateLoginLink(self):
        locator = "css:a.ico-login"
        return locator
    
    def locateEmailField(self):
        locator = "id:Email"
        return locator

    def locatePasswordField(self):
        locator = "id:Password"
        return locator

    def locateConfirmPassword(self):
        locator = "id:ConfirmPassword"
        return locator

    def locateRegisterLink(self):
        locator = "css:a.ico-register"
        return locator
    
    def locateFirstName(self):
        locator = "id:FirstName"
        return locator

    def locateLastName(self):
        locator = "id:LastName"
        return locator

    def locateLoginButton(self):
        locator = "css:input.login-button"
        return locator

    def locateRegisterButton(self):
        locator = "id:register-button"
        return locator
    
    def locateWelcomeMsg(self):
        locator = "css:h2.topic-html-content-header"
        return locator
