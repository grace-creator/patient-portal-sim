from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import SessionLocal, Base, engine
from .models import Patient

app = FastAPI(title="Patient Portal Backend")

# CORS - Must be the FIRST middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/patients")
def list_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return [
        {
            "id": p.id,
            "first_name": p.first_name,
            "last_name": p.last_name,
            "dob": p.dob.isoformat() if p.dob else None,
            "note": p.note,
        }
        for p in patients
    ]
