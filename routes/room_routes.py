from fastapi import FastAPI, APIRouter, HTTPException
from schemas import RoomCreate, RoomResponse

app = FastAPI()

room_router = APIRouter(prefix="/rooms", tags=["Rooms"])

rooms_db = {}

# ROOMS CRUAD
@room_router.post("/", response_model=RoomResponse)
def create_room(room: RoomCreate):
    new_room_id = len(rooms_db) + 1
    new_room = {"room_id": new_room_id, **room.model_dump()}
    rooms_db[new_room_id] = new_room
    return new_room

@room_router.get("/{room_id}", response_model=RoomResponse)
def get_room(room_id: int):
    room = rooms_db.get(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@room_router.put("/{room_id}", response_model=RoomResponse)
def update_room(room_id: int, room_data: RoomCreate):
    if room_id not in rooms_db:
        raise HTTPException(status_code=404, detail="Room not found")
    
    rooms_db[room_id].update(room_data.model_dump())
    return rooms_db[room_id]

@room_router.delete("/{room_id}")
def delete_room(room_id: int):
    if room_id not in rooms_db:
        raise HTTPException(status_code=404, detail="Room not found")
    
    del rooms_db[room_id]
    return {"message": f"Room {room_id} deleted successfully"}

@room_router.post("/{room_id}/devices/{device_id}")
def assign_device_to_room(room_id: int, device_id: int):
    if room_id not in rooms_db:
        raise HTTPException(status_code=404, detail="Room not found")

    rooms_db[room_id]["devices"].append(device_id)
    return {"message": f"Device {device_id} assigned to Room {room_id}"}

@room_router.post("/{room_id}/devices")
def get_devices_from_room(room_id: int):
    if room_id not in rooms_db:
        raise HTTPException(status_code=404, detail="User not found")

    return rooms_db[room_id]["devices"]


app.include_router(room_router)