# get
import requests
import allure
import pytest

@allure.feature('Test Get-feature')
@allure.suite('Test Get-suite')
class TestRestApiGet():

    @allure.title('Get List Users')
    @allure.description("This test case verifies that we get correct response data")
    @pytest.mark.regression
    def test_get_list_users(self):
        with allure.step("Send GET request to fetch list of users"):
            response = requests.get('https://reqres.in/api/users?page=2')

        with allure.step("Verify the response status code"):
            assert response.status_code == 200, f'Expected Status code 200, but got {response.status_code}'

        response_body = response.json()

        with allure.step("Verify the page number in the response"):
            assert response_body['page'] == 2

        with allure.step("Verify the per_page count in the response"):
            assert response_body['per_page'] == 6

        with allure.step("Verify the number of users in the response"):
            assert len(response_body['data']) == 6

        with allure.step("Verify the total_pages count in the response"):
            assert response_body['total_pages'] == 2

        with allure.step("Verify the response contains 'data'"):
            assert "data" in response_body

    @allure.title('Get Single User')
    @allure.description("This test case verifies that we get correct response for single user")
    @pytest.mark.regression
    def test_get_single_user(self):
        with allure.step("Send GET request to fetch a single user"):
            response = requests.get('https://reqres.in/api/users/10')

        with allure.step("Verify the response status code"):
            assert response.status_code == 200, f'Expected Status code 200, but got {response.status_code}'

        response_body = response.json()

        with allure.step("Verify the user ID in the response"):
            assert response_body['data']['id'] == 10

    @allure.title('Get Single User Not Found')
    @allure.description("This test case verifies that we receive Not Found Error")
    @pytest.mark.regression
    def test_get_single_user_not_found(self):
        with allure.step("Send GET request to fetch a non-existent user"):
            response = requests.get('https://reqres.in/api/users/23')

        with allure.step("Verify the response status code"):
            assert response.status_code == 404, f'Expected Status code 404, but got {response.status_code}'

    @allure.title('Get List Resource')
    @allure.description("This test case verifies that we receive all elements in data")
    @pytest.mark.regression
    def test_get_list_resource(self):
        with allure.step("Send GET request to fetch list of resources"):
            response = requests.get('https://reqres.in/api/unknown')

        with allure.step("Verify the response status code"):
            assert response.status_code == 200, f'Expected Status code 200, but got {response.status_code}'

        response_body = response.json()

        with allure.step("Verify the response contains 'data'"):
            assert "data" in response_body

        with allure.step("Verify each resource contains required keys"):
            for resource in response_body['data']:
                assert 'id' in resource, f"'id' key is missing in data: {resource}"
                assert 'name' in resource, f"'name' key is missing in data: {resource}"
                assert 'year' in resource, f"'year' key is missing in data: {resource}"
                assert 'color' in resource, f"'color' key is missing in data: {resource}"
                assert 'pantone_value' in resource, f"'pantone_value' key is missing in data: {resource}"

        with allure.step("Verify 'data' is a non-empty list"):
            assert isinstance(response_body["data"], list)
            assert len(response_body["data"]) > 0

    @allure.title('Get Single Resource')
    @allure.description("This test case verifies that we receive all elements in data for single user")
    @pytest.mark.regression
    def test_get_single_resource(self):
        resource_id = 2

        with allure.step(f"Send GET request to fetch resource with ID {resource_id}"):
            response = requests.get(f"https://reqres.in/api/unknown/{resource_id}")

        with allure.step("Verify the response status code"):
            assert response.status_code == 200, f'Expected Status code 200, but got {response.status_code}'

        response_body = response.json()

        with allure.step("Verify the response contains 'data'"):
            assert "data" in response_body, "'data' key is missing in the response body"

        resource = response_body["data"]

        with allure.step(f"Verify the resource ID matches {resource_id}"):
            assert resource["id"] == resource_id, f'Expected resource id {resource_id}, but got {resource["id"]}'

        with allure.step("Verify the resource contains 'name'"):
            assert "name" in resource, "'name' key is missing in the resource"

        with allure.step("Verify the resource contains 'year'"):
            assert "year" in resource, "'year' key is missing in the resource"

        with allure.step("Verify the resource contains 'color'"):
            assert "color" in resource, "'color' key is missing in the resource"

        with allure.step("Verify the resource contains 'pantone_value'"):
            assert "pantone_value" in resource, "'pantone_value' key is missing in the resource"

    @allure.title('Get Single Resource Not Found')
    @allure.description("This test case verifies that we receive not found error for single user")
    @pytest.mark.regression
    def test_get_single_resource_not_found(self):
        with allure.step("Send GET request to fetch a non-existent resource"):
            response = requests.get('https://reqres.in/api/unknown/23')

        with allure.step("Verify the response status code"):
            assert response.status_code == 404, f'Expected Status code 404, but got {response.status_code}'

if __name__ == "__main__":
    pytest.main()
