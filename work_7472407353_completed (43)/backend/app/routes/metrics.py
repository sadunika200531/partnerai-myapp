from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Metric
from ..schemas import MetricData

router = APIRouter()

@router.post("/report")
def report_metrics(data: MetricData, db: Session = Depends(get_db)):
    metric = Metric(cpu_usage=data.cpu_usage, ram_usage=data.ram_usage)
    db.add(metric)
    db.commit()
    return {"status": "success"}