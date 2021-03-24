import uuid
from datetime import date, datetime

from pydantic.types import UUID4


class Category:
    id: UUID4
    name: str
    description: str
    created_at: datetime

    def __init__(self, name: str, description: str) -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.created_at = datetime.today()
