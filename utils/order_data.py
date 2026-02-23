from faker import Faker

fake = Faker("ru_RU")


def build_order_payload():
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.random_int(min=1, max=237),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=7),
        "deliveryDate": fake.date(pattern="%Y-%m-%d"),
        "comment": fake.text(max_nb_chars=20),
    }


COLOR_VARIANTS = [
    (["BLACK"], "Черный цвет"),
    (["GREY"], "Серый цвет"),
    (["BLACK", "GREY"], "Оба цвета"),
    ([], "Без цвета"),
]
