from fastapi import FastAPI, APIRouter, HTTPException
from schemas import HouseCreate, HouseResponse

app = FastAPI()

house_router = APIRouter(prefix="/houses", tags=["Houses"])

houses_db = {}

# HOUSES CRUAD
@house_router.post("/", response_model=HouseResponse)
def create_house(house: HouseCreate):
    new_house_id = len(houses_db) + 1
    for house_id in houses_db:
        if houses_db[house_id]["address"] == house.address and houses_db[house_id]["city"] == house.city and houses_db[house_id]["state"] == house.state and houses_db[house_id]["zipcode"] == house.zipcode:
            raise HTTPException(status_code=400, detail="House already exists")
    new_house = {"house_id": new_house_id, **house.model_dump()}
    houses_db[new_house_id] = new_house
    return new_house

@house_router.get("/{house_id}", response_model=HouseResponse)
def get_house(house_id: int):
    house = houses_db.get(house_id)
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    return house

@house_router.put("/{house_id}", response_model=HouseResponse)
def update_house(house_id: int, house_data: HouseCreate):
    if house_id not in houses_db:
        raise HTTPException(status_code=404, detail="House not found")
    
    houses_db[house_id].update(house_data.model_dump())
    return houses_db[house_id]

@house_router.delete("/{house_id}")
def delete_house(house_id: int):
    if house_id not in houses_db:
        raise HTTPException(status_code=404, detail="House not found")
    
    del houses_db[house_id]
    return {"message": f"House {house_id} deleted successfully"}

@house_router.post("/{house_id}/rooms/{room_id}")
def assign_room_to_house(house_id: int, room_id: int):
    if house_id not in houses_db:
        raise HTTPException(status_code=404, detail="House not found")

    houses_db[house_id]["rooms"].append(room_id)
    return {"message": f"Room {room_id} assigned to House {house_id}"}

@house_router.get("/{house_id}/rooms")
def get_rooms_from_house(house_id: int):
    if house_id not in houses_db:
        raise HTTPException(status_code=404, detail="House not found")

    return houses_db[house_id]["rooms"]

app.include_router(house_router)