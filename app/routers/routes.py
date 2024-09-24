from fastapi import APIRouter

from app.routers.incident_notification import router as incident_notification_router

routers = APIRouter()
routers.include_router(incident_notification_router)