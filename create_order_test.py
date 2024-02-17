# Елизавета Рудь, 13-я когорта - Финальный проект, Инженер по тестированию плюс

import data
import sender_stand_request

# Тест "Клиент создает заказ. Проверяется, что по треку заказа можно получить данные о заказе"
def test_create_new_order():
    # Присвоение переменной body данных заказа
    body = data.order_body
    # В переменную response сохраняется результат запроса
    response = sender_stand_request.post_new_order(body)
    # В переменную number_track сохраняется номер трека заказа
    number_track = response.json()["track"]
    # В переменную order сохраняется запрос на получения заказа по треку заказа.
    order = sender_stand_request.get_order_info(number_track)
    # Проверка, что код ответа равен 200
    assert order.status_code == 200