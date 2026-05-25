from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware   # ← Added this
from sqlalchemy.orm import Session
from datetime import date

from .database import SessionLocal, Base, engine
from .models import Patient

app = FastAPI(title="Patient Portal Backend - Week 2")

# === CORS Middleware (Important for frontend to talk to backend) ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # Allows your phone and local frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables on startup if needed
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
            "dob": p.dob.isoformat(),
            "note": p.note,
        }
        for p in patients
    ]


@app.get("/patients/{patient_id}")
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {
        "id": patient.id,
        "first_name": patient.first_name,
        "last_name": patient.last_name,
        "dob": patient.dob.isoformat(),
        "note": patient.note,
    }
