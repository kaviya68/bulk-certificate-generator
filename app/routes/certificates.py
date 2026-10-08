from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.certificate import GenerationJob, Certificate
from app.schemas import CertificateRequest

router = APIRouter()


@router.post("/generate")
def generate_certificates(
    request: CertificateRequest,
    db: Session = Depends(get_db)
):
    # Create a new generation job
    job = GenerationJob(
        certificate_title=request.certificate_title,
        organization=request.organization,
        event_date=request.event_date,
        total=len(request.recipients),
        status="processing"
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return {
        "job_id": job.id,
        "status": job.status,
        "total": job.total
    }