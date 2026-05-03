# streamlit_app.py

import streamlit as st
import time
import pandas as pd
from src.shared_data import shared_data

st.set_page_config(page_title="Drowsiness Dashboard", layout="wide")

st.title("🚗 Driver Drowsiness Dashboard")

# Layout
col1, col2 = st.columns(2)

fatigue_chart = col1.line_chart()
ear_chart = col2.line_chart()

mar_chart = col1.line_chart()
blink_chart = col2.line_chart()

yawn_chart = st.line_chart()

status_box = st.empty()

while True:
    if len(shared_data.fatigue) > 0:
        df = pd.DataFrame({
            "Fatigue": list(shared_data.fatigue),
            "EAR": list(shared_data.ear),
            "MAR": list(shared_data.mar),
            "Blink Rate": list(shared_data.blink_rate),
            "Yawns": list(shared_data.yawns)
        })

        fatigue_chart.line_chart(df["Fatigue"])
        ear_chart.line_chart(df["EAR"])
        mar_chart.line_chart(df["MAR"])
        blink_chart.line_chart(df["Blink Rate"])
        yawn_chart.line_chart(df["Yawns"])

        latest = df.iloc[-1]

        # Status logic
        if latest["Fatigue"] > 80:
            status = "🔴 CRITICAL"
        elif latest["Fatigue"] > 50:
            status = "🟠 WARNING"
        elif latest["Fatigue"] > 25:
            status = "🟡 TIRED"
        else:
            status = "🟢 ALERT"

        status_box.metric("Current Status", status, f"{int(latest['Fatigue'])}%")

    time.sleep(1)