import os
import glob
import shutil

from utility.API_Requests import API_Request
from utility.ConfigFileReader import ConfigFileReader

config_reader = ConfigFileReader()
api_requests = API_Request()

api_key = config_reader.get_value_of(os.path.abspath('')+'/test_data/Config.ini','APPLICATION_DETAILS',
                                      'API_KEY')

function_name = config_reader.get_value_of(os.path.abspath('')+'/test_data/Config.ini','APPLICATION_DETAILS',
                                      'FUNCTION_NAME')

symbol_name = config_reader.get_value_of(os.path.abspath('')+'/test_data/Config.ini','APPLICATION_DETAILS',
                                      'SYMBOL_NAME')

interval_value = config_reader.get_value_of(os.path.abspath('')+'/test_data/Config.ini','APPLICATION_DETAILS',
                                      'INTERVAL_VALUE')

alpha_endpoint = config_reader.get_value_of(os.path.abspath('')+'/test_data/Config.ini','ENDPOINTS',
                                      'alpha_vantage')



def test_clean():
    files_path = os.path.abspath('')+'/reports/*'
    filelist = glob.glob(files_path)
    for file in filelist:
        print(file)
        os.remove(file)
    if os.path.isdir(os.path.abspath('')+'/allure-report'):
        shutil.rmtree(os.path.abspath('')+'/allure-report')


def test_timeserieswithValidParams():
    params = {'function': function_name , 'symbol': symbol_name, 'interval': interval_value, 'apikey': api_key}
    response = api_requests.get_request(alpha_endpoint,params)
    assert response.status_code == 200



def test_timeserieswithEmptyAPIKey():
    params = {'function': function_name , 'symbol': symbol_name, 'interval': interval_value, 'apikey': ''}
    response = api_requests.get_request(alpha_endpoint,params)
    assert response.status_code == 200
    assert response.json()['Error Message'] == 'the parameter apikey is invalid or missing. Please claim your free API key on (https://www.alphavantage.co/support/#api-key). It should take less than 20 seconds.'


def test_timeserieswithEmptyParamters():
    params = {'function': '' , 'symbol': '', 'interval': '', 'apikey': api_key}
    response = api_requests.get_request(alpha_endpoint,params)
    assert response.status_code == 200
    assert response.json()['Error Message'] == 'This API function () does not exist.'


def test_timeserieswithInvalidIntervalTime():
    params = {'function': function_name, 'symbol': symbol_name, 'interval': '0min', 'apikey': api_key}
    response = api_requests.get_request(alpha_endpoint,params)
    assert response.status_code == 200
    assert response.json()['Error Message'] == 'Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_INTRADAY.'


def test_timeserieswithInvalidSymbol():
    params = {'function': function_name, 'symbol': 'BMT', 'interval': interval_value, 'apikey': api_key}
    response = api_requests.get_request(alpha_endpoint,params)
    assert response.status_code == 200
    assert response.json()['Error Message'] == 'Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_INTRADAY.'


def test_generate_report():
    os.system('allure generate report/allure')

