import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_team_data

st.set_page_config(
    page_title="NFL Analytics Platform",
    page_icon="🏈",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f7fb;
        font-family: Arial, sans-serif;
    }

    .header-box, .team-card {
        background: white;
        padding: 28px;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
        margin-bottom: 25px;
    }

    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #111827;
    }

    .subtitle, .note {
        color: #4b5563;
    }

    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #111827;
        margin-top: 25px;
        margin-bottom: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

df = load_team_data()

st.markdown(
    """
    <div class="header-box">
        <div class="main-title">NFL Analytics Platform</div>
        <div class="subtitle">
            A sports analytics platform built with Python, Pandas, Streamlit, and NFL team data.
        </div>
        <div class="note">
            Data source: local NFL team dataset, prepared for future live data integration.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-title">League Overview</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.metric("Total Teams", len(df))
col2.metric("Conferences", df["Conference"].nunique())
col3.metric("Divisions", df["Division"].nunique())

st.markdown('<div class="section-title">Team Explorer</div>', unsafe_allow_html=True)

left, right = st.columns([1, 2])

with left:
    search = st.text_input("Search for a team")

    filtered_df = df.copy()

    if search:
        filtered_df = filtered_df[
            filtered_df["Team"].str.contains(search, case=False, na=False)
            | filtered_df["Abbreviation"].str.contains(search, case=False, na=False)
        ]

    selected_team = st.selectbox("Select Team", filtered_df["Team"])

with right:
    team = df[df["Team"] == selected_team].iloc[0]

    st.markdown(
        f"""
        <div class="team-card">
            <h3>{team["Team"]}</h3>
            <p>
                <strong>Abbreviation:</strong> {team["Abbreviation"]}<br>
                <strong>Conference:</strong> {team["Conference"]}<br>
                <strong>Division:</strong> {team["Division"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="section-title">NFL Teams Table</div>', unsafe_allow_html=True)

st.dataframe(
    df[["Abbreviation", "Team", "Conference", "Division"]],
    use_container_width=True
)

st.markdown('<div class="section-title">Teams by Conference</div>', unsafe_allow_html=True)

conference_counts = df["Conference"].value_counts()

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(conference_counts.index, conference_counts.values)
ax.set_title("NFL Teams by Conference")
ax.set_xlabel("Conference")
ax.set_ylabel("Number of Teams")

st.pyplot(fig)

st.markdown('<div class="section-title">Teams by Division</div>', unsafe_allow_html=True)

division_counts = df["Division"].value_counts().sort_index()

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(division_counts.index, division_counts.values)
ax2.set_title("NFL Teams by Division")
ax2.set_xlabel("Division")
ax2.set_ylabel("Number of Teams")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig2)