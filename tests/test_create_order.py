import allure
import pytest

from utils.order_data import build_order_payload, COLOR_VARIANTS
from utils.helpers import create_order


@allure.epic("Orders API")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title(
        "Создание заказа ({color_title}): код ответа 201, в теле ответа есть track"
    )
    @pytest.mark.parametrize("colors, color_title", COLOR_VARIANTS)
    def test_create_order_success(self, colors, color_title):
        payload = build_order_payload()
        if colors is not None:
            payload["color"] = colors
        response = create_order(payload)
        body = response.json()
        assert response.status_code == 201
        assert isinstance(body.get("track"), int)
