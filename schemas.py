from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class UserBase(BaseModel):
    name: str
    username: str
    email: str
    phone: str
    houses: List[int] = []  # Assuming the user can have multiple houses

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    user_id: int

    model_config = ConfigDict(from_attributes=True)

class HouseBase(BaseModel):
    address: str
    city: str
    state: str
    zipcode: str
    sqft: int
    rooms: List[int] = []  # List of room IDs

class HouseCreate(HouseBase):
    pass

class HouseResponse(HouseBase):
    house_id: int
    model_config = ConfigDict(from_attributes=True)

class RoomBase(BaseModel):
    name: str
    area: int
    devices: List[int] = []  # List of device IDs

class RoomCreate(RoomBase):
    pass

class RoomResponse(RoomBase):
    room_id: int

    model_config = ConfigDict(from_attributes=True)

class DeviceBase(BaseModel):
    name: str
    type: str
    status: str

class DeviceCreate(DeviceBase):
    pass

class DeviceResponse(DeviceBase):
    device_id: int

    model_config = ConfigDict(from_attributes=True)