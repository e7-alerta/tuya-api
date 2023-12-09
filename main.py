from fastapi import FastAPI

from manager import device_monitor

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api/v1/iot/monitor")
async def monitoring_iot_devices():
    """
    monitorear el estado de los dispositivos en tuya cloud api
    """
    device_monitor.sync_devices_status()
    return {
        "data": [
            {
                "id": "5f5b4c9f-5c9b-4e2e-9d4a-2c4b0e7f6b4a",
                "status": "enabled",
                "alerted": False,
                "device_type": "door_contact",
                "name": "Puerta de entrada",
                "tuya_id": "01600000000000000000000000000001",
                "place_id": "5f5b4c9f-5c9b-4e2e-9d4a-2c4b0e7f6b4a"
            }
        ]
    }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8010)
