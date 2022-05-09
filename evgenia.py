import hashlib
from datetime import date

import requests, json
from requests.exceptions import ConnectionError

token = 'AQAAAAAoPF1mAAd_WI72IH3Q5UJuu4DxHHcEP9g'

headers = {"Authorization": "Bearer " + token,  # OAuth-токен. Использование слова Bearer обязательно
           "Accept-Language": "ru",  # Язык ответных сообщений
           }


# campaigns = 429429
# adgroups = 4181693
# keyword = 10620322
# ad = 3615057


CampaignsURL = 'https://api-sandbox.direct.yandex.com/json/v5/ads'
jsonBody = json.dumps(payload, ensure_ascii=False).encode('utf8')

try:
    result = requests.post(CampaignsURL, jsonBody, headers=headers)

    print("Заголовки запроса: {}".format(result.request.headers))
    print("Запрос: {}".format(result.request.body))
    print("Заголовки ответа: {}".format(result.headers))
    print("Ответ: {}".format(result.text))
    print("\n")

    if result.status_code != 200 or result.json().get("error", False):
        print("Произошла ошибка при обращении к серверу API Директа.")
        print("Код ошибки: {}".format(result.json()["error"]["error_code"]))
        print("Описание ошибки: {}".format(result.json()["error"]["error_detail"]))
        print("RequestId: {}".format(result.headers.get("RequestId", False)))
    else:
        print("RequestId: {}".format(result.headers.get("RequestId", False)))
        print("Информация о баллах: {}".format(result.headers.get("Units", False)))
        print("-------------\n")
        for campaign in [result.json()["result"]["Campaigns"][0]]:
            # print("Рекламная кампания: {} State: {} Status: {} ID: {}".format(campaign['Name'], campaign['State'], campaign["Status"], campaign["Id"]))
            # print(campaign["SourceId"])
            for item in sorted(campaign.keys()):
                print(f"{item}: {campaign[item]}")
            print("\n")

        if result.json()['result'].get('LimitedBy', False):
            # Если ответ содержит параметр LimitedBy, значит,  были получены не все доступные объекты.
            # В этом случае следует выполнить дополнительные запросы для получения всех объектов.
            # Подробное описание постраничной выборки - https://tech.yandex.ru/direct/doc/dg/best-practice/get-docpage/#page
            print("Получены не все доступные объекты.")


except ConnectionError:
    print("Произошла ошибка соединения с сервером API.")

except:
    print("Произошла непредвиденная ошибка.")
