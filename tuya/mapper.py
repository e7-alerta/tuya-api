from tuya.types import TuyaDoorSensorStatus, TuyaDoorSensorInfo


def map_device_info_result(item):
    print(item)
    return TuyaDoorSensorInfo(
        t=item.get("update_time", 0),
        tid=item.get("biz_type", 0),
        uuid=item.get("uuid", ""),
        id=item.get("id", ""),
        local_key=item.get("local_key", ""),
        online=item.get("online", False),
        name=item.get("name", ""),
        model=item.get("model", ""),
        product_id=item.get("product_id", ""),
        product_name=item.get("product_name", ""),
        category=item.get("category", ""),
        active_time=item.get("active_time", 0),
        update_time=item.get("update_time", 0),
        create_time=item.get("create_time", 0),
        ip=item.get("ip", ""),
        lat=float(item.get("lat", 0)),
        lon=float(item.get("lon", 0)),
        owner_id=item.get("owner_id", ""),
        pv=item.get("pv", ""),
        room_id=item.get("room_id", ""),
        sub=item.get("sub", False),
        time_zone=item.get("time_zone", "")
    )


def map_device_status_result(result):
    doorcontact_state = False
    battery_percentage = 0
    temper_alarm = False

    for status in result.get("status", []):
        code = status.get("code", "")
        value = status.get("value")

        if code == 'doorcontact_state':
            doorcontact_state = value
        elif code == 'battery_percentage':
            battery_percentage = value
        elif code == 'temper_alarm':
            temper_alarm = value

    return TuyaDoorSensorStatus(
        t=result.get("t", 0),
        last_refreshed_at=result.get("last_refreshed_at", 0),
        battery_percentage=battery_percentage,
        doorcontact_state=doorcontact_state,
        temper_alarm=temper_alarm
    )