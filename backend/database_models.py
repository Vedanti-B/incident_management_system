from sqlalchemy import Column, String, Integer, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from database import engine
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class DBWorkItem(Base):
    __tablename__ = "work_items"

    id = Column(String, primary_key=True, index=True)
    component_id = Column(String, index=True)
    status = Column(String, default="OPEN") # Requirement: State Management
    severity = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    # Requirement: RCA must be linked to the incident
    rca_data = relationship("DBRCA", back_populates="work_item", uselist=False)

class DBRCA(Base):
    __tablename__ = "root_cause_analysis"

    id = Column(Integer, primary_key=True, index=True)
    work_item_id = Column(String, ForeignKey("work_items.id"))
    category = Column(String) # e.g., Network, Hardware, Software
    fix_applied = Column(String)
    prevention_steps = Column(String)
    
    work_item = relationship("DBWorkItem", back_populates="rca_data")

# Create the tables in Docker Postgres
Base.metadata.create_all(bind=engine)