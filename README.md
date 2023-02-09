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

Step 3. Connect the 2 services
Start both the containers.
Create a new Python program which takes city as user input, sends request to first service.
Then parses the zip code from the response returned. Then use it to send request to second service.
