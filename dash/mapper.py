from dash.types import Device, DeviceStatus, DeviceType

"""
{
    "id": "1f3d153c-e925-43bd-ba05-f39bebda7450",
    "status": "published",
    "date_created": "2023-10-26T02:10:23.657Z",
    "date_updated": "2023-12-03T07:39:59.782Z",
    "place": "0fc19e07-8fe1-49d7-a87f-9b254c07faa9",
    "alerted": false,
    "has_neighborhood_alert": false,
    "device_name": "valkyrie-vf1s",
    "device_type": "door_window",
    "params": {
        "wifi": {
            "ssid": "",
            "password": ""
        },
        "has_ble": true
    },
    "tuya_id": "eb3553b506ae11cafbpmpc",
    "door_sensor": true,
    "motion_sensor": false,
    "store_button": false,
    "tuya_device": true
}

"""


def device_load(item):
    device_type = None
    if item['device_type'] == "mini_alarm":
        device_type = DeviceType.MINI_ALARM
    if item["device_type"] == "door_contact":
        device_type = DeviceType.DOOR_CONTACT
    elif item["device_type"] == "store_button":
        device_type = DeviceType.ALARM_BUTTON
    elif item["device_type"] == "motion_sensor":
        device_type = DeviceType.MOTION_SENSOR
    elif item["device_type"] == "phone_button":
        device_type = DeviceType.ALARM_BUTTON
    print(item)
    return Device(
        id=item["id"],
        status=DeviceStatus(item["status"]),
        device_type=device_type,
        alerted=item["alerted"],
        name=item["device_name"],
        tuya_id=item["tuya_id"],
        place_id=item["place"]
    )
