all::help

help:	# to get all commands        
	@grep '^[^#[:space:]].*:' Makefile 

test-login-docker:	# run login test on docker (chrome is headless)
	@echo "run login test with docker"
	chmod +x utils.sh
	./utils.sh uncomment headless
	docker-compose up -d
	docker-compose exec robot robot --listener Resources/CustomListener.py TestCases/TC1_LOGIN.robot
	./utils.sh open_results

test-register-docker:	# run register test on docker (chrome is headless)
	@echo "run register test with docker"
	chmod +x utils.sh
	./utils.sh uncomment headless
	docker-compose up -d
	docker-compose exec robot robot --listener Resources/CustomListener.py TestCases/TC2_REGISTER.robot
	./utils.sh open_results

test-login-local:	# run login test on local
	@echo "run login test on local"
	chmod +x utils.sh
	./utils.sh comment headless
	pip3 install -r requirements.txt
	robot --listener Resources/CustomListener.py TestCases/TC1_LOGIN.robot

test-login-register:	# run register test on local
	@echo "run register test on local"
	chmod +x utils.sh
	./utils.sh comment headless
	pip3 install -r requirements.txt
	robot --listener Resources/CustomListener.py TestCases/TC2_REGISTER.robot