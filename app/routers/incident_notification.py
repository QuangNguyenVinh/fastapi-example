from dependency_injector.wiring import Provide, inject
from app.services.incident_notification_service import IncidentNotificationService
from fastapi import APIRouter, Depends
from app.core.container import Container

router = APIRouter(
    prefix="/incident-notification",
    tags=["incident notification"],
)


@router.post("/")
@inject
async def notify(service: IncidentNotificationService = Depends(Provide[Container.incident_notification_service])):
    return service.notify()
