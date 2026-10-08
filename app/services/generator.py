from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os


def generate_certificate(
    name,
    certificate_title,
    organization,
    event_date,
    certificate_id
):
    os.makedirs("certificates", exist_ok=True)

    file_path = f"certificates/certificate_{certificate_id}.pdf"

    pdf = canvas.Canvas(file_path, pagesize=A4)

    width, height = A4

    # Title
    pdf.setFont("Helvetica-Bold", 28)
    pdf.drawCentredString(
        width / 2,
        height - 150,
        "CERTIFICATE"
    )

    # Certificate title
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(
        width / 2,
        height - 210,
        certificate_title
    )

    # Recipient
    pdf.setFont("Helvetica", 16)
    pdf.drawCentredString(
        width / 2,
        height - 280,
        "This certificate is proudly presented to"
    )

    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(
        width / 2,
        height - 330,
        name
    )

    # Organization
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(
        width / 2,
        height - 390,
        f"Organized by {organization}"
    )

    # Date
    pdf.drawCentredString(
        width / 2,
        height - 430,
        f"Date: {event_date}"
    )

    pdf.save()

    return file_path