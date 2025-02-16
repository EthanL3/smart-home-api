from fastapi import FastAPI, APIRouter, HTTPException
from schemas import DeviceCreate, DeviceResponse

app = FastAPI()

device_router = APIRouter(prefix="/devices", tags=["Devices"])

# Stub storage
devices_db = {}

# DEVICES CRUD
@device_router.post("/", response_model=DeviceResponse)
def create_device(device: DeviceCreate):
    new_device_id = len(devices_db) + 1
    new_device = {"device_id": new_device_id, **device.model_dump()}
    devices_db[new_device_id] = new_device
    return new_device

@device_router.get("/{device_id}", response_model=DeviceResponse)
def get_device(device_id: int):
    device = devices_db.get(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@device_router.put("/{device_id}", response_model=DeviceResponse)
def update_device(device_id: int, device_data: DeviceCreate):
    if device_id not in devices_db:
        raise HTTPException(status_code=404, detail="Device not found")
    
    devices_db[device_id].update(device_data.model_dump())
    return devices_db[device_id]

@device_router.delete("/{device_id}")
def delete_device(device_id: int):
    if device_id not in devices_db:
        raise HTTPException(status_code=404, detail="Device not found")
    
    del devices_db[device_id]
    return {"message": f"Device {device_id} deleted successfully"}


app.include_router(device_router)