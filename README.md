# ERP Automation
This test suite was created in order to speed up internal testing. It uses Selenium to move through the UI ensuring the
end user behaviour is as expected. 

## Project Structure

```
automated_tests/
├── .venv
├── json_skeletons/
│   └── configs/
│       └── *json templates
├── pages/
│   ├── base.py
│   └── configs/
│       ├── product_cateogory.py
│       ├── service_types.py
│       ├── routes.py
│       ├── rules.py
│       ├── package_types.py
│       ├── artworkmanifest.py
│       └── shipping_methods.py
├── testcases_json/
│   └── configs/
│       └── specific dirs/
│           └── *json data
├── tests/
│   └── configs/
│       ├── test_artwork_manifest.py
│       ├── test_product_categories.py
│       ├── test_routes.py
│       ├── test_operation_types.py
│       ├── test_rules.py
│       ├── package_types.py
│       ├── test_service_types.py
│       └── test_shipping_methods.py
├── static/
│   └── *any needed static files
├── README.md
├── conftest.py
├── pyrightconfig.json
├── run_tests.py
└── requirements.txt
```
The backbone of the tests is Pytest. Currently, the only test suite is to check if shipping methods are configured correctly.
Filling out the JSON skeleton and placing it into the ```testcases_json/<desired test folder> ``` it will append that json
data and run all the tests outlined in the script. 
This allows the extension of the test in the category as well as more components

## Usage
Run ```python run_scripts.py``` and it will run the entire suite on our staging instance

Use ```--tb <length of trace back>``` to adjust the trace back length. All Pytest options are available

Use ```--count <int>``` or ```-c <int>``` To run the test multiple times

Use ```--environment <staging or production or uat>```  or ```-e <staging or production or uat>``` To choose which instance to test on

Use ```--file <test script path>``` or ```-f <test script path>``` To run a specific tests script

Use ```--window ``` To watch the test go through the UI or ```--window kiosk``` for fullscreen
    -> [!WARNING]> you may interfere with the test if you interact with the browser manually

## Next Tests
1. Other configurations and their children
2. End to End product movement
3. state testing :(


### Example Output
![image](https://github.com/user-attachments/assets/a8b3120d-c68c-4969-91da-11bc054c3e23)
![image](https://github.com/user-attachments/assets/3a60ef0f-6fbe-44dc-b217-adb04652aedb)

