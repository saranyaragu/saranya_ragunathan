Setup Working Environment

Install scoop from www.scoop.sh

Install allure commandline by running the following command:

scoop install allure

git clone
cd to project directory

Install virtualenv:
py -m pip install --user virtualenv

Create a virtual environment:
py -m venv env

Activate your virtual environment:
.\env\Scripts\activate

install pipenv:
pip install -r ./requirements.txt

Run Tests

pytest Tests/test_01.py --alluredir=TestReports/test_case_01 --browser <firefox/remote/chrome_headless>

pytest Tests/test_02.py --alluredir=TestReports/test_case_02 --browser <firefox/remote/chrome_headless>

pytest Tests/test_03.py --alluredir=TestReports/test_case_03 --browser <firefox/remote/chrome_headless>

pytest Tests/test_04.py --alluredir=TestReports/test_case_04 --browser <firefox/remote/chrome_headless>

if no browser was selected then chrome will be used.

Parallel execution using xdist:

pytest Tests/test_02.py -n 5 --alluredir=TestReports/test_case_02 --browser <firefox/remote/chrome_headless>

Run according to tags:
pytest -k "<tag_name>" --browser <firefox/chrome/remote/chrome_headless>

View Test Results
view allure results:
allure serve allure-results


View Help And Custom CLI Options
pytest --help


##########################################################################################################################################

1. What other possible scenario’s would you suggest for testing the Jupiter Toys application?

Answer:

1. Scenario to validate if the user can remove the items from cart and after removing the items  if cart value has been cleared or  not.
2. Scenario to check if the user can modify the quantity in the cart table. Once changed, product price, subtotal & total to be displayed based on the latest changes.
3. Scenario to check if the empty cart is selected, all the items in the cart has to be removed and cart number reset to 0.
4. Scenario to click checkout and proceed to enter delivery & payment details to purchase the shopping items and order number is received.
5. Scenario to click submit in the checkout page without key in delivery address 
6. Scenario to click submit in the checkout page without key in payment details
7. Scenario to login into the toys application using valid/invalid credentials
8. Scenario to check, upon clicking start shopping button from home page,if the user can navigate to Shop page or not
9. Scenario to check if user can carry on shopping from cart page after clicking Carry on Shopping option
10. After completing the purchase, if the user click Shopping again button, user should be redirected  to shopping page and cart list should be empty.


2. Jupiter Toys is expected to grow and expand its offering into books, tech, and modern art. We are expecting the of tests will grow to a very large number.

What approaches could you used to reduce overall execution time?
 Answer: 
1. Parallel Test Execution:
   a. We can trigger the scrips over multiple browsers in parallel using Pytest xdist distributed plugin.We can specify different platforms and run tests in parallel on all of them and this helps to reduce the test exectuion time.
   for ex: Assume for one test case the script run time is 5 mins and for 10 test case in sequence run, it will be around 50 mins.
   whereas in parallel execution mode all the scripts will be triggered at one go and total execution time is 5 mins for all the cases
   b. If CI/CD pipeline setup implemented, segregating the test execution on  different machines can be achieved using Jenkins agents for distributed build environments. We can create multiple nodes based on the remote machine/virtual machines/docker container availability and all the scripts can be triggered in one go.
2. Headless Browser Execution:
    Effective way of running the browser UI tests without the actual browser,  it does not require the test environment to display the visual elements of an application,which typically increases the execution time compared to browser tests.
    Headless testing implemented in this framework and that can be controlled based on the headless parameter in the config file.
3. using Wait time smartly:
    Using explicit timeouts wherever required because the script will wait until a certain condition occurs. If we set the implict wait time, script will wait for the whole time frame which impacts the execution time.
4. Halting test cases at appropriate places instead of running the whole test cases. if any failure in the middle of the scripts, there is no point in running the whole test cases. If the expected behaviour is not achieved,we can use sys.exit function to come out the script run.
5. Using API  testing wherever applicable instead of navigating it through the web UI

How will your framework cater for this?
 Answer: 
1.  Common test methods defined for repetitive tasks like 
    selecting the items from the shop page, 
    get_item_price_in_shoppage, 
    go_to_cart_page,
    get_item_price_in_cart,
    validate_item_price,
    validate_price_total, so that even if other products like Books, tech, and modern art are added and if that has the same behaviour as toys-buy we can use the same methods and just the test data - parameter to be changed in the external test data source to utilize those common methods.
2. Parametrization using pytest.mark.parametrize is implemented in this script so that we can repeat the same test cases for multiple combinations of data and that can be executed in parallel as well.
3. For parallel execution we can make use of xdist plugin and while running the tests from command line we can input -n followed by number of times scripts to be executed
    ex: pytest <<test file path >> -n=2 (test file will be executed in parallel based on browser/system config)
4. Headless testing implemented in this framework and in the config file there is a parameter "Headless" and in the conftest file browser mode is handled. if headless value is "Y" script will run in the background instead od opening the browser UI and for value "N" script will be executed in browser mode.



Question 3: 
Describe when to use a BDD approach to automation and when NOT to use BDD 

when to use:
1. BDD process is clearly defined and everyone in the team follows the process. Because communications between the user and the developer are essential, if the user if not available, it will be difficult to work past ambiguities and questions generated by the user stories
2. If the requirements comes from Business ex. Business rules check then we can make that as a BDD test. If the requirements is part of the implementation then it should be a unit test ex: Testing an API
3. BDD should be used to test a particular behaviour not all the individual components of a behaviour.
4. No frequent change in the requirements, if requirement change quite often it will be difficult to keep the automated tests in sync with what’s being developed
5. Use BDD when it will have wide collaboration to include stakeholders/ Three amigos who would be excluded if we use unit tests or other
6. BDD can be used if we know the domain/functionality where in for the domain which we are exploring BDD is not recommended

Not to use/not recommended if :
1. project requires multiple combinations to test using external data sources depending on external sources sometimes cause problems. we can define in the Given statement but this quickly become complex
2. Retrofitting is time consuming, Retrospectively fitting BDD to an existing project can be a time-consuming and difficult process
3. BDD process is not followed correctly, then automating the scripts becomes quite difficult
4. Parallelization is needed to test many combinations of test data
5. No proper communication between dev, BA, Business and test roles
