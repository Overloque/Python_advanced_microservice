from http import HTTPStatus


class TestSmoke:
    def test_check_status(self, my_app_helper):
        response = my_app_helper.get_status()

        assert response.status_code == HTTPStatus.OK, f"Expected status code {HTTPStatus.OK} but got {response.status_code}. {response.text}"
        assert response.json()["users"] == True, "Сервис не загрузил данные для тестов"
