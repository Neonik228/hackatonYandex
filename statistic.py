import datetime

import requests
from requests.exceptions import ConnectionError
from time import sleep
import json
import sys


if sys.version_info < (3,):
    def u(x):
        try:
            return x.encode("utf8")
        except UnicodeDecodeError:
            return x
else:
    def u(x):
        if type(x) == type(b''):
            return x.decode('utf8')
        else:
            return x

ReportsURL = 'https://api-sandbox.direct.yandex.com/json/v5/reports'
token = 'AQAAAAAoPF1mAAd_WI72IH3Q5UJuu4DxHHcEP9g'

headers = {
    "Authorization": "Bearer " + token,
    "Accept-Language": "ru",
    "processingMode": "auto",
    # Формат денежных значений в отчете
    "returnMoneyInMicros": "false",
    # Не выводить в отчете строку с названием отчета и диапазоном дат
    "skipReportHeader": "true",
    # Не выводить в отчете строку с названиями полей
    "skipColumnHeader": "true",
    # Не выводить в отчете строку с количеством строк статистики
    "skipReportSummary": "true"
}

# # body = {
# #     "params": {
# #         "SelectionCriteria": {
# #             "Filter": [{
# #                 "Field": "CampaignId",
# #                 "Operator": "IN",
# #                 "Values": ["428878"]
# #             }],
# #             "DateFrom": "2021-11-21",
# #             "DateTo": "2021-11-23"
# #         },
# #         "FieldNames": [
# #             "Date",
# #             "CampaignName",
# #             "LocationOfPresenceName",
# #             "Impressions",
# #             "Clicks",
# #             "Cost",
# #             "AdNetworkType",
# #             "AvgCpc",
# #             "Device",
# #             "Gender",
# #             "IncomeGrade",
# #             "Profit",
# #             "Placement",
# #             "Slot"
# #         ],
# #         "ReportName": u("НАЗВАНИЕ_ОТЧЕТА"),
# #         "ReportType": "AD_PERFORMANCE_REPORT",
# #         "DateRangeType": "CUSTOM_DATE",
# #         "Format": "TSV",
# #         "IncludeVAT": "NO",
# #         "IncludeDiscount": "NO"
# #     }
# # }


body = {
    "params": {
        "SelectionCriteria": {
            "Filter": [{
                "Field": "CampaignId",
                "Operator": "EQUALS",
                "Values": ["428878"]
            }],
        },
        "FieldNames": [
            "Impressions", "Date"
        ],
        "ReportName": "Statistec_status_d126",
        "ReportType": "CAMPAIGN_PERFORMANCE_REPORT",
        "DateRangeType": "LAST_7_DAYS",
        "Format": "TSV",
        "IncludeVAT": "NO",
        "IncludeDiscount": "NO"
    }
}
body = json.dumps(body, indent=4)

while True:
    try:
        req = requests.post(ReportsURL, body, headers=headers)
        req.encoding = 'utf-8'  # Принудительная обработка ответа в кодировке UTF-8
        if req.status_code == 400:
            print("Параметры запроса указаны неверно или достигнут лимит отчетов в очереди")
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            print("JSON-код запроса: {}".format(u(body)))
            print("JSON-код ответа сервера: \n{}".format(u(req.json())))
            break
        elif req.status_code == 200:
            print("Отчет создан успешно")
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            print("Содержание отчета: \n{}".format(u(req.text)))
            dic = dict()
            for item in req.text.split("\n"):
                print(item.split("\t"))
                if item:
                    num, typ = item.split("\t")
                    dic[typ] = num
            print(dic)
            break
        elif req.status_code == 201:
            print("Отчет успешно поставлен в очередь в режиме офлайн")
            retryIn = int(req.headers.get("retryIn", 60))
            print("Повторная отправка запроса через {} секунд".format(retryIn))
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            sleep(retryIn)
        elif req.status_code == 202:
            print("Отчет формируется в режиме офлайн")
            retryIn = int(req.headers.get("retryIn", 60))
            print("Повторная отправка запроса через {} секунд".format(retryIn))
            print("RequestId:  {}".format(req.headers.get("RequestId", False)))
            sleep(retryIn)
        elif req.status_code == 500:
            print("При формировании отчета произошла ошибка. Пожалуйста, попробуйте повторить запрос позднее")
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            print("JSON-код ответа сервера: \n{}".format(u(req.json())))
            break
        elif req.status_code == 502:
            print("Время формирования отчета превысило серверное ограничение.")
            print(
                "Пожалуйста, попробуйте изменить параметры запроса - уменьшить период и количество запрашиваемых данных.")
            print("JSON-код запроса: {}".format(body))
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            print("JSON-код ответа сервера: \n{}".format(u(req.json())))
            break
        else:
            print("Произошла непредвиденная ошибка")
            print("RequestId:  {}".format(req.headers.get("RequestId", False)))
            print("JSON-код запроса: {}".format(body))
            print("JSON-код ответа сервера: \n{}".format(u(req.json())))
            break
    except ConnectionError:
        print("Произошла ошибка соединения с сервером API")
        break
    except:
        import traceback
        traceback.print_exc()
        print("Произошла непредвиденная ошибка")
        break

# CampaignsURL = 'https://api-sandbox.direct.yandex.ru/live/v4/json/'
#
# token = 'AQAAAAAoPF1mAAd_WI72IH3Q5UJuu4DxHHcEP9g'
#
#
# import hashlib
#
# masterToken = 'RrQkPwBT9OkmiIjz'
# operationNum = 8
# usedMethod = 'PayCampaigns'
# login = 'neoniklis'
# financeToken = hashlib.sha256(
#     masterToken.encode('utf8') + str(operationNum).encode('utf8') + usedMethod.encode('utf8') + login.encode(
#         'utf8')).hexdigest()
# wq = 0
# while True:
#     financeToken = hashlib.sha256(
#         masterToken.encode('utf8') + str(operationNum + wq).encode('utf8') + usedMethod.encode('utf8') + login.encode(
#             'utf8')).hexdigest()
#     body = {
#         "method": "PayCampaigns",
#         "finance_token": financeToken,
#         "operation_num": operationNum + wq,
#         "param": {
#             "Payments": [{
#                 "CampaignID": 429304,
#                 "Sum": 1000,
#                 "Currency": "RUB"
#             }],
#             "ContractID": "11111/00",
#             "PayMethod": "Bank"
#         },
#         "token": token,
#         "locate": "ru"
#     }
#
#     jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')
#
#     try:
#         result = requests.post(CampaignsURL, jsonBody)
#
#         print("Заголовки запроса: {}".format(result.request.headers))
#         print("Запрос: {}".format(result.request.body))
#         print("Заголовки ответа: {}".format(result.headers))
#         print("Ответ: {}".format(result.text))
#         print(operationNum)
#         print("\n")
#
#         if result.status_code != 200 or result.json().get("error", False):
#             print("Произошла ошибка при обращении к серверу API Директа.")
#             print("Код ошибки: {}".format(result.json()["error"]["error_code"]))
#             print("Описание ошибки: {}".format(result.json()["error"]["error_detail"]))
#             print("RequestId: {}".format(result.headers.get("RequestId", False)))
#         else:
#             print("RequestId: {}".format(result.headers.get("RequestId", False)))
#             print("Информация о баллах: {}".format(result.headers.get("Units", False)))
#             print("-------------\n")
#             for campaign in [result.json()["result"]["Campaigns"][0], result.json()["result"]["Campaigns"][-2]]:
#                 # print("Рекламная кампания: {} State: {} Status: {} ID: {}".format(campaign['Name'], campaign['State'], campaign["Status"], campaign["Id"]))
#                 # print(campaign["SourceId"])
#                 for item in sorted(campaign.keys()):
#                     print(f"{item}: {campaign[item]}")
#                 print("\n")
#
#             if result.json()['result'].get('LimitedBy', False):
#                 # Если ответ содержит параметр LimitedBy, значит,  были получены не все доступные объекты.
#                 # В этом случае следует выполнить дополнительные запросы для получения всех объектов.
#                 # Подробное описание постраничной выборки - https://tech.yandex.ru/direct/doc/dg/best-practice/get-docpage/#page
#                 print("Получены не все доступные объекты.")
#     except ConnectionError:
#         print("Произошла ошибка соединения с сервером API.")
#     except:
#         if result.json()["error_code"] == 351:
#             wq += 1
#         print("Произошла непредвиденная ошибка.")
