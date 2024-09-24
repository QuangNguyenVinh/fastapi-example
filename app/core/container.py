from dependency_injector import containers, providers
from app.services import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.routers.incident_notification"
        ]
    )

    incident_notification_service = providers.Factory(IncidentNotificationService)
