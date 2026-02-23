import allure


from utils import helpers


class TestOrderList:
    @allure.title(
        "Проверка получения списка заказов: код ответа 200, в теле ответа есть список заказов"
    )
    def test_get_order_list_success(self):
        response = helpers.get_orders_list()
        body = response.json()
        assert response.status_code == 200
        assert "orders" in body
        assert len(body["orders"]) > 0
        assert "id" in body["orders"][0]

    @allure.title(
        "Проверка получения списка заказов несуществующего курьера: код ответа 404, в теле ответа 'Курьер с идентификатором 999999 не найден'"
    )
    def test_get_order_list_with_nonexisting_courier_fail(self):
        response = helpers.get_orders_list_with_unexisting_courier()
        assert response.status_code == 404
        assert response.json()["message"] == "Курьер с идентификатором 999999 не найден"
