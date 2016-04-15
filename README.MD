# Descrption:
This repository contanins a Restful service to handle the Fibonacci calculation. It also contains the unite test scripts, Jmeter performance test case, and manually function test methods.
The Product Specification.docx charify how to handle it as a product and to grantee the product quality from process and tools.


[![Build Status](https://travis-ci.org/i070595/emc2.svg?branch=master)](https://travis-ci.org/i070595/emc2)

## **Prepare**
     #~ pip install -r requirements.txt
     #~ sudo apt-get install jmeter


## **Testing**

### Performance test:
Fibonacci Service is

Open Jmeter case fibService.jmx and start performance test. it will simulate 50 customer requests fibService in 30 seconds.

### Unit Test:
    python manage.py test
result:


### Function test:
* pip install httpie <br>
http GET http://127.0.0.1:5000/api/v1.0/fib/10 <br>
http GET http://127.0.0.1:5000/api/v1.0/fib/100 <br>
http GET http://127.0.0.1:5000/api/v1.0/fib/asdf <br>
http GET http://127.0.0.1:5000/api/v1.0/fib/-10 <br>
http GET http://127.0.0.1:5000/api/v1.0/fib/$#@ <br>

* we can also use Chrome Postman to do function test.
* About the Web part, we can use selenium to do a framework for automation testing, but the web developer should provide web control ID in their Web framework.
