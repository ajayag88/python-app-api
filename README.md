# python-app-api
A project or app created for teaching/learning purpose. It is very basic code with bugs with purpose. 

Requirements
1. There are bugs in API code endpoint/bank-1.py. Identify the bugs and fix them
2. Some API's always return code other than 200 OK. Fix them all to return code 200 OK for correct set of inputs
3. Add a new API(DELETE/UPDATE) by name "Account holder email" and let it return always message "Operation Not Permitted" and code "403"

Deploy the app bank-1.py
1. Let there be a log file showing all incoming requests and return code

Test cases
1. Write a test script by name "test-bank-api.py" such that
      a. Call every API - with correct and incorrect inputs. Let each API return 200 and non 200 code
2. Form a dictionary which should give a count of pass(200 OK) and fail(non 200 OK) for a given API.
    Example: login is an API call, and it has 10 pass and 20 fails
      {"login": [{"Pass": 10, "fail": 20}]}

Bonus
1. Make the bank app secure by enforcing the app on HTTPS

