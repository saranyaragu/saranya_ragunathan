#!/bin/bash

echo '#### Create Virtual Environment ####'
VIRTUAL_ENV_NAME='virtual-environment'
virtualenv $VIRTUAL_ENV_NAME


echo '#### Activate Virtual Environment ####'
source $VIRTUAL_ENV_NAME/bin/activate


echo '#### Install requirements ####'
pip install -r ./requirements.txt


echo '#### Run tests ####'
pytest Tests/test_01.py --alluredir=TestReports/test_case_01 --browser <firefox/remote/chrome_headless>
pytest Tests/test_02.py --alluredir=TestReports/test_case_02 --browser <firefox/remote/chrome_headless>
pytest Tests/test_03.py --alluredir=TestReports/test_case_03 --browser <firefox/remote/chrome_headless>
pytest Tests/test_04.py --alluredir=TestReports/test_case_04 --browser <firefox/remote/chrome_headless>

 
echo ### deactivate virtual environment ###
deactivate
