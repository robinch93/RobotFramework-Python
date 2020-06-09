# RobotFramework-Python
Implementation of Keyword-Driven Testing using robot framework and by custom python library made using standard robot framework libraries

**Prerequisite**

- Python 
- Robot-Framework Libraries

**BUILD**

1. Creating Python Virtual environment, [PipFile](https://github.com/robinch93/RobotFramework-Python/blob/master/Pipfile)
2. Installing necessary libraries 

Application  [DemoWebShop](http://demowebshop.tricentis.com/) is tested for Login and Registration Features:

- Login Feature: This feature is tested for valid and invalid credentials by writing keywords in the same robot file. 

[TC1_lOGIN.robot](https://github.com/robinch93/RobotFramework-Python/blob/master/TestCases/TC1_LOGIN.robot)

- Registration Feature: This feature is tested for new and existing users by creating a custom python library, by importing standard robot framework libraries like BuiltIn, String, SeleniumLibrary. 

[TC2_REGISTER.robot](https://github.com/robinch93/RobotFramework-Python/blob/master/TestCases/TC2_REGISTER.robot)

[Custum Library](https://github.com/robinch93/RobotFramework-Python/tree/master/Resources/CustomLib.py)


All the required locators are put in separate [Locators](https://github.com/robinch93/RobotFramework-Python/blob/master/Resources/Elements.py) file for easy access. 


