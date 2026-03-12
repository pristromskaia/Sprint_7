import random
import string
import requests
from allure import step
from utils.urls import Urls


@step("Создать рандомную строку длины {length}")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


@step("Cоздать рандомные данные курьера")
def create_courier_details():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return {"login": login, "password": password, "firstName": first_name}


@step("Создать радномные данные курьера без пароля")
def create_courier_details_without_password():
    login = generate_random_string(10)
    first_name = generate_random_string(10)
    return {"login": login, "firstName": first_name}


@step("Создать рандомные данные курьера без логина")
def create_courier_details_without_login():
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return {"password": password, "firstName": first_name}


@step("Создать курьера")
def create_courier(payload):
    return requests.post(Urls.CREATE_COURIER, json=payload)


@step("Получить Id курьера")
def get_courier_id(login, password):
    response = login_courier(login, password)
    if response.status_code == 200:
        return response.json().get("id")
    return None


@step("Удалить курьера")
def delete_courier_by_id(courier_id):
    return requests.delete(f"{Urls.DELETE_COURIER}{courier_id}")


@step("Авторизовать курьера")
def login_courier(login, password):
    payload = {"login": login, "password": password}
    return requests.post(Urls.COURIER_LOGIN, json=payload)


@step("Создать заказ с данными {payload}")
def create_order(payload):
    return requests.post(Urls.CREATE_ORDER, json=payload)


@step("Получить список заказов")
def get_orders_list():
    return requests.get(Urls.GET_ORDERS_LIST)


@step("Получить список заказов с несуществующим курьером")
def get_orders_list_with_unexisting_courier():
    return requests.get(Urls.GET_ORDERS_LIST, params={"courierId": "999999"})
