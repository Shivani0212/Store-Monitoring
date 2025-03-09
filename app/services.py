import uuid
from .utils import calculate_uptime_downtime

report_status = {}

async def generate_report():
    report_id = str(uuid.uuid4())
    report_status[report_id] = "Running"
    
    # Simulate processing
    report_data = calculate_uptime_downtime([])
    
    # Save report as CSV
    report_file = f"data/report_{report_id}.csv"
    df = pd.DataFrame([report_data])
    df.to_csv(report_file, index=False)
    
    report_status[report_id] = report_file
    return report_id

async def get_report_status(report_id: str):
    return report_status.get(report_id, "Invalid report ID")
