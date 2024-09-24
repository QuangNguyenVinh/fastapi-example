import os
from typing import List

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()

ENV: str = ""

class Configs(BaseSettings):
    # base
    ENV: str = os.getenv("ENV", "dev")
    PROJECT_NAME: str = "infra-worker"
    API: str = "/api"

    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    # auth
    JIRA_USERNAME: str = os.getenv("JIRA_USERNAME", "")
    JIRA_API_TOKEN: str = os.getenv("JIRA_API_TOKEN", "")
    JIRA_URI: str = os.getenv("JIRA_URI", "https://infra-worker.atlassian.net")
    JIRA_ISSUE_API: str = os.getenv("JIRA_ISSUE_API", "/rest/api/2/issue")

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    class Config:
        case_sensitive = True


class TestConfigs(Configs):
    ENV: str = "test"


configs = Configs()

if ENV == "prod":
    pass
elif ENV == "stage":
    pass
elif ENV == "test":
    setting = TestConfigs()