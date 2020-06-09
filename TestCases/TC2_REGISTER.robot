***Settings***
Library  SeleniumLibrary
Library  BuiltIn
Library  ../Resources/CustomLib.py
Library  ../Resources/Locators.py
Variables  ../Resources/Elements.py

***Variables***
${browser}  firefox
${url}  http://demowebshop.tricentis.com/
${firstname}  john
${lastname}  cena
${gender}  M
${existing_email}  randyorton@gmail.com 


***Test Cases***
TestCase1: Register New User
    [Documentation]  Verify Registration of new user on demo web shop
    [Tags]  integration
    [Setup]         Start Browser Window    ${url}  ${browser} 
        Click Register Link     ${RegisterLink_Loc}
        Select Gender Radiobutton  Gender  ${gender}
        Input First Name            ${FirstName_Loc}        ${firstname}
        Input Last Name             ${LastName_Loc}         ${lastname}
        Input Random Email          ${Email_Loc}            ${firstname}
        Input Random Password       ${Password_Loc}         ${firstname}        ${PassError_Loc}        ${Short_Password_Err}
        Input Confirm Password      ${ConfirmPass_Loc}  ${ConfirmErr_Loc}   ${Unmatched_Pass_Err}
        Click Register Button       ${RegisterButton_Loc}
        Register Page Title         ${Register_Page_Title}
        Success Register Message    ${ResgisterMsg_Loc}     ${success_register_msg}
    [Teardown]        Close Browser Window

TestCase2: Register Existing User
    [Documentation]  Verify Registration of existing user on demo web shop
    [Tags]  integration
    [Setup]         Start Browser Window    ${url}  ${browser}
        Click Register Link     ${RegisterLink_Loc}
        Select Gender Radiobutton  Gender  ${gender}
        Input First Name        ${FirstName_Loc}    ${firstname}
        Input Last Name         ${LastName_Loc}     ${lastname}
        Input Email             ${Email_Loc}        ${existing_email}    
        Input Random Password   ${Password_Loc}     ${firstname}    ${PassError_Loc}    ${Short_Password_Err}
        Input Confirm Password  ${ConfirmPass_Loc}  ${ConfirmErr_Loc}   ${Unmatched_Pass_Err}
        Click Register Button   ${RegisterButton_Loc}
        sleep  3
        Email Exist Error       ${EmailExist_Loc}   ${Email_Exist_Error}     
    [Teardown]        Close Browser Window

***Keywords***



