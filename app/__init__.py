from fastapi import FastAPI
from router import report

from database.postgres import connect_to_db

app = FastAPI()
db = connect_to_db()
app.include_router(report.rt_report)

@app.get('/')
async def root():
    return {'API': 'Enable Ok'}

