import allure
from utils.helpers import login_courier
from utils.courier_data import UNEXISTING_LOGIN, UNEXISTING_PASSWORD, WRONG_PASSWORD


class TestLoginCourier:
    @allure.title("Логин курьера: код ответа 200, в теле ответа есть id")
    def test_login_courier_success(self, created_courier):
        response = login_courier(created_courier["login"], created_courier["password"])
        assert response.status_code == 200
        assert response.json().get("id")

    @allure.title(
        "Запрос без логина: код ответа 400, в теле ответа: 'Недостаточно данных для входа'"
    )
    def test_login_courier_without_login_fail(self, created_courier):
        response = login_courier("", created_courier["password"])
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title(
        "Запрос без пароля: код ответа 400,в теле ответа: 'Недостаточно данных для входа'"
    )
    def test_login_courier_without_password_fail(self, created_courier):
        response = login_courier(created_courier["login"], "")
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title(
        "Запрос c неверным паролем: код ответа 404, в теле ответа: 'Учетная запись не найдена'"
    )
    def test_login_courier_wrong_password_fail(self, created_courier):
        response = login_courier(created_courier["login"], WRONG_PASSWORD)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title(
        "Авторизация несуществующего курьера: код ответа 404, в теле ответа: 'Учетная запись не найдена'"
    )
    def test_login_courier_nonexistent_courier_fail(self):
        response = login_courier(UNEXISTING_LOGIN, UNEXISTING_PASSWORD)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
