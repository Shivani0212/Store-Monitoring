from pydantic import BaseModel
from datetime import datetime

class ReportResponse(BaseModel):
    report_id: str

class ReportStatus(BaseModel):
    status: str
    report_file: str | None = None
