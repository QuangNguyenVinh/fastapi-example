import logging
from app.core.config import configs

logger = logging.getLogger('uvicorn.error')


class IncidentNotificationService:

    def __init__(self):
        pass

    def notify(self):
        logger.info('Notify Incident to JIRA {}'.format(configs.JIRA_URI))
