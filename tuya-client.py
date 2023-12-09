from tuya_connector import (
	TuyaOpenAPI,
	TuyaOpenPulsar,
	TuyaCloudPulsarTopic,
)

ACCESS_ID = "m8ky7sd4j4vg98ck9vqu"
ACCESS_KEY = "67004a8a599a447db2422d63163a2608"
PROJECT = "p1700190146847dcr574"

API_ENDPOINT = "https://openapi.tuyaus.com"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285/"

MQ_ENV_PROD = "event"
MQ_ENV_TEST = "event-test"

# Init OpenAPI and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()


# Call any API from Tuya

# Get all devices
# response = openapi.get("/v1.0/devices", dict())
response = openapi.get("/v1.0/users/az1700188402100MNn65/devices", dict())
print(response)

response = openapi.get("/v1.0/devices/eb3553b506ae11cafbpmpc", dict())
print(response)

response = openapi.get("/v1.0/devices/eb3553b506ae11cafbpmpc/status", dict())

response = openapi.get("/v1.0/devices/status?device_ids=eb3553b506ae11cafbpmpc", dict())


# Init Message Queue
open_pulsar = TuyaOpenPulsar(
	ACCESS_ID, ACCESS_KEY, MQ_ENDPOINT, TuyaCloudPulsarTopic.PROD
)
# Add Message Queue listener
open_pulsar.add_message_listener(lambda msg: print(f"---\nexample receive: {msg}"))

# Start Message Queue
open_pulsar.start()


"""
Device status notification			
Generate MQTT Connection Configuration	POST:/v1.0/iot-03/open-hub/access-config


"""