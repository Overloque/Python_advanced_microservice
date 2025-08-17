import requests

from src.models.Pagination import Pagination


class MyAppHelper:
    """
    Методы для приложения
    """

    def __init__(self, base_url: str):
        self.base_url = base_url

    def _get_url(self, url: str):
        return f"{self.base_url}/{url}"

    def get_users(self, headers, params: dict = None):
        url = "/"
        return requests.get(url=self._get_url(url), headers=headers, params=params)

    def login_user(self, data, headers):
        url = "api/login"
        return requests.post(url=self._get_url(url), json=data, headers=headers)

    def create_user(self, data, headers):
        url = "api/users"
        return requests.post(url=self._get_url(url), json=data, headers=headers)

    def update_user(self, headers, user_id: int):
        url = f"api/users/{user_id}"
        return requests.put(url=self._get_url(url), json={}, headers=headers)

    def get_user(self, headers, user_id: int):
        url = f"api/users/{user_id}"
        return requests.get(url=self._get_url(url), headers=headers)

    def get_status(self):
        url = "status"
        return requests.get(url=self._get_url(url))
