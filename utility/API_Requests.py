import json

import allure
import pytest
import requests



@allure.step('Response')
def get_response(response):
    pass

@allure.step('Status code')
def get_status_code(status_code):
    pass



class API_Request:

    @allure.step('GET Request call for')
    def get_request(self, endpoint, params):
        response = requests.get(endpoint, params=params)
        get_response(str(response.json()))
        get_status_code(response.status_code)
        return response
