***Settings***
Library  SeleniumLibrary
Library  ../Resources/Locators.py
Library  ../Resources/CustomLib.py
Variables  ../Resources/Elements.py
Test Teardown  Close Browser window 

***Variables***
${url}  http://demowebshop.tricentis.com/
${valid_email}  randyorton@gmail.com
${valid_password}  test2020
${success_msg}  Welcome to our store  
${unsuccess_msg}  The credentials provided are incorrect
${invalid_email}  someone@gmail.com
${invalid_password}  invalid

***Test Cases***

TestCase1: Login Valid Credentials
    [Documentation]  Verify valid login to demo web shop
    [Tags]  integration
        Start Browser Window    ${url}
        Click Login Link
        Input Email  ${valid_email}
        Input Password  ${valid_password}
        Click Login Button
        Welcome Message Validation
        
TestCase2: Login Invalid Credentials
    [Documentation]  Verify invalid login to demo web shop
    [Tags]  integration
        Start Browser Window    ${url}
        Click Login Link
        Input Email     ${invalid_email}
        Input Password  ${invalid_password}
        Click Login Button
        Unsuccessful Login Warning

***Keywords***
Click Login Link
    page should contain link  ${LoginLink_Loc}
    click link  ${LoginLink_Loc}

Input Email
    [Arguments]  ${email}
    element should be visible  ${Email_Loc}
    element should be enabled  ${Email_Loc}
    input text  ${Email_Loc}  ${email}

Input Password  
    [Arguments]  ${password}
    element should be visible  ${Password_Loc}
    element should be enabled   ${Password_Loc}
    input text  ${Password_Loc}  ${password}

Click Login Button
    page should contain button  ${LoginButton_Loc}
    element should be enabled   ${LoginButton_Loc}
    click button                ${LoginButton_Loc}

Welcome Message Validation
    ${recieved_msg}  get text  ${WelcomeMsg_Loc}
    element should contain  ${WelcomeMsg_Loc}  ${success_msg}
    should be equal as strings  ${success_msg}  ${recieved_msg}
    log to console  ${recieved_msg}

Unsuccessful Login Warning
    ${recieved_msg}  get text  ${InvalidMsg_Loc}
    element should contain  ${InvalidMsg_Loc}  ${unsuccess_msg}
    should be equal as strings  ${unsuccess_msg}  ${recieved_msg}
    log to console  ${recieved_msg}

Close Browser window
    close browser
