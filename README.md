# ERP Automation
This test suite was created in order to speed up internal testing. It uses Selenium to move through the UI ensuring the
end user behaviour is as expected. 

## Project Structure

```
automated_tests/
├── .venv
├── json_skeletons/
│   ├── apparel_shipping_template.json
│   └── *other JSON templates for tests
├── pages/
│   ├── __init__.py
│   ├── base.py
│   ├── product_category.py
│   └── shipping_methods.py
├── testcases_json/
│   ├── shipping_methods/
│   │   └── *JSON of all base cases
│   └── product_categories/
│       ├── finished/
│       │   └── *JSON of all base cases
│       └── raw/
│           └── *JSON of all base cases
├── tests/
│   ├── __init__.py
│   ├── test_product_categories.py
│   └── tests_shipping_methods.py
├── .env
├── README.md
├── conftest.py
├── requirements.txt
└── runtests.py
```
The backbone of the tests is Pytest. Currently, the only test suite is to check if shipping methods are configured correctly.
Filling out the JSON skeleton and placing it into the ```testcases_json/<desired test folder> ``` it will append that json
data and run all the tests outlined in the script. 
This allows the extension of the test in the category as well as more components

## Usage
Run ```python run_scripts.py``` and it will run the entire suite on our staging instance

Use ```--tb <length of trace back>``` to adjust the trace back length. All Pytest options are available

Use ```--count <int>``` or ```-c <int>``` To run the test multiple times

Use ```--environment <staging or production>```  or ```-e <staging or production>``` To choose which instance to test on

Use ```--file <test script path>``` or ```-f <test script path>``` To run a specific tests script

Use ```--window ``` To watch the test go through the UI or ```--window kiosk``` for fullscreen
    -> [!WARNING]> you may interfere with the test if you interact with the browser manually

## Next Tests
1. Other configurations and their children
2. End to End product movement
3. state testing :(


### Example Output
![image](https://github.com/user-attachments/assets/a8b3120d-c68c-4969-91da-11bc054c3e23)
