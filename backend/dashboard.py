import streamlit as st
import pandas as pd
from sqlalchemy import create_engine


SQL_URL = "postgresql://admin:password123@localhost:5432/ims_db"
engine = create_engine(SQL_URL)

st.set_page_config(page_title="SRE Incident Dashboard", layout="wide")
st.title("🛡️ Incident Management System")


if st.button('Refresh Data'):
    st.rerun()


df = pd.read_sql("SELECT * FROM work_items ORDER BY created_at DESC", engine)


col1, col2 = st.columns(2)
col1.metric("Total Incidents", len(df))
col2.metric("Open Tickets", len(df[df['status'] == 'OPEN']))


st.subheader("Recent Incidents")
st.dataframe(df, width='stretch')