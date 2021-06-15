Steps to configure the API Automation Project:

1) Login to bitbucket url 
2) Open the API Automation Project i.e., test_aplha
3) Click Clone and copy the url
4) Switch to Desktop and create a Workspace
5) Enter into the workspace and Open the terminal from here
6) Paste the url and press Enter
7) Enter Password and press Enter. Cloning process will be started and completed
8) Switch into the API Automation Project by entering the command cd AlphaVantageAPIAutomation
9) Switch to develop branch by entering the command as git checkout develop. Develop branch code will be loaded
10) Create a branch in local by entering the command as git branch branchname
11) Switch into the branch by entering the command as git checkout branchname
12) Open the pycharm Editor
13) Go to File > Open, load the project i.e., AlphaVantageAPIAutomation

Steps to configure Python Interpreter and install required packages:
1) Click on Configure Python Interpreter link (or) Go to File > Settings > Project Interpreter, Click Setting icon and after Click Add
2) Go to Virtualenv Environment, Select “New Environment” radio option and Click Ok
3) Virtual Environment will be created. Click Apply and Ok
4) Supporting packages will be installed. Once it is done, Install requirements link will be populated
5) Click on that link and Click Install
6) Packages will be installed and project will be ready to use

To view reports

allure serve <path to the reports folder>

Postman collections


https://www.getpostman.com/collections/4f50115cd594f4d5607b


https://www.getpostman.com/collections/dfed3d0f70c3803ead1c

 

Below are the basic test cases for the given functionality.


Test Case without valid Api Key -> This test case will not have a valid Api Key query param value(WCEOL8WGB2X89QK1TEST), API will throw an Information Message and the same is being asserted in the Tests section. -> Negative Case
Test Case without Api Key -> This test case will not have a Api Key query param value, API will throw an Error Message and the same is being asserted in the Tests section. -> Negative Case
Test Case with valid Api Key -> This test case will have a valid Api Key query param value(WCEOL8WGB2X89QK1), API will accept the key and return a success Note and the same is being asserted in the Tests section. -> Positive Case
Test Case with invalid URL -> This test case will not have a valid URL(http://www.alphavantage.co), API will throw 301 error message the same is being asserted in the Tests section. -> Negative Case






