from dash.types import DeviceType, Device
from tuya.connector import TuyaConnector, API_ENDPOINT, ACCESS_ID, ACCESS_KEY
from tuya.door_sensor_handler import SensorClient as DoorSensorClient

connector: TuyaConnector = None

connector = TuyaConnector(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
connector.connect()


def get_device_status_log(device: Device):
    print("get_device_status_log of ", device)

    if DeviceType.DOOR_CONTACT == device.device_type or DeviceType.MOTION_SENSOR == device.device_type or DeviceType.MINI_ALARM == device.device_type:
        print("device is door contact")
        sensorClient = DoorSensorClient(connector, device.tuya_id)
        if DeviceType.MINI_ALARM == device.device_type:
            [event_codes, is_sos] = sensorClient.get_report_logs(device.device_type.event_codes, check_sos=True)
        else:
            [event_codes, is_sos] = sensorClient.get_report_logs(device.device_type.event_codes, check_sos=False)
        print(" event codes: ", event_codes, " is sos: ", is_sos)
        return [event_codes, is_sos]
    pass
