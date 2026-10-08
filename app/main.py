from fastapi import FastAPI

from app.routes.certificates import router as certificate_router

app = FastAPI(title="Bulk Certificate Generator")


@app.get("/")
def home():
    return {
        "message": "Bulk Certificate Generator API is running"
    }


app.include_router(
    certificate_router,
    prefix="/certificates",
    tags=["Certificates"]
)