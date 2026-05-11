from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session 
from database_models import DBWorkItem
from database import redis_client, mongo_db, get_db
from models import Signal
import datetime
import uuid 
app = FastAPI()

@app.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "timestamp": datetime.datetime.utcnow()
    }

@app.post("/ingest")
async def ingest_signal(signal: Signal, db: Session = Depends(get_db)):
    
    await mongo_db.signals.insert_one(signal.dict())
    
    
    redis_key = f"debounce:{signal.component_id}:{signal.signal_type}"
    if redis_client.exists(redis_key):
        return {"status": "debounced"}
    
    redis_client.setex(redis_key, 10, "active")
    
    
    try:
        new_work_item = DBWorkItem(
            id=str(uuid.uuid4())[:8],
            component_id=signal.component_id,
            severity=signal.severity,
            status="OPEN"
        )
        
        db.add(new_work_item)
        db.commit() 
        db.refresh(new_work_item)
        
        print(f"[{datetime.datetime.now()}] ✅ DB SUCCESS: Saved {new_work_item.id}")
        
        return {
            "status": "created", 
            "incident_id": new_work_item.id,
            "component": signal.component_id
        }
    except Exception as e:
        db.rollback() 
        print(f"❌ DB ERROR: {e}")
        return {"status": "error", "message": str(e)}