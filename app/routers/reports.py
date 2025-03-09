from fastapi import APIRouter, BackgroundTasks
from ..services import generate_report, get_report_status
from ..schemas import ReportResponse, ReportStatus

router = APIRouter()

@router.post("/trigger_report", response_model=ReportResponse)
async def trigger_report(background_tasks: BackgroundTasks):
    report_id = await generate_report()
    return {"report_id": report_id}

@router.get("/get_report", response_model=ReportStatus)
async def get_report(report_id: str):
    status = await get_report_status(report_id)
    if status == "Running":
        return {"status": "Running"}
    return {"status": "Complete", "report_file": status}
