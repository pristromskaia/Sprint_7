import allure
from utils.helpers import (
    create_courier_details,
    create_courier_details_without_password,
    create_courier_details_without_login,
    create_courier,
)


class TestCreateCourier:
    @allure.title(
        "Создание курьера с валидными данными: код ответа 201, в теле ответа есть ok: true"
    )
    def test_create_courier_with_valid_data_success(self, courier_data):
        response = create_courier(courier_data)
        assert response.status_code == 201
        assert response.json().get("ok") is True

    @allure.title(
        "Нельзя создать двух одинаковых курьеров: код ответа 409, в теле ответа 'Этот логин уже используется. Попробуйте другой.'"
    )
    def test_create_duplicate_courier_fail(self, created_courier):
        second_response = create_courier(created_courier)
        assert second_response.status_code == 409
        assert (
            second_response.json().get("message")
            == "Этот логин уже используется. Попробуйте другой."
        )

    @allure.title(
        "Нельзя создать курьера без пароля: код ответа 400, в теле ответа 'Недостаточно данных для создания учетной записи'"
    )
    def test_create_courier_without_password_fail(self):
        courier_data = create_courier_details_without_password()
        response = create_courier(courier_data)
        assert response.status_code == 400
        assert (
            response.json().get("message")
            == "Недостаточно данных для создания учетной записи"
        )

    @allure.title(
        "Нельзя создать курьера без логина: код ответа 400, в теле ответа 'Недостаточно данных для создания учетной записи'"
    )
    def test_create_courier_without_login_fail(self):
        courier_data = create_courier_details_without_login()
        response = create_courier(courier_data)
        assert response.status_code == 400
        assert (
            response.json().get("message")
            == "Недостаточно данных для создания учетной записи"
        )
