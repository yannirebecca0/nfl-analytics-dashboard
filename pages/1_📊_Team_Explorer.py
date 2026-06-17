import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_team_data

st.set_page_config(page_title="Team Explorer", page_icon="📊", layout="wide")

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    padding: 34px;
    border-radius: 22px;
    margin-bottom: 28px;
}
.hero h1 {
    color: white;
    font-size: 2.7rem;
}
.hero p {
    color: #dbeafe;
}
.card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    margin-bottom: 18px;
}
.section-title {
    font-size: 1.45rem;
    font-weight: 800;
    margin-top: 28px;
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

df = load_team_data()

st.markdown("""
<div class="hero">
    <h1>📊 Team Explorer</h1>
    <p>Search, filter, and explore NFL teams by conference, division, record, scoring, and performance metrics.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Filters</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    search = st.text_input("Search team")

with col2:
    conference_filter = st.selectbox(
        "Conference",
        ["All"] + sorted(df["Conference"].unique().tolist())
    )

with col3:
    division_filter = st.selectbox(
        "Division",
        ["All"] + sorted(df["Division"].unique().tolist())
    )

filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["Team"].str.contains(search, case=False, na=False)
        | filtered_df["Abbreviation"].str.contains(search, case=False, na=False)
    ]

if conference_filter != "All":
    filtered_df = filtered_df[filtered_df["Conference"] == conference_filter]

if division_filter != "All":
    filtered_df = filtered_df[filtered_df["Division"] == division_filter]

st.markdown('<div class="section-title">Select a Team</div>', unsafe_allow_html=True)

selected_team = st.selectbox("Choose team", filtered_df["Team"])

team = df[df["Team"] == selected_team].iloc[0]
team_color = team["Primary Color"]

st.markdown(
    f"""
    <div class="card" style="border-top: 8px solid {team_color};">
        <h2>{team["Team"]}</h2>
        <p>
            <strong>Abbreviation:</strong> {team["Abbreviation"]}<br>
            <strong>Conference:</strong> {team["Conference"]}<br>
            <strong>Division:</strong> {team["Division"]}<br>
            <strong>Record:</strong> {int(team["Wins"])}-{int(team["Losses"])}<br>
            <strong>Win Percentage:</strong> {team["Win Percentage"]}<br>
            <strong>Point Differential:</strong> {int(team["Point Differential"])}
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-title">Team Metrics</div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

m1.metric("Wins", int(team["Wins"]))
m2.metric("Losses", int(team["Losses"]))
m3.metric("Points Scored", int(team["Points Scored"]))
m4.metric("Points Allowed", int(team["Points Allowed"]))

st.markdown('<div class="section-title">Performance Chart</div>', unsafe_allow_html=True)

metrics = ["Wins", "Losses", "Points Scored", "Points Allowed", "Point Differential"]
values = [team[m] for m in metrics]

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(metrics, values, color=team_color)

ax.set_title(f"{selected_team} Performance Overview", fontsize=15, fontweight="bold")
ax.set_ylabel("Value")
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.3)
plt.xticks(rotation=20)
plt.tight_layout()

st.pyplot(fig)

st.markdown('<div class="section-title">Filtered Team Table</div>', unsafe_allow_html=True)

st.dataframe(
    filtered_df[
        [
            "Abbreviation",
            "Team",
            "Conference",
            "Division",
            "Wins",
            "Losses",
            "Win Percentage",
            "Points Scored",
            "Points Allowed",
            "Point Differential"
        ]
    ],
    use_container_width=True
)