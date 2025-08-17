import json
from http import HTTPStatus

import pytest

from src.data.constants import Constants
from src.models.Pagination import Pagination
from src.models.User import User


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
        response = my_app_helper.update_user(headers=Constants.headers, user_id=2)

        assert response.status_code == HTTPStatus.OK, f"Expected status code {HTTPStatus.OK} but got {response.status_code}. {response.text}"
        assert response.json()["first_name"] == "updated_first_name"

    @pytest.mark.parametrize("user_id", [1, 6, 12])
    def test_get_user(self, my_app_helper, user_id):
        response = my_app_helper.get_user(headers=Constants.headers, user_id=user_id)

        User.model_validate(response.json())
        assert response.status_code == HTTPStatus.OK, f"Expected status code {HTTPStatus.OK} but got {response.status_code}. {response.text}"
        assert response.json()["email"] is not None

    def test_get_users(self, my_app_helper):
        response = my_app_helper.get_users(headers=Constants.headers)

        for user in response.json()["items"]:
            User.model_validate(user)

        assert response.status_code == HTTPStatus.OK, f"Expected status code {HTTPStatus.OK} but got {response.status_code}. {response.text}"

    @pytest.mark.parametrize("page,size", ([1, 3], [2, 8]))
    def test_get_users_with_pagination(self, my_app_helper, page, size):
        response = my_app_helper.get_users(headers=Constants.headers, params=Pagination(page=page, size=size).dict())

        data = response.json()

        assert response.status_code == HTTPStatus.OK, f"Expected status code {HTTPStatus.OK} but got {response.status_code}. {response.text}"
        assert len(data["items"]) <= size
        assert data["total"] == 12
        assert data["page"] == page
        assert data["size"] == size

    @pytest.mark.parametrize("size", [1, 10])
    def test_get_users_with_size(self, my_app_helper, size):
        response = my_app_helper.get_users(headers=Constants.headers, params=Pagination(size=size).dict())

        data = response.json()

        assert response.status_code == HTTPStatus.OK, f"Expected status code {HTTPStatus.OK} but got {response.status_code}. {response.text}"
        assert len(data["items"]) == size
