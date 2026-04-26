from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class MetricData(BaseModel):
    cpu_usage: float
    ram_usage: float

class AIRequest(BaseModel):
    prompt: str
    api_key: str