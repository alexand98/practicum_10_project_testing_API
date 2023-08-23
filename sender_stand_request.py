import requests
import configuration
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

def post_new_kit(body, kit_headers):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=kit_headers)  # а здесь заголовки
