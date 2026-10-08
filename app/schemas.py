from pydantic import BaseModel, EmailStr
from typing import List


class Recipient(BaseModel):
    name: str
    email: EmailStr


class CertificateRequest(BaseModel):
    certificate_title: str
    organization: str
    event_date: str
    recipients: List[Recipient]