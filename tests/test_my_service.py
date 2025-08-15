from http import HTTPStatus

from src.data.constants import Constants


class TestMyService:
    def test_login_success(self, my_app_helper):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = my_app_helper.login_user(data=data, headers=Constants.headers)

        assert response.status_code == HTTPStatus.OK, f"Expected status code {HTTPStatus.OK} but got {response.status_code}. {response.text}"
        assert response.json()["token"] is not None

    def test_create_user(self, my_app_helper):
        data = {
            "name": "morpheus",
            "job": "leader"
        }
        response = my_app_helper.create_user(data=data, headers=Constants.headers)
        response_data = response.json()

        assert response.status_code == HTTPStatus.CREATED, f"Expected status code {HTTPStatus.CREATED} but got {response.status_code}. {response.text}"
        assert response_data["id"] is not None
        assert response_data["name"] == data.get("name")
        assert response_data["job"] == data.get("job")

    def test_update_user(self, my_app_helper):
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        user_id = 2
        response = my_app_helper.update_user(data=data, headers=Constants.headers, user_id=user_id)

        assert response.status_code == HTTPStatus.OK, f"Expected status code {HTTPStatus.OK} but got {response.status_code}. {response.text}"
        assert response.json()["job"] == data.get("job")

    def test_delete_user(self, my_app_helper):
        user_id = 2
        response = my_app_helper.delete_user(headers=Constants.headers, user_id=user_id)

        assert response.status_code == HTTPStatus.NO_CONTENT, f"Expected status code {HTTPStatus.NO_CONTENT} but got {response.status_code}. {response.text}"

    def test_get_user(self, my_app_helper):
        user_id = 2
        response = my_app_helper.get_user(headers=Constants.headers, user_id=user_id)

        assert response.status_code == HTTPStatus.OK, f"Expected status code {HTTPStatus.OK} but got {response.status_code}. {response.text}"
        assert response.json()["email"] == "janet.weaver@reqres.in"

    def test_get_users(self, my_app_helper):
        response = my_app_helper.get_users(headers=Constants.headers)

        assert response.status_code == HTTPStatus.OK, f"Expected status code {HTTPStatus.OK} but got {response.status_code}. {response.text}"
