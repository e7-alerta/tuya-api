import requests

from dash.types import Device


def alert_device(device: Device, is_sos: bool):
    print("alert_device", device)
    response = requests.get(f"https://alerts.vecinos.com.ar/api/v1/alarms/tuya-device/{device.tuya_id}?sos={is_sos}")
    print("response", response)
    pass