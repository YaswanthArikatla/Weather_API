# <a href="#">Weather API</a>

Weather API using Django

Technologies used: Django, django-rest-framework

IDE: VS-Code

### Project Description :
In this assignment, you will need to build a set of APIs for a weather application.
We would require you to develop the following RESTful APIs using Django Rest
Framework / Flask / Node JS.
1. Login API
2. Logout API
3. Get Weather Information API
. This API should return Weather information of 30 cities in JSON format.

### Login API
 POST http://127.0.0.1:8000/rest-auth/login/ in the body paste the following credentials:<br>
 "username":"test", "password":"admin@123"<br>
 you will see the token and copy the token
 
 ### Logout API
 POST http://127.0.0.1:8000/rest-auth/logout/ in the headers section<br>
 Key : Authorization<br>
 value : Token ```<your key value>```
 
  ### Weather API
 GET http://127.0.0.1:8000/weather/data/ the weather details is display and the ideal page size - 10 items<br>
 GET http://127.0.0.1:8000/weather/data/?page=2 the weather details is displayed<br>
 GET http://127.0.0.1:8000/weather/data/?page=3 the weather details is displayed
 


### credentials


Test user <br>
username : test<br>
password : admin@123


