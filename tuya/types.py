from enum import Enum

from pydantic import BaseModel


class TuyaSensorEvent(Enum):
    DOORCONTACT_STATE = "doorcontact_state"
    TEMPER_ALARM = "temper_alarm"
    PIR_STATE = "pir_state"


class TuyaEventEntry(BaseModel):
    created_at: int
    activated: bool
    event: TuyaSensorEvent


class TuyaSensorType(Enum):
    door_sensor = "mcs"
    motion_sensor = "pir"
    temperature_sensor = "temp"


class TuyaSensorStatus(BaseModel):
    t: int
    last_refreshed_at: int
    battery_percentage: int


class TuyaSensorInfo(BaseModel):
    t: int
    tid: int
    uuid: str
    id: str
    local_key: str
    online: bool
    name: str
    model: str
    product_id: str
    product_name: str
    category: str
    active_time: int
    update_time: int
    create_time: int
    ip: str
    lat: float
    lon: float
    owner_id: str
    pv: str
    room_id: str
    sub: bool
    time_zone: str


class TuyaDoorSensorInfo(TuyaSensorInfo):
    pass


class TuyaDoorSensorStatus(TuyaSensorStatus):
    doorcontact_state: bool
    temper_alarm: bool
    pass
