import allure
import requests
import pytest


@allure.feature('User Registration-feature')
@allure.suite('Registration-suite')
class TestUserRegistration():
  @allure.title('Test Successful Registration')
  @allure.description('This test verifies that a user can successfully register with valid credentials.')
  @pytest.mark.regression
  @pytest.mark.smoke
  def test_registration_successful(self):
    data={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }
    with allure.step("Send registration request with valid data"):
      response=requests.post('https://reqres.in//api/register', data=data)
    with allure.step("Verify the response status code and response data"):
      assert response.status_code==200, f"Expected status code 200, but got {response.status_code}"
      self.token=response.json().get('token')
      response_data=response.json()
      assert 'token' in response_data, "Token not found in response data"
      assert 'id'in response_data, "Id not found in response data"

    @allure.title('Test Unsuccessful Registration')
    @allure.description('This test verifies that a user cannot register with missing password.')
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_registration_unsuccessful(self):

      data={
      "email": "eve.holt@reqres.in"
      }

      with allure.step("Send registration request with missing password"):
        response=requests.post('https://reqres.in//api/register', data=data)
      with allure.step("Verify the response status code and response data"):
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        self.token=response.json().get('token')
        response_data = response.json()
        assert 'token' not in response_data, "Token found in response data"
        assert 'id' not in response_data, "Id found in response data"
        assert 'error' in response_data, 'Error message not found in response data'
        assert response_data['error']=='Missing pasword', "Error message is not 'Missing pasword'"


if __name__ == "__main__":
    pytest.main()
