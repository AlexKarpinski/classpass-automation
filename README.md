### Classpass Python Framework 
-----
## In order to start to work with the project, download it using command:
```
git clone git@github.com:AlexKarpinski/classpass-automation.git
```

## Then load all dependencies:
```
pipenv install
```

## Run Instructions 
----- 
The python framework can be ran directly from the command line using pytest. The framework fetches the latest build from Kobiton to test against if you do not provide a build in the call. 

Call Example 

Use 'pytest -h' to see usage. 
```
usage: pytest test [-m] --device-name --env --build 

Custom options:
  --device-name is required. 
  --env is optional. By default uses 'prod' env.  
```
## Examples 

Execute all tests on MAC_MINI_LOCAL_SAMSUNG_S6 desired capabilities locally
```
pytest --device-name MAC_MINI_LOCAL_SAMSUNG_S6
```
Execute all tests using MAC_MINI_LOCAL_IPHONE_XR from desired capabilities
```
pytest --device-name MAC_MINI_LOCAL_IPHONE_XR
```
Execute all tests using KOBITON_SAMSUNG_S6 in the Kobiton from desired capabilities
```
pytest --device-name KOBITON_SAMSUNG_S6
```
## Allure report:
After tests execution is completed, results are loaded into allure-results folder.
To open allure report use the following command:
```
allure serve allure_results/"path"
```
Note: Before running tests it makes sense to delete allure-results folder if it is not empty:

Windows:
```
rmdir allure_results
```
Mac/linyx:
```
rm -rf allure_results
```
