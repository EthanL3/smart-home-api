from fastapi import FastAPI, APIRouter, HTTPException
from schemas import UserCreate, UserResponse

app = FastAPI()

user_router = APIRouter(prefix="/users", tags=["Users"])

users_db = {}

# User CRUAD
@user_router.post("", response_model=UserResponse)
def create_user(user: UserCreate):
    new_user_id = len(users_db) + 1
    new_user = {"user_id": new_user_id, **user.model_dump()}
    users_db[new_user_id] = new_user
    return new_user

@user_router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserCreate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    users_db[user_id].update(user_data.model_dump())
    return users_db[user_id]

@user_router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    del users_db[user_id]
    return {"message": f"User {user_id} deleted successfully"}

@user_router.post("/{user_id}/houses/{house_id}")
def assign_house_to_user(user_id: int, house_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    users_db[user_id]["houses"].append(house_id)
    return {"message": f"House {house_id} assigned to User {user_id}"}

@user_router.post("/{user_id}/houses")
def get_houses_from_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    return users_db[user_id]["houses"]


app.include_router(user_router)