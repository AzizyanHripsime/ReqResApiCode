import pytest
import requests
import allure


@pytest.fixture(scope="session")
def user_data():
    return {}


@allure.feature('Create user-feature')
@allure.suite('Create user-suite')
class TestRestApiPost():
    @allure.title('Test Create User')
    @allure.description("This test case verifies that we created a new user successfully")
    @pytest.mark.smoke
    def test_create(self, user_data):
        data = {
            "name": "morpheus",
            "job": "leader"
        }
        headers={'Content-Type': 'application/json'}

        with allure.step("Send POST request to create a new user"):
            response = requests.post('https://reqres.in/api/users', json=data, headers=headers)

        with allure.step("Verify the response status code"):
            assert response.status_code == 201, f'Expected Status code 201, but got {response.status_code}'

        response_body = response.json()
        user_data['id'] = response_body.get('id')
        with allure.step("Verify the response contains 'name'"):
            assert 'name' in response_body, "The response data does not contain 'name'"

        with allure.step("Verify the response contains 'job'"):
            assert 'job' in response_body, "The response data does not contain 'job'"

        with allure.step("Verify the response contains 'id'"):
            assert 'id' in response_body, "The response data does not contain 'id'"

        with allure.step("Verify the response contains 'createdAt'"):
            assert 'createdAt' in response_body, "The response data does not contain 'createdAt'"

        with allure.step("Verify the 'name' in response matches the input data"):
            assert response_body['name'] == data['name'], f"Expected name {data['name']}, but got {response_body['name']}"

        with allure.step("Verify the 'job' in response matches the input data"):
            assert response_body['job'] == data['job'], f"Expected job {data['job']}, but got {response_body['job']}"


@allure.feature('Update user all data-feature')
@allure.suite('Update user all data-suite')
class TestRestApiUpdatePut():
    data = [
        {"name": "kim", "job": "zion resident"}
    ]
    headers = {'Content-Type': 'application/json'}

    @allure.feature('Update User Data With PUT-feature')
    @allure.suite('Update User Data With PUT-suite')
    @pytest.mark.smoke
    @pytest.mark.parametrize('condition', data)
    def test_update_put(self, condition, user_data):
        user_id = user_data.get('id')

        with allure.step("Send PUT request to update user data"):
            response = requests.put(f'https://reqres.in/api/users/{user_id}', json=condition, headers=self.headers)

        with allure.step("Verify the response status code"):
            assert response.status_code == 200, f'Expected Status code 200, but got {response.status_code}'

        response_data = response.json()

        with allure.step("Verify the response contains 'name'"):
            assert 'name' in response_data, f"The response data does not contain 'name'"

        with allure.step("Verify the response contains 'job'"):
            assert 'job' in response_data, f"The response data does not contain 'job'"

        with allure.step("Verify the response contains 'updatedAt'"):
            assert 'updatedAt' in response_data, f"The response data does not contain 'updatedAt'"

        with allure.step("Verify the 'name' in the response matches the input data"):
            assert condition['name'] == response_data['name'], f"Expected name {condition['name']}, but got {response_data['name']}"

        with allure.step("Verify the 'job' in the response matches the input data"):
            assert condition['job'] == response_data['job'], f"Expected job {condition['job']}, but got {response_data['job']}"


@allure.feature('Update user partial data-feature')
@allure.suite('Update user partial data-suite')
class TestRestApiUpdatePatch():
    data = [
        {"name": "ashot", "job": "zion resident"}
    ]
    headers = {'Content-Type': 'application/json'}

    @allure.feature('Update User Data With PATCH-feature')
    @allure.suite('Update User Data With PATCH-suite')
    @pytest.mark.regression
    @pytest.mark.parametrize('condition', data)
    def test_update_patch(self, condition, user_data):
        user_id = user_data.get('id')

        with allure.step("Send PATCH request to update user data"):
            response = requests.patch(f'https://reqres.in/api/users/{user_id}', json=condition, headers=self.headers)

        with allure.step("Verify the response status code"):
            assert response.status_code == 200, f'Expected Status code 200, but got {response.status_code}'

        response_data = response.json()

        with allure.step("Verify the response contains 'name'"):
            assert 'name' in response_data, f"The response data does not contain 'name'"

        with allure.step("Verify the response contains 'job'"):
            assert 'job' in response_data, f"The response data does not contain 'job'"

        with allure.step("Verify the response contains 'updatedAt'"):
            assert 'updatedAt' in response_data, f"The response data does not contain 'updatedAt'"

        with allure.step("Verify the 'name' in the response matches the input data"):
            assert condition['name'] == response_data['name'], f"Expected name {condition['name']}, but got {response_data['name']}"

        with allure.step("Verify the 'job' in the response matches the input data"):
            assert condition['job'] == response_data['job'], f"Expected job {condition['job']}, but got {response_data['job']}"


@allure.feature('User Delete-feature')
@allure.suite('User Delete-suite')
class TestUserDelete():

    @allure.title('Test Delete User')
    @allure.description('This test verifies that a user can be successfully deleted.')
    @pytest.mark.smoke
    def test_delete_user(self, user_data):
        user_id = user_data.get('id')
        with allure.step(f"Send delete request for user with ID {user_id}"):
            response = requests.delete(f"https://reqres.in/api/users/{user_id}")
        with allure.step("Verify the delete response status code"):
            assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"


if __name__ == "__main__":
    pytest.main()
