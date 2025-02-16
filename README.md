# **Smart Home API** 

## **Overview**  
This is a FastAPI-based Smart Home API that manages **Users, Houses, Rooms, and Devices**. The API allows CRUD operations and assignments between these entities.

## **Tech Stack**  
- **FastAPI** - Web framework
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **pytest** - Unit testing
- **GitHub Actions** - CI/CD automation

## **Base URL**  
```
http://localhost:8000
```

---

## **API Endpoints**  

### **Users API**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/users/` | Create a new user |
| `GET` | `/users/{user_id}` | Retrieve user details |
| `PUT` | `/users/{user_id}` | Update user details |
| `DELETE` | `/users/{user_id}` | Delete a user |
| `POST` | `/users/{user_id}/houses/{house_id}` | Assign a house to a user |
| `GET` | `/users/{user_id}/houses` | Get houses assigned to a user |

### **Houses API**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/houses/` | Create a new house |
| `GET` | `/houses/{house_id}` | Retrieve house details |
| `PUT` | `/houses/{house_id}` | Update house details |
| `DELETE` | `/houses/{house_id}` | Delete a house |
| `POST` | `/houses/{house_id}/rooms/{room_id}` | Assign a room to a house |
| `GET` | `/houses/{house_id}/rooms` | Get rooms assigned to a house |

### **Rooms API**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/rooms/` | Create a new room |
| `GET` | `/rooms/{room_id}` | Retrieve room details |
| `PUT` | `/rooms/{room_id}` | Update room details |
| `DELETE` | `/rooms/{room_id}` | Delete a room |
| `POST` | `/rooms/{room_id}/devices/{device_id}` | Assign a device to a room |
| `GET` | `/rooms/{room_id}/devices` | Get devices assigned to a room |

### **Devices API**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/devices/` | Create a new device |
| `GET` | `/devices/{device_id}` | Retrieve device details |
| `PUT` | `/devices/{device_id}` | Update device details |
| `DELETE` | `/devices/{device_id}` | Delete a device |

---

## **Data Models**  
### **User Model**  
```json
{
  "user_id": 1,
  "name": "John Doe",
  "username": "johndoe",
  "email": "john@example.com",
  "phone": "123-456-7890",
  "houses": [1, 2]
}
```

### **House Model**  
```json
{
  "house_id": 1,
  "address": "123 Ocean Drive",
  "city": "Boston",
  "state": "MA",
  "zipcode": "02215",
  "sqft": 2000,
  "rooms": [101, 102]
}
```

### **Room Model**  
```json
{
  "room_id": 1,
  "name": "Living Room",
  "area": 100,
  "devices": [201, 202]
}
```

### **Device Model**  
```json
{
  "device_id": 1
  "name": "Smart Thermostat",
  "type": "Thermostat",
  "status": "on",
}
```
