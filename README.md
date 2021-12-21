# RobotFramework-Python
Implementation of Keyword-Driven Testing using robot framework and by custom python library made using standard robot framework libraries.
The tests were performed on [this](http://demowebshop.tricentis.com/) website.

**Prerequisite**

- [Docker](https://docs.docker.com/get-docker/) 
- `git clone https://github.com/robinch93/RobotFramework-Python.git`

**How To Run**

1. [Login Test](https://github.com/robinch93/RobotFramework-Python/blob/master/TestCases/TC1_LOGIN.robot): </br>
    Run on Docker: `make test-login-docker` </br>
    Run on Local:  `make test-login-local`  </br>

3. [Register Test](https://github.com/robinch93/RobotFramework-Python/blob/master/TestCases/TC2_REGISTER.robot): </br>
    Run on Docker: `make test-register-docker`  </br>
    Run on Local: `make test-register-local`    </br>


NOTE: To get all make commands, run `make all` or `make help`
