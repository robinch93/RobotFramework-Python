docker-compose up -d && \
docker-compose exec robot robot --listener Resources/CustomListener.py TestCases/TC1_LOGIN.robot && \
open -a "Google Chrome" http://localhost:8505/outputs/log.html