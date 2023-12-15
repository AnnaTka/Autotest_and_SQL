# Ткачук Анна, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import request_sender


# Получение заказа по треку

def get_order_by_track_number(track):
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_NUMBER_PATH,
                            params=track)
    return response


# Тест. Успешное получение заказа по его треку

def test_get_order_by_track_number():
    created_track = request_sender.order_track_number()
    track = {"t": created_track}
    response_get_order = get_order_by_track_number(track)
    assert response_get_order.status_code == 200, "Failed to get order."

