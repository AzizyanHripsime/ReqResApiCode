import allure
import requests
import pytest


@allure.feature('User Login-feature')
@allure.suite('User Login-suite')
class TestUserLogin():
    @allure.title('Test Successful Login')
    @allure.description('This test verifies that a user can successfully log in with valid credentials.')
    @pytest.mark.regression
    def test_login_successful(self):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        with allure.step("Send login request with valid data"):
            response = requests.post('https://reqres.in/api/login', data=data)
        with allure.step("Verify the response status code and response data"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
            self.token = response.json().get('token')
            response_data = response.json()
            assert 'token' in response_data, "Token not found in response data"

    @allure.title('Test Unsuccessful Login')
    @allure.description('This test verifies that a user cannot log in with missing password.')
    @pytest.mark.regression
    def test_login_unsuccessful(self):
        data_un = {"email": "peter@klaven"}
        with allure.step("Send login request with missing password"):
            response = requests.post('https://reqres.in/api/login', data=data_un)
        with allure.step("Verify the response status code and response data"):
            assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
            response_data = response.json()
            assert 'token' not in response_data, "Token found in response data"
            assert 'id' not in response_data, "Id found in response data"
            assert 'error' in response_data, 'Error message not found in response data'
            assert response_data['error'] == 'Missing password', "Error message is not 'Missing password'"


if __name__ == "__main__":
    pytest.main()
