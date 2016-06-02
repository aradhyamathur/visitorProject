<h1>Visitor project</h1>

The project aims at providing an API for a sample visitor model.


<h3> Setting up </h3>
 git clone https://github.com/aradhyamathur/visitorProject.git

<h3> Running Project </h3> 
cd pathto/visitorProject
python manage.py runserver


<b>Visitor Project Endpoints</b>

<b> GET Request </b>
**authorisation details to be provided**

url : '/visitor/'

<u> Sample Input </u>
http -a username:password GET  http://127.0.0.1:8000/visitor/ 


<u>Sample Output</u>

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 2,
        "name": "aradhya",
        "email": "a@meee.com",
        "phone_number": "+919015670010"
    },
    {
        "id": 3,
        "name": "xyz",
        "email": "a@a.com",
        "phone_number": "+919012332222"
    }
]

<br>

<b> GET </b> 

url: '/visitor/<id>'

<u> Sample Output  </u>

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "name": "aradhya",
    "email": "a@meee.com",
    "phone_number": "+919015670010"
}



<b> POST Request </b>

url: '/visitor/' arguments to be passed - 
name = 'visitorName'
email = 'visitorEmail'
phone_number = 'visotorPhoneNumber'

**authorisation details to be provided**
<u>Sample Input</u>
http -a username:password POST http://127.0.0.1:8000/visitor/ name='new' phone_number="+919015670010" email='a@a.com'


HTTP/1.0 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Date: Thu, 02 Jun 2016 07:26:58 GMT
Server: WSGIServer/0.1 Python/2.7.6
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "email": "a@a.com", 
    "id": 14, 
    "name": "new", 
    "phone_number": "+919015670010"
}
