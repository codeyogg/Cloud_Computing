# Cloud_Computing



Cloud assignment 


Step 1. Build a server
Both services are going to be HTTP servers. So first learn x
* For Service 1, the param is city, response will be zip code
* For Service 2, the param is zip code, response will be weather 

Use Flask for creating the server -
https://www.geeksforgeeks.org/multi-value-query-parameters-with-flask/


Can be used for service 1 - pyzipcode · PyPI

Service 2 is more involved. Need to use some 3rd party weather library.
Eg. https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

Forget about containers for now. Simply build and test both the services as simple Python programs.


Step 2. Containerize the services

How to Dockerize a Flask Application

You should be able to run both the services as docker containers and test them using curl.

Commands used:
-for Building the dockefile:

docker build dockerfile -t s1 

-for mapping the ports of service1 and service2:

docker run  -p 0.0.0.0:5000:5000 s1
docker run  -p 0.0.0.0:5001:5000 s2 &

-for checking the running docker processes:
docker ps



Step 3.

Connect the 2 services
-we use the command ro get the ip of both the services service :
docker inspect d | grep IPAdd
response:
"SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.2",
                    "IPAddress": "172.17.0.2",
-sh into the first service and make the connection:
 docker exec -it c sh 
 
 
 -connectivity setup and service response:
 wget -q -O - 172.17.0.2:5000/weather?zip=95129
 Temperature (in kelvin unit) = 280.82
 atmospheric pressure (in hPa unit) = 1024
 humidity (in percentage) = 82
 description = mist172.17.0.3 - - [09/Feb/2023 22:28:25] "GET /weather?zip=95129 HTTP/1.1" 200 -
 
 wget -q -O - 172.17.0.2:5000/weather?zip=95129
 Temperature (in kelvin unit) = 280.82
 atmospheric pressure (in hPa unit) = 1024
 humidity (in percentage) = 82
 description = mist172.17.0.3 - - [09/Feb/2023 22:29:13] "GET /weather?zip=95129 HTTP/1.1" 200 -


wget -q -O - 172.17.0.2:5000/weather?zip=95012
172.17.0.3 - - [09/Feb/2023 22:29:19] "GET /weather?zip=95012 HTTP/1.1" 200 -
                                                                              Temperature (in kelvin unit) = 280.13
 atmospheric pressure (in hPa unit) = 1024
 humidity (in percentage) = 96
 description = light rain
 
 for connectivity:
 
 docker run --net city-weather-net --name svc1 -p 0.0.0.0:5000:5000 -d s1
 
 docker run --net city-weather-net --name svc2 -p 0.0.0.0:5001:5000 -d s2
 
 
 for testing on curl:
 
 
 
 curl -X GET "http://localhost:5000/zipcode?city=san%20jose"
 
 
 

