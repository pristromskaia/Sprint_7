import pytest
from utils.helpers import (
    create_courier_details,
    create_courier,
    delete_courier_by_id,
    login_courier,
)


@pytest.fixture
def courier_data():
    courier_data = create_courier_details()
    yield courier_data
    login_response = login_courier(courier_data["login"], courier_data["password"])
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        delete_courier_by_id(courier_id)


@pytest.fixture
def created_courier():
    courier_data = create_courier_details()
    create_courier(courier_data)
    login_response = login_courier(courier_data["login"], courier_data["password"])
    courier_id = login_response.json()["id"]
    yield courier_data
    delete_courier_by_id(courier_id)
