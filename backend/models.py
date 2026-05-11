from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from datetime import datetime

class Signal(BaseModel):
    component_id: str
    signal_type: str
    severity: int = Field(ge=1, le=5) # Allows severity 1 to 5
    timestamp: str
    
class RootCauseAnalysis(BaseModel):
    category: str  # Dropdown: Hardware, Software, Network, etc.
    fix_applied: str
    prevention_steps: str
    start_time: datetime
    end_time: datetime

class WorkItem(BaseModel):
    id: str
    component_id: str
    status: str = "OPEN"  # OPEN, INVESTIGATING, RESOLVED, CLOSED
    severity: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    rca: Optional[RootCauseAnalysis] = None # Mandatory before closing