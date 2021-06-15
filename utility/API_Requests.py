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
    # for getting header value
    def post_request(self, uri, payload):
        response = requests.post(uri, json.dumps(payload))
        # get_response(str(response.json()))
        # print(json.dumps(response.json(), indent=4))
        # if response.json()["status"] == "success":
        #     pass
        # else:
        #     pytest.fail(response.json(), pytrace=True)
        return response

    def post_request_with_header(self, uri, payload, header):
        response = requests.post(uri, json.dumps(payload), headers=header)
        print(response)
        return response

    def delete_request_with_payload(self, uri, payload, header):
        response = requests.delete(uri, json=payload, headers=header)
        # print(json.dumps(response.json(), indent=4))
        # if response.json()["status"] == "success":
        #     pass
        # else:
        #     pytest.fail(response.json()["status"] == "success", pytrace=True)
        return response

    # def delete_request_with_payload_without_header(self, uri, payload):
    #     response = requests.delete(uri, json=payload)       # json.dumps(payload) not working
    #     return response


    def delete_request_without_payload(self, uri, header):
        response = requests.delete(uri, headers=header)
        print(json.dumps(response.json(), indent=4))
        # if response.json()["status"] == "success":
        #     pass
        # else:
        #     pytest.fail(response.json()["status"] == "success", pytrace=True)
        return response

    @allure.step('GET Request call for')
    def get_request(self, endpoint, params):
        response = requests.get(endpoint, params=params)
        get_response(str(response.json()))
        get_status_code(response.status_code)
        assert response.status_code == 200
        return response
