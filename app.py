import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="NFL Analytics Dashboard",
    page_icon="🏈",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f7fb;
        font-family: 'Inter', 'Arial', sans-serif;
    }

    .header-box {
        background: white;
        padding: 32px;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
        margin-bottom: 25px;
    }

    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #111827;
        margin-bottom: 6px;
    }

    .subtitle {
        font-size: 1rem;
        color: #4b5563;
        margin-bottom: 8px;
    }

    .note {
        font-size: 0.85rem;
        color: #6b7280;
    }

    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #111827;
        margin-top: 25px;
        margin-bottom: 12px;
    }

    .team-card {
        background: white;
        padding: 24px;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }

    .team-card h3 {
        color: #111827;
        margin-bottom: 10px;
    }

    .team-card p {
        color: #374151;
        font-size: 1rem;
        line-height: 1.6;
    }

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #e5e7eb;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.05);
    }

    div[data-testid="stMetricValue"] {
        color: #111827;
        font-size: 1.4rem;
    }

    div[data-testid="stMetricLabel"] {
        color: #6b7280;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="header-box">
        <div class="main-title">NFL Analytics Dashboard</div>
        <div class="subtitle">
            A clean football analytics dashboard for exploring team performance, scoring trends, and win metrics.
        </div>
        <div class="note">
            Note: This version uses sample team data while the real NFL data source is being integrated.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

@st.cache_data
def load_team_data():
    url = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/team_desc.csv"
    teams = pd.read_csv(url)

    teams = teams[
        [
            "team_abbr",
            "team_name",
            "team_id",
            "team_conf",
            "team_division",
            "team_color",
            "team_logo_espn"
        ]
    ]

    teams = teams.rename(
        columns={
            "team_abbr": "Abbreviation",
            "team_name": "Team",
            "team_id": "Team ID",
            "team_conf": "Conference",
            "team_division": "Division",
            "team_color": "Primary Color",
            "team_logo_espn": "Logo"
        }
    )

    return teams

df = load_team_data()
df = pd.DataFrame(data)
df["Point Differential"] = df["Points Scored"] - df["Points Allowed"]
df["Win Percentage"] = (df["Wins"] / (df["Wins"] + df["Losses"])).round(3)

st.markdown('<div class="section-title">League Snapshot</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

# col1.metric("Most Wins", df.loc[df["Wins"].idxmax(), "Team"], int(df["Wins"].max()))
# col2.metric("Highest Scoring", df.loc[df["Points Scored"].idxmax(), "Team"], int(df["Points Scored"].max()))
# col3.metric("Best Defense", df.loc[df["Points Allowed"].idxmin(), "Team"], int(df["Points Allowed"].min()))
# col4.metric("Best Point Differential", df.loc[df["Point Differential"].idxmax(), "Team"], int(df["Point Differential"].max()))

st.markdown('<div class="section-title">Explore a Team</div>', unsafe_allow_html=True)

left, right = st.columns([1, 2])

with left:
    selected_team = st.selectbox("Select Team", df["Team"])
    selected_stat = st.selectbox(
        "Select Statistic",
        ["Wins", "Losses", "Points Scored", "Points Allowed", "Point Differential", "Win Percentage"]
    )

with right:
    team = df[df["Team"] == selected_team].iloc[0]

    st.markdown(
        f"""
        <div class="team-card">
            <h3>{selected_team}</h3>
            <p>
                <strong>Record:</strong> {int(team["Wins"])}-{int(team["Losses"])}<br>
                <strong>Points Scored:</strong> {int(team["Points Scored"])}<br>
                <strong>Points Allowed:</strong> {int(team["Points Allowed"])}<br>
                <strong>Point Differential:</strong> {int(team["Point Differential"])}<br>
                <strong>Win Percentage:</strong> {team["Win Percentage"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="section-title">Team Statistics Table</div>', unsafe_allow_html=True)
st.dataframe(df, use_container_width=True)

st.markdown('<div class="section-title">Performance Comparison</div>', unsafe_allow_html=True)

sorted_df = df.sort_values(by=selected_stat, ascending=False)

fig, ax = plt.subplots(figsize=(14, 6))
ax.bar(sorted_df["Team"], sorted_df[selected_stat])

ax.set_title(f"NFL Teams by {selected_stat}", fontsize=16, fontweight="bold")
ax.set_xlabel("Team")
ax.set_ylabel(selected_stat)
plt.xticks(rotation=90)
plt.tight_layout()

st.pyplot(fig)