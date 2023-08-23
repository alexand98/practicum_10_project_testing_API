import requests
import configuration
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def post_new_kit(body):
    post_new_user_response = post_new_user(data.user_body).json()
    authToken = post_new_user_response['authToken']
    kit_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {authToken}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=kit_headers)  # а здесь заголовки
response2 = post_new_kit(data.kit_body)
print(response2.status_code)
print(response2.json())