from pydantic import BaseModel
import datetime


class Defection(BaseModel):
    defection_time: datetime.timedelta
    id: int
    reason: str
    defection_type_id: int
    student_id: int

    class Config:
        orm_mode = True