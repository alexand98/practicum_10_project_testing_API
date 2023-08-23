import data
import sender_stand_request

def get_kit_body(name):
    # копирование словаря с телом запроса из файла data
    current_body = data.kit_body.copy()
    # изменение значения в поле name
    current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_body
def test_create_kit_1_letter_in_name_get_success_response():
    # В переменную user_body сохраняется обновленное тело запроса с именем “Аа”
    user_body = get_kit_body("а")
    # В переменную user_response сохраняется результат запроса на создание пользователя
    user_response = sender_stand_request.post_new_kit(user_body)

    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201, "Status code is not 201"
    # Проверяется, что в ответе есть поле authToken, и оно не пустое
    assert user_response.json()["name"] == user_body["name"]