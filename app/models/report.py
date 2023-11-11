from pydantic import BaseModel
from datetime import datetime, date


class Report(BaseModel):
    user: int
    body: str
    date: date
    state: str


