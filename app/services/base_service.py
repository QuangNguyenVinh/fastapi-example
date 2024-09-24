from typing import Any, Protocol


class BaseService:
    def __init__(self) -> None:
        pass

    def close_session(self) -> None:
        pass
