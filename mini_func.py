import requests, json
from requests.exceptions import ConnectionError
import traceback
from datetime import date

token = "AQAAAAAoPF1mAAd_WI72IH3Q5UJuu4DxHHcEP9g"

headers = {"Authorization": "Bearer " + token,
           "Accept-Language": "ru"}

CampaignsURL = 'https://api-sandbox.direct.yandex.com/json/v5/ads'
body = {
    "method": "resume",
    "params": {
        "SelectionCriteria": {
            "Ids": [3613992]
        }
    }
}

# keywords = [{
#     'Keyword': "---autotargeting",
#     'AdGroupId': 4180705,
# }]
#
# payload = {
#     'method': 'add',
#     'params': {'Keywords': keywords},
# }
# URL = 'https://api-sandbox.direct.yandex.com/json/v5/keywords'
# jsonBody = json.dumps(payload, ensure_ascii=False).encode('utf8')
#
# try:
#     result = requests.post(URL, jsonBody, headers=headers)
#
#     # Отладочная информация
#     print("Заголовки запроса: {}".format(result.request.headers))
#     print("Запрос: {}".format(result.request.body))
#     print("Заголовки ответа: {}".format(result.headers))
#     print("Ответ: {}".format(result.text))
#     print("\n")
#     print("Id_campaigns: {}".format(result.json()["result"]["AddResults"][0]["Id"]))
#
#     # Обработка запроса
#     if result.status_code != 200 or result.json().get("error", False):
#         print("Произошла ошибка при обращении к серверу API Директа.")
#         print("Код ошибки: {}".format(result.json()["error"]["error_code"]))
#         print("Описание ошибки: {}".format(result.json()["error"]["error_detail"]))
#         print("RequestId: {}".format(result.headers.get("RequestId", False)))
#     else:
#         print("RequestId: {}".format(result.headers.get("RequestId", False)))
#         print("Информация о баллах: {}".format(result.headers.get("Units", False)))
#         campaign_id = result.json()["result"]["AddResults"][0]["Id"]
# except:
#     # В данном случае мы рекомендуем проанализировать действия приложения
#     print(traceback.print_exc())
#     print("Произошла непредвиденная ошибка.")
#
#
# body = {
#     'method': 'moderate',
#     'params': {
#         'SelectionCriteria': {
#             'Ids': [3613992],
#         },
#     },
# }
#
# jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')
#
# try:
#     result = requests.post(CampaignsURL, jsonBody, headers=headers)
#
#     # Отладочная информация
#     print("Заголовки запроса: {}".format(result.request.headers))
#     print("Запрос: {}".format(result.request.body))
#     print("Заголовки ответа: {}".format(result.headers))
#     print("Ответ: {}".format(result.text))
#     print("\n")
#     print("Id_campaigns: {}".format(result.json()["result"]["AddResults"][0]["Id"]))
#
#     # Обработка запроса
#     if result.status_code != 200 or result.json().get("error", False):
#         print("Произошла ошибка при обращении к серверу API Директа.")
#         print("Код ошибки: {}".format(result.json()["error"]["error_code"]))
#         print("Описание ошибки: {}".format(result.json()["error"]["error_detail"]))
#         print("RequestId: {}".format(result.headers.get("RequestId", False)))
#     else:
#         print("RequestId: {}".format(result.headers.get("RequestId", False)))
#         print("Информация о баллах: {}".format(result.headers.get("Units", False)))
#         campaign_id = result.json()["result"]["AddResults"][0]["Id"]
# except:
#     # В данном случае мы рекомендуем проанализировать действия приложения
#     print(traceback.print_exc())
#     print("Произошла непредвиденная ошибка.")
#
payload = {
    "method": "get",
    "params": {
        "SelectionCriteria": {
            "Types": ["TEXT_CAMPAIGN"]
        },
        "FieldNames": ["Id", "Name"],
        # "TextAdFieldNames": ["AdImageHash", "Href", "Text", "Title"],
        # "Page": {
        #   "Limit": (long),
        #   "Offset": (long)
        # }
    }
}
#
jsonBody = json.dumps(payload, ensure_ascii=False).encode('utf8')
CampaignsURL = "https://api-sandbox.direct.yandex.com/json/v5/campaigns"
try:
    result = requests.post(CampaignsURL, jsonBody, headers=headers)

    # Отладочная информация
    print("Заголовки запроса: {}".format(result.request.headers))
    print("Запрос: {}".format(result.request.body))
    print("Заголовки ответа: {}".format(result.headers))
    print("Ответ: {}".format(result.text))
    print("\n")

    # Обработка запроса
    if result.status_code != 200 or result.json().get("error", False):
        print("Произошла ошибка при обращении к серверу API Директа.")
        print("Код ошибки: {}".format(result.json()["error"]["error_code"]))
        print("Описание ошибки: {}".format(result.json()["error"]["error_detail"]))
        print("RequestId: {}".format(result.headers.get("RequestId", False)))
    else:
        print("RequestId: {}".format(result.headers.get("RequestId", False)))
        print("Информация о баллах: {}".format(result.headers.get("Units", False)))
        arr = []
        for item in result.json()["result"]["Campaigns"]:
            arr.append(item["Id"])
        print(arr)
        print(len(arr))
except:
    # В данном случае мы рекомендуем проанализировать действия приложения
    print(traceback.print_exc())
    print("Произошла непредвиденная ошибка.")



payload = {
    "method": "get",
    "params": {
        "SelectionCriteria": {
            "Types": ["TEXT_CAMPAIGN"]
        },
        "FieldNames": ["Id", "Name"],
        # "TextAdFieldNames": ["AdImageHash", "Href", "Text", "Title"],
        # "Page": {
        #   "Limit": (long),
        #   "Offset": (long)
        # }
    }
}
#
jsonBody = json.dumps(payload, ensure_ascii=False).encode('utf8')
CampaignsURL = "https://api-sandbox.direct.yandex.com/json/v5/campaigns"
try:
    result = requests.post(CampaignsURL, jsonBody, headers=headers)

    # Отладочная информация
    print("Заголовки запроса: {}".format(result.request.headers))
    print("Запрос: {}".format(result.request.body))
    print("Заголовки ответа: {}".format(result.headers))
    print("Ответ: {}".format(result.text))
    print("\n")

    # Обработка запроса
    if result.status_code != 200 or result.json().get("error", False):
        print("Произошла ошибка при обращении к серверу API Директа.")
        print("Код ошибки: {}".format(result.json()["error"]["error_code"]))
        print("Описание ошибки: {}".format(result.json()["error"]["error_detail"]))
        print("RequestId: {}".format(result.headers.get("RequestId", False)))
    else:
        print("RequestId: {}".format(result.headers.get("RequestId", False)))
        print("Информация о баллах: {}".format(result.headers.get("Units", False)))
        arr = []
        for item in result.json()["result"]["Campaigns"]:
            arr.append(item["Id"])
        print(arr)
        print(len(arr))
except:
    # В данном случае мы рекомендуем проанализировать действия приложения
    print(traceback.print_exc())
    print("Произошла непредвиденная ошибка.")