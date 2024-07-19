import requests
import allure
import pytest


@allure.feature("Reqres API-feature")
@allure.suite("Reqres API-suite")
@allure.story("Delayed Response")
@allure.title("Test delayed response of the Reqres API")
@pytest.mark.regression
def test_delayed_response():
    url = "https://reqres.in/api/users?delay=3"
    with allure.step(f"Send GET request to {url}"):
        response = requests.get(url)

    with allure.step("Check response status code"):
        assert response.status_code == 200

    with allure.step("Check if response contains the expected keys"):
        data = response.json()
        assert 'data' in data
        assert 'page' in data
        assert 'total' in data


if __name__ == "__main__":
    pytest.main()