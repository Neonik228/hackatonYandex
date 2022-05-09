import json
import requests

# data = {
#     "method": "get",
#     "params": {
#         "SelectionCriteria": {
#             "Ids": [3613992]
#         },
#         "FieldNames": ["Id", "AdGroupId", "State", "Status", "Type"],
#         "TextAdFieldNames": ["AdImageHash", "Href", "Text", "Title"],
#         # "Page": {
#         #   "Limit": (long),
#         #   "Offset": (long)
#         # }
#     }
# }

# data = {
#   "method": "get",
#   "params": {
#     "SelectionCriteria": {
#       "AdImageHashes": ["P1qAsSY7rbsShnEJ3D25VA", "a47B_VmMVFHQc-ocLatFGg"],
#     },
#     "FieldNames": ["AdImageHash", "OriginalUrl", "PreviewUrl", "Name", "Type", "Subtype", "Associated"],
#   }
# }

payload = {
    'method': 'get',
    'params': {
        'SelectionCriteria': {},
        'FieldNames': ['State', 'Status'],
    },
}

token = "AQAAAAAoPF1mAAd_WI72IH3Q5UJuu4DxHHcEP9g"

headers = {"Authorization": "Bearer " + token,
           "Accept-Language": "ru"}
CampaignsURL = 'https://api-sandbox.direct.yandex.com/json/v5/campaigns'

jsonBody = json.dumps(payload, ensure_ascii=False).encode('utf8')

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
        dic = {"DRAFT": 0, "MODERATION": 0, "ACCEPTED": 0, "REJECTED": 0, "ACTIVE": 0, "SUSPENDED": 0, "ENDED": 0,
               "ARCHIVED": 0, "CONVERTED": 0, "UNKNOWN": 0}
        for item in result.json()["result"]["Campaigns"]:
            dic[item["Status"]] = dic.get(item["Status"], 0) + 1
        print(dic)


# Обработка ошибки, если не удалось соединиться с сервером API Директа
except ConnectionError:
    # В данном случае мы рекомендуем повторить запрос позднее
    print("Произошла ошибка соединения с сервером API.")

# Если возникла какая-либо другая ошибка
except Exception as e:
    print(e)
    # В данном случае мы рекомендуем проанализировать действия приложения
    print("Произошла непредвиденная ошибка.")
