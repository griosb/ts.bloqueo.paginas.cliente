from pydantic import BaseModel
from typing import Optional


class HostTemplate(BaseModel):
    id:Optional[int] = None
    name: str
    ip:str
    