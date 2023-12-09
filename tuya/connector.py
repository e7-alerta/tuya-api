from tuya_connector import ( TuyaOpenAPI )

ACCESS_ID = "m8ky7sd4j4vg98ck9vqu"
ACCESS_KEY = "67004a8a599a447db2422d63163a2608"
PROJECT = "p1700190146847dcr574"

API_ENDPOINT = "https://openapi.tuyaus.com"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285/"


class TuyaConnector:
    expire_time = None
    access_token = None
    refresh_token = None
    last_refreshed_at = None
    connected = False

    def __init__(self, api_endpoint, access_id, access_key):
        self.connected = False
        self.connection_response = None
        self.tuya = TuyaOpenAPI(api_endpoint, access_id, access_key)

    def connect(self):
        print("Connecting to Tuya API")
        self.connection_response = self.tuya.connect()
        self.expire_time = self.connection_response["result"]["expire_time"]
        self.access_token = self.connection_response["result"]["access_token"]
        self.refresh_token = self.connection_response["result"]["refresh_token"]
        self.last_refreshed_at = self.connection_response["t"]
        self.connected = True

    def get(self, url, params):
        return self.tuya.get(url, params)

