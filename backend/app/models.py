from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    note = Column(String, nullable=True)
