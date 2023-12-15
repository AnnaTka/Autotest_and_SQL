import requests
import configuration
import data


# Создание нового заказа

def post_new_order(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                             json=body)
    return response


# Получение номера трека заказа


def order_track_number():
    current_body = data.order_body
    response_create_order = post_new_order(current_body)
    return response_create_order.json()["track"]


