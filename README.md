# TechAssessment
 
Test Framework for Podium site. 

I wanted to test page functionality, but the assignment was to not submit forms.
So i limited my tests on the page navigation and elements functionality. 
I would however would have liked to test that the Chat functionality worked by starting a chat.

I could not test SQL injection as i cannot submit the form and the site is not using js to validate most of the fields.

**To run the tests.** 
`docker build -t pytest .`


Pytest locally. 
`pytest -s -v tests/ `