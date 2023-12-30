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
    sync_result = device_monitor.sync_devices_status()
    return {
        "data":  sync_result["data"]
    }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8010)
