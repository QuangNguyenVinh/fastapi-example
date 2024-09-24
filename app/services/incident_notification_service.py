import logging
from app.core.config import configs
from app.services.base_service import BaseService

logger = logging.getLogger('uvicorn.error')


class IncidentNotificationService(BaseService):

    def __init__(self):
        super().__init__()
        pass

    def notify(self):
        logger.info('Notify Incident to JIRA {}'.format(configs.JIRA_URI))
