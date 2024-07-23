# ERP Automation
This test suite was created in order to speed up internal testing. It uses Selenium to move through the UI ensuring the
end user behaviour is as expected. 

## Project Structure
The backbone of the tests is Pytest. Currently, the only test suite is to check if shipping methods are configured correctly.
Filling out the JSON skeleton and placing it into the ```testcases_json/<desired test folder> ``` it will append that json
data and run all the test outlined in the script. 
This allows extension of the test in the category as well as more components

## Usage
Run ```python run_scripts.py``` and it will run the entire suite on our staging instance

Use ```--tb <length of trace back>``` to adjust the length of trace back. All Pytest options are available

Use ```--count <int>``` or ```-c <int>``` To run the test multiple times

Use ```--environment <staging or production>```  or ```-e <staging or production>``` To choose which instance to test on

## Next Tests
1. Other configurations and their children
2. End to End product movement
3. state testing :(
