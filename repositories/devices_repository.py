from dash.api import devices_api
from dash.types import DeviceType, DeviceStatus


def find_all_enabled_tuya_devices(
        device_type: DeviceType = None
):
    """
    Find all enabled tuya devices.
    :return: the devices
    """
    return devices_api.get_devices(
        status=DeviceStatus.ENABLED,
        tuya_device=True,
        device_type=device_type
    )