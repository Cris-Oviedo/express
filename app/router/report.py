from fastapi import APIRouter
from models.report import Report


rt_report = APIRouter()

@rt_report.post('/send-report')
async def set_report_by_user(report: Report):
    return {'Se cargaron correctamente los datos':report}