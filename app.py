"""AI Readiness Scan - Streamlit app.

Run locally:  streamlit run app.py
"""

import plotly.graph_objects as go
import streamlit as st

from scan.questions import DIMENSIONS, QUESTIONS, SCALE, SECTORS
from scan.report import ai_summary, build_report
from scan.scoring import score

st.set_page_config(page_title="AI Readiness Scan", page_icon="🤖", layout="centered")

st.title("AI Readiness Scan")
st.write(
    "A 5-minute check of how ready a small business is to use AI, "
    "with a score across six dimensions and a practical 30-day plan."
)

with st.form("scan"):
    business = st.text_input("Business name (optional)")
    sector = st.selectbox("Sector", list(SECTORS))
    st.caption("Rate each statement from 1 (not at all) to 5 (fully).")

    answers = {}
    for key, label in DIMENSIONS.items():
        st.subheader(label)
        for q in (q for q in QUESTIONS if q["dimension"] == key):
            answers[q["id"]] = st.select_slider(
                q["text"], options=list(SCALE), value=3,
                format_func=lambda v: f"{v} - {SCALE[v]}", key=q["id"],
            )
    submitted = st.form_submit_button("Get my readiness report")

if submitted:
    result = score(answers)

    st.header(f"Overall: {result.overall:.1f} / 5 ({result.level})")
    st.write(result.level_description)

    labels = [DIMENSIONS[k] for k in DIMENSIONS]
    values = [result.dimension_scores[k] for k in DIMENSIONS]
    fig = go.Figure(go.Scatterpolar(r=values + values[:1], theta=labels + labels[:1], fill="toself"))
    fig.update_layout(polar=dict(radialaxis=dict(range=[0, 5])), showlegend=False, height=420)
    st.plotly_chart(fig, use_container_width=True)

    try:
        api_key = st.secrets.get("ANTHROPIC_API_KEY")
    except Exception:  # no secrets file configured
        api_key = None
    summary = ai_summary(business, sector, result, api_key)
    if summary:
        st.subheader("Executive summary (AI-generated)")
        st.write(summary)

    report = build_report(business, sector, result)
    if summary:
        report = report.replace("## Overall readiness", f"## Executive summary\n{summary}\n\n## Overall readiness", 1)
    st.markdown(report)
    st.download_button("Download report (Markdown)", report, file_name="ai_readiness_report.md")
