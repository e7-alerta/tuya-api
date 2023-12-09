from enum import Enum

from pydantic import BaseModel


class DeviceEvent(Enum):
    PIR_STATE = "pir_state"
    DOORCONTACT_STATE = "doorcontact_state"
    ALARM_STATE = "alarm_state"
    TEMPER_ALARM = "temper_alarm"


class DeviceType(Enum):
    DOOR_CONTACT = ("door_contact", [DeviceEvent.DOORCONTACT_STATE, DeviceEvent.TEMPER_ALARM])
    MINI_ALARM = ("mini_alarm", [DeviceEvent.PIR_STATE])
    ALARM_BUTTON = ("alarm_button", [])
    PHONE_BUTTON = ("phone_button", [])
    MOTION_SENSOR = ("motion_sensor", [DeviceEvent.PIR_STATE])
    LIGHT_SENSOR = ("light_sensor", [])
    CAMERA = ("camera", [])
    WINDOW = ("window", [])
    GARAGE_DOOR = ("garage_door", [])
    DOOR_LOCK = ("door_lock", [])
    DOOR_BELL = ("door_bell", [])

    def __init__(self, value, event_codes: []):
        self._value_ = value
        self.event_codes = event_codes


class DeviceStatus(Enum):
    ENABLED = "enabled"
    ACTIVATED = "activated"
    DISABLED = "disabled"
    pass


class Device(BaseModel):
    id: str
    status: DeviceStatus
    alerted: bool
    device_type: DeviceType
    name: str
    tuya_id: str
    place_id: str
