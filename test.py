import json
from datetime import date

import requests

# payload = {
#     'method': 'add',
#     'params': {
#         'Campaigns': [{
#             'Name': "Смотрю на бюджет",
#             'StartDate': str(date.today()),
#             'TextCampaign': {
#                 'BiddingStrategy': {
#                     'Search': {
#                         'BiddingStrategyType': 'WB_MAXIMUM_CLICKS',
#                         'WbMaximumClicks': {
#                             'WeeklySpendLimit': 10000000000,
#                         },
#                     },
#                     'Network': {
#                         'BiddingStrategyType': 'NETWORK_DEFAULT',
#                         'NetworkDefault': {}
#                     }
#                 }
#             }
#         }]
#     }
# }
#
# response, result = await self._request('/campaigns', payload)
# return self._get_single_add_result(response, result)['Id']

# data = {
#   "method": "get",
#   "params": {
#     "SelectionCriteria": {
#       "AdImageHashes": ["P1qAsSY7rbsShnEJ3D25VA", "a47B_VmMVFHQc-ocLatFGg"],
#     },
#     "FieldNames": ["AdImageHash", "OriginalUrl", "PreviewUrl", "Name", "Type", "Subtype", "Associated"],
#   }
# }

data = {
    "method": "resume",
    "params": {
        "SelectionCriteria": {
            "Ids": [429304]
        }
    }
}

token = "AQAAAAAoPF1mAAd_WI72IH3Q5UJuu4DxHHcEP9g"

headers = {"Authorization": "Bearer " + token,
           "Accept-Language": "ru"}
CampaignsURL = 'https://api-sandbox.direct.yandex.com/json/v5/campaigns'

jsonBody = json.dumps(data, ensure_ascii=False).encode('utf8')

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
        print(result.json()['result']['AddResults'][0]['AdImageHash'])
        print(type(result.json()['result']['AddResults'][0]['AdImageHash']))


# Обработка ошибки, если не удалось соединиться с сервером API Директа
except ConnectionError:
    # В данном случае мы рекомендуем повторить запрос позднее
    print("Произошла ошибка соединения с сервером API.")

# Если возникла какая-либо другая ошибка
except Exception as e:
    print(e)
    # В данном случае мы рекомендуем проанализировать действия приложения
    print("Произошла непредвиденная ошибка.")
