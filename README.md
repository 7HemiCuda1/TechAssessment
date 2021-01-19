# TechAssessment
 
Test Framework for Podium site. 

I wanted to test page functionality, but the assignment was to not submit forms.
So i limited my tests on the page navigation and elements functionality. 
I would however would have liked to test that the Chat functionality worked by starting a chat.

I could not test SQL injection as i cannot submit the form and the site is not using js to validate most of the fields.

**To run the tests.** 
Until I have an image created you will need to build it to run. As soon as it is in good shape i will build and put on Dockerhub.
`docker build -t pytest .`

To make this easier to use i will add a web interface to allow you to select the tests you want to run. Create test sets etc. 

Pytest locally. 
`pytest -s -v -m functionality `