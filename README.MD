# Overview
This repository contains a Restful service to handle the Fibonacci calculation. It also contains the unite test scripts, Jmeter test script for performance and function test, and other function test methods. About product management, I think that all success is sales success. I clarify how to support sales and improve product from several aspects: market, organization, system landscape, continues delivery and operation. <br>

[![Build Status](https://travis-ci.org/i070595/emc2.svg?branch=master)](https://travis-ci.org/i070595/emc2)

## Market
Provide stable and quality service will be our commitment to customer. The product’s market segment will be University, Research center and calculation service provider. To success setup an echo system is the key to achieve successfully. <br>

## Organization
In order to support the product sales, development and maintenance, setup teams for correspond responsibility will be necessary.<br>
**Customer support team:** Customers message and requirement.<br>
**Development team:** Product bug fixing, new feature development, innovation and deployment interface.<br>
**CD team:** Continues delivery system and testing center.<br>
**DevOps team:** Online system monitor and operation, system deployment and upgrade.<br>

## System landscape
The product development will be considered as Continues delivery mode, and all Dev and QA will work on the same platform and focused on their professional area. Dev and QA will not consider about environment, infrastructure and deployment, they will only consider about development requirements and deployment interface.<br><br>
The product landscape will considered as Micro-service structure, packaged in Docker and deployed on Mesos.<br>

**Product Development**<br>

System development team will focus on the Fibonacci number service development and customer requirements. The system will be development under TDD principle, all feature should be defined as testable. Unit test will cover every code layers, and all service must be stateless.<br>

* **Fibonacci service development**<br>
Developer and QA focus on this area to continues improve service quality, optimize response speed and system perforce<br>
<br>
* **Testing**<br>
    **Unit testing:** Dev will provide Unit testing code once their class was finished.<br>
    **Function testing:** QA can book environment from CD center and do function testing rely on test case, every function or feature   cutoff, the test case and testing should be finished.<br>
    **Integration testing:** All QA should provide e2e test case and upload to Testlink which used to manage test case. <br>
    **Regression testing:** it covered by automation test scripts. When the system grow up, no one can grantee the quality regression                         without automation testing. All QA will delivery test script on function and e2e scenario. Developers                             should delivery unit test case when their features were finished.<br>
    **Performance testing:** it will be covered by performance testing tools, like Jmeter.<br>
    **Deployment and upgrade testing:** deployment and upgrade is not part of development but it is integration the whole production                                      to success. Without pay attention to this part, even we pass in every testing phase, we may                                       have high probability to fail. I suggest to divide this part to two phase: binary deployment                                      and database data upgrade.<br><br>
* **Testing tools:** <br>
    * Jmeter for backend service testing and performance testing. <br>
    * Selenium for front service testing.<br>
    * Unit test tools for unit testing.<br>
    * Python to meet daily testing tools requirement.<br>
    * All automation testing script will run in the Testing Center, all the logs will be collected and analysis. The result will send   to    stakeholders.<br>


