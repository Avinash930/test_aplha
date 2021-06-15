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


def test_timeseries():
    params = {'function': function_name , 'symbol': symbol_name, 'interval': interval_value, 'apikey': api_key}
    api_requests.get_request(alpha_endpoint,params)

def test_generate_report():
    os.system('allure generate report/allure')

