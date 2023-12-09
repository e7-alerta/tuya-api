from enum import Enum

import requests

from dash.mapper import device_load
from dash.types import DeviceStatus


def get_devices(
        status: DeviceStatus = None,
        tuya_device: bool = None,
        device_type: str = None
):
    # status = "activated"

    url = "http://dash.vecinos.com.ar/items/iot_devices"

    querystring = {
        "limit": "20"
    }

    print("device_type value is: ", device_type.value)
    if device_type:
        querystring["filter[device_type][_eq]"] = device_type.value

    if tuya_device:
        querystring["filter[tuya_device][_eq]"] = tuya_device

    if status:
        querystring["filter[status][_eq]"] = status.value

    response = requests.request("GET", url, params=querystring)
    data = response.json()["data"]
    print(data)

    devices = []
    for item in data:
        device = device_load(item)
        devices.append(
            device
        )
    return devices


def mark_device_alerted(device_id: str):
    # url = f"https://dash.vecinos.com.ar/items/iot_devices/{device_id}"
    url = f"http://dash.vecinos.com.ar/items/iot_devices/{device_id}"
    payload = {
        "alerted": True,
        "status": DeviceStatus.ACTIVATED.value
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("PATCH", url, headers=headers, json=payload)
    return response


if __name__ == '__main__':
    devices = get_devices()
    print(devices)
    mark_device_alerted(devices[0].id)
