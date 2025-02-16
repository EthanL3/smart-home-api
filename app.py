from fastapi import FastAPI
from routes.house_routes import house_router
from routes.room_routes import room_router
from routes.user_routes import user_router
from routes.device_routes import device_router

app = FastAPI(title="Smart Home API")

# Registering Routers
app.include_router(house_router)
app.include_router(room_router)
app.include_router(user_router)
app.include_router(device_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)