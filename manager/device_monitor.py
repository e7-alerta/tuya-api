from dash.types import DeviceType
from repositories import devices_repository
from tuya import service as tuya_service
from services import alerts_service


def check_alerts(device, event_codes):
    if not event_codes:
        return False
    return len(event_codes) > 0


def sync_devices_status():
    """
    monitorear el estado de los dispositivos en tuya cloud api
    obtener los dispositivos tipo tuya de dash api
    consultar en tuya cloud api el estado de cada dispositivo
    si el estado es diferente al estado actual, actualizar el estado en dash api
    """
    alerted_devices = {
        "door_sensors": [],
        "motion_sensors": [],
        "sos_buttons": [],
        "mini_alarms": [],
    }


    print(" sincronizando estado de dispositivos tuya tipo mini alarmar")
    devices = devices_repository.find_all_enabled_tuya_devices(
        device_type=DeviceType.MINI_ALARM
    )
    print(f"devices encontrados:  {devices}")
    for device in devices:
        print(f"device {device.id} is a mini alarm enabled")
        if device.alerted:
            print(f"device {device.id} is already alerted")
            continue
        # obtener el estado del dispositivo en tuna cloud api
        [ event_codes, is_sos ] = tuya_service.get_device_status_log(device)
        is_alerted = check_alerts(device, event_codes)
        if is_alerted:
            # send alerta al servicio de alertas de dash
            device.alerted = True
            alerts_service.alert_device(device, is_sos)
            print(f"device {device.id} is alerted")
            alerted_devices["mini_alarms"].append(device)


    print(" sincronizando estado de dispositivos tuya tipo sensor de puerta")
    # check alertas de sensores de puertas
    devices = devices_repository.find_all_enabled_tuya_devices(
        device_type=DeviceType.DOOR_CONTACT
    )
    print(f"devices {devices}")
    for device in devices:
        print(f"device {device.id} is a door sensor enabled")
        if device.alerted:
            print(f"device {device.id} is already alerted")
            continue
        # obtener el estado del dispositivo en tuna cloud api
        [ event_codes, is_sos] = tuya_service.get_device_status_log(device)
        is_alerted = check_alerts(device, event_codes)
        if is_alerted:
            # send alerta al servicio de alertas de dash
            device.alerted = True
            alerts_service.alert_device(device, is_sos)
            print(f"device {device.id} is alerted")
            alerted_devices["door_sensors"].append(device)


    #    devices = devices_repository.find_all_enabled_tuya_devices(
    #        device_type=DeviceType.MOTION_SENSOR
    #    )
    #    print(f"devices {devices}")
    #    for device in devices:
    #        print(f"device {device.id} is a motion sensor enabled")
    #        if device.alerted:
    #            print(f"device {device.id} is already alerted")
    #            continue
    #        # obtener el estado del dispositivo en tuna cloud api
    #        event_codes = tuya_service.get_device_status_log(device)
    #        is_alerted = check_alerts(device, event_codes)
    #        if is_alerted:
    #            # send alerta al servicio de alertas de dash
    #            device.alerted = True
    #            alerts_service.alert_device(device)
    #            print(f"device {device.id} is alerted")
    #            alerted_devices["motion_sensors"].append(device)

    PIR_STATE = "pir_state"

    return {
        "data": {
            "alerted_devices": alerted_devices
        }
    }
