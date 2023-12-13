from datetime import datetime, timedelta
from urllib.parse import urlencode

from tuya.connector import TuyaConnector
from tuya.mapper import map_device_info_result, map_device_status_result
from tuya.types import TuyaDoorSensorStatus, TuyaDoorSensorInfo, TuyaSensorEvent, TuyaEventEntry

SIZE = 20
DOOR_CONTACT_STATE = "doorcontact_state"
ALERT_STATE = "alert_state"


class SensorClient:
    info_response = None
    status_response = None

    device_status: TuyaDoorSensorStatus = None
    device_info: TuyaDoorSensorInfo = None

    def __init__(self, tuya_connector: TuyaConnector, device_id):
        self.tuya = tuya_connector
        self.device_id = device_id

    def connect(self):
        self.tuya.connect()

    def get_device_info(self):
        response = self.tuya.get(f"/v1.0/devices/{self.device_id}", dict())

        if response.get("success"):
            device_info_result = response.get("result", {})
            self.device_info = map_device_info_result(device_info_result)
            self.device_status = map_device_status_result(device_info_result)
            self.info_response = response

        return self.device_info

    def get_device_status(self):
        response = self.tuya.get(f"/v1.0/devices/{self.device_id}/status", dict())

        if response.get("success"):
            device_status_result = response.get("result", {})
            self.device_status = map_device_status_result(device_status_result)
            self.status_response = response

        return self.device_status

    def get_report_logs(self, event_codes, check_sos=False):
        # Obtén la fecha y hora actual
        end_time = datetime.now()
        # Resta 5 minutos para obtener la fecha y hora de inicio
        start_time = end_time - timedelta(minutes=15)
        # Convierte las fechas y horas en milisegundos (si es necesario)
        end_time_timestamp = int(end_time.timestamp() * 1000)
        start_time_timestamp = int(start_time.timestamp() * 1000)
        # Imprime las fechas y horas en formato legible
        print("End Time:", end_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Start Time:", start_time.strftime("%Y-%m-%d %H:%M:%S"))
        # Imprime las fechas y horas en formato de timestamp (milisegundos)
        print("End Time Timestamp:", end_time_timestamp)
        print("Start Time Timestamp:", start_time_timestamp)

        # querystring = {
        #     "codes": DOOR_CONTACT_STATE,
        #     "start_time":  start_time,
        #     "end_time":  end_time,
        #     "size": SIZE
        # }
        # url = f"/v2.0/cloud/thing/{self.device_id}/report-logs"
        # to = f"{url}?{urlencode(querystring)}"
        # print("to[v1]: ", to)
        # to2 = f"/v2.0/cloud/thing/eb3553b506ae11cafbpmpc/report-logs?codes=doorcontact_state&end_time=1701858559290&size=20&start_time=1701685759290"
        # to3 = f"/v2.0/cloud/thing/eb3553b506ae11cafbpmpc/report-logs?codes=doorcontact_state&end_time={end_time_timestamp}&size=20&start_time={start_time_timestamp}"

        if len(event_codes) == 1:
            to3 = f"/v2.0/cloud/thing/{self.device_id}/report-logs?codes={event_codes[0].value}&end_time={end_time_timestamp}&size=20&start_time={start_time_timestamp}"
        if len(event_codes) == 2:
            to3 = f"/v2.0/cloud/thing/{self.device_id}/report-logs?codes={event_codes[0].value},{event_codes[1].value}&end_time={end_time_timestamp}&size=20&start_time={start_time_timestamp}"
        if len(event_codes) == 3:
            to3 = f"/v2.0/cloud/thing/{self.device_id}/report-logs?codes={event_codes[0].value},{event_codes[1].value},{event_codes[2].value}&end_time={end_time_timestamp}&size=20&start_time={start_time_timestamp}"

        print("to3[v3]: ", to3)
        response = self.tuya.get(to3, dict())
        print("response: ", response)
        if response.get("success"):
            print("success")
            result = response.get("result", {})
            logs = result.get("logs", [])
            # si no hay logs, no hay nada que hacer
            if len(logs) == 0:
                return [None, None]
            # recorro los logs para obtener los diferentes codigos  de estado
            # no hace falta repetir el mismo codigo de estado
            codes = set()
            for log in logs:
                if check_sos:
                    if log.get("code") == "pir_state" and log.get("value") != "none":
                        codes.add(log.get("code"))
                        return [codes, True]
                else:
                    codes.add(log.get("code"))
            return [codes, False]

        else:
            return [None,None]

        # if response.get("success"):
        #     raw_logs = response.get("result", {}).get("logs", [])
        #     for log in raw_logs:
        #         logs.append(
        #             TuyaEventEntry(
        #                 created_at=datetime.fromtimestamp(log.get("t")),
        #                 event=TuyaSensorEvent(log.get("code")),
        #                 activated=log.get("value") == "true"
        #             )
        #         )
        # return logs
