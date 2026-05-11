# Mission Critical Incident Management System (SRE Assignment)

## 🚀 Overview
A resilient, production-ready incident ingestion pipeline built with **FastAPI**, **Redis**, **PostgreSQL**, and **MongoDB**. The system is designed to handle high-frequency signals while maintaining data integrity and observability.

## 🏗️ Architecture
- **API Layer:** FastAPI (Asynchronous request handling)
- **Caching & Debouncing:** Redis (Performance layer to prevent alert fatigue)
- **Audit Log:** MongoDB (Data lake for raw signal persistence)
- **Source of Truth:** PostgreSQL (Structured incident state management)
- **Dashboard:** Streamlit (Real-time observability)
- **Containerization:** Docker Compose

## 🛠️ Non-Functional Highlights (Bonus Points)
- **Performance:** Implemented **Redis Debouncing** to reduce database write-load by $O(1)$ lookups. It prevents duplicate incident creation within a 10-second window.
- **Polyglot Persistence:** Used MongoDB for high-volume logs and PostgreSQL for ACID-compliant work items.
- **Observability:** Includes a `/health` endpoint and a live Streamlit dashboard.

## 🚦 How to Run
1. **Start Infrastructure:** `docker-compose up -d`
2. **Start Backend:** `cd backend && python -m uvicorn main:app --reload`
3. **Run Simulator:** `python simulate_signals.py`
4. **View Dashboard:** `python -m streamlit run dashboard.py`
