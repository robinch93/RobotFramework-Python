""" This file contains all the locators used.  """

""" Login Feature """
LoginLink_Loc = 'css:a.ico-login'
Email_Loc = 'id:Email'
Password_Loc = 'id:Password'
ConfirmPass_Loc = 'id:ConfirmPassword'
LoginButton_Loc = 'css:input.login-button'

""" Register Feature """
RegisterLink_Loc = 'css:a.ico-register'
FirstName_Loc = 'id:FirstName'
LastName_Loc = 'id:LastName'
RegisterButton_Loc = 'id:register-button'

WelcomeMsg_Loc = 'css:h2.topic-html-content-header'
InvalidMsg_Loc = 'css:div.message-error>div>ul'
ResgisterMsg_Loc = 'css:div.result'
EmailExist_Loc = 'css:div.message-error'

""" Field Validation Error """
PassError_Loc = 'css:span[for="Password"]'
ConfirmErr_Loc = 'css:span[for="Confirm Password"]'

""" Expected Messages """
Short_Password_Err = 'The password should have at least 6 characters.'
Unmatched_Pass_Err = 'The password and confirmation password do not match.'
Success_Register_Msg =  'Your registration completed'
Email_Exist_Error =     'The specified email already exists'

""" Page Titles """
Home_Page_Title = 'Demo Web Shop'
Register_Page_Title = 'Demo Web Shop. Register'