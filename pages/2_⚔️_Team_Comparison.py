import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_team_data

st.set_page_config(page_title="Team Comparison", page_icon="⚔️", layout="wide")

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #111827, #991b1b);
    padding: 34px;
    border-radius: 22px;
    margin-bottom: 28px;
}
.hero h1 {
    color: white;
    font-size: 2.7rem;
}
.hero p {
    color: #fee2e2;
}
.card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    margin-bottom: 18px;
}
.win {
    color: #16a34a;
    font-weight: 800;
}
.loss {
    color: #dc2626;
    font-weight: 800;
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
    <h1>⚔️ Team Comparison</h1>
    <p>Compare two NFL teams side by side using records, scoring, defense, and point differential.</p>
</div>
""", unsafe_allow_html=True)
team_options = df["Team"].tolist()

col1, col2 = st.columns(2)

with col1:
    team1_name = st.selectbox("Select Team 1", team_options, key="team1")

with col2:
    team2_name = st.selectbox("Select Team 2", team_options, index=1, key="team2")

team1 = df[df["Team"] == team1_name].iloc[0]
team2 = df[df["Team"] == team2_name].iloc[0]
team1_score = 0
team2_score = 0

higher_metrics = [
    "Wins",
    "Win Percentage",
    "Points Scored",
    "Point Differential"
]

lower_metrics = [
    "Points Allowed"
]

for metric in higher_metrics:
    if team1[metric] > team2[metric]:
        team1_score += 1
    elif team2[metric] > team1[metric]:
        team2_score += 1

for metric in lower_metrics:
    if team1[metric] < team2[metric]:
        team1_score += 1
    elif team2[metric] < team1[metric]:
        team2_score += 1

if team1_score > team2_score:
    st.success(
        f"🏆 {team1_name} leads this comparison, outperforming "
        f"{team2_name} in {team1_score} of 5 key metrics."
    )
elif team2_score > team1_score:
    st.success(
        f"🏆 {team2_name} leads this comparison, outperforming "
        f"{team1_name} in {team2_score} of 5 key metrics."
    )
else:
    st.info(
        f"🤝 {team1_name} and {team2_name} are tied across the selected metrics."
    )

def winner_class(value1, value2, lower_is_better=False):
    if value1 == value2:
        return "", ""
    if lower_is_better:
        return ("win", "loss") if value1 < value2 else ("loss", "win")
    return ("win", "loss") if value1 > value2 else ("loss", "win")

winpct_1, winpct_2 = winner_class(team1["Win Percentage"], team2["Win Percentage"])
diff_1, diff_2 = winner_class(team1["Point Differential"], team2["Point Differential"])

team1_color = team1["Primary Color"]
team2_color = team2["Primary Color"]

st.markdown('<div class="section-title">Team Profiles</div>', unsafe_allow_html=True)

profile1, profile2 = st.columns(2)

with profile1:
    st.markdown(
        f"""
        <div class="card" style="border-top: 8px solid {team1_color};">
            <h2>{team1["Team"]}</h2>
            <p><strong>Conference:</strong> {team1["Conference"]}</p>
            <p><strong>Division:</strong> {team1["Division"]}</p>
            <p><strong>Record:</strong> {int(team1["Wins"])}-{int(team1["Losses"])}</p>
            <p><strong>Win Percentage:</strong> <span class="{winpct_1}">{team1["Win Percentage"]}</span></p>
            <p><strong>Point Differential:</strong> <span class="{diff_1}">{int(team1["Point Differential"])}</span></p>
        </div>
        """,
        unsafe_allow_html=True
    )

with profile2:
    st.markdown(
        f"""
        <div class="card" style="border-top: 8px solid {team2_color};">
            <h2>{team2["Team"]}</h2>
            <p><strong>Conference:</strong> {team2["Conference"]}</p>
            <p><strong>Division:</strong> {team2["Division"]}</p>
            <p><strong>Record:</strong> {int(team2["Wins"])}-{int(team2["Losses"])}</p>
            <p><strong>Win Percentage:</strong> <span class="{winpct_2}">{team2["Win Percentage"]}</span></p>
            <p><strong>Point Differential:</strong> <span class="{diff_2}">{int(team2["Point Differential"])}</span></p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="section-title">Metric Breakdown</div>', unsafe_allow_html=True)

comparison = pd.DataFrame({
    "Metric": [
        "Wins",
        "Losses",
        "Win Percentage",
        "Points Scored",
        "Points Allowed",
        "Point Differential"
    ],
    team1_name: [
        int(team1["Wins"]),
        int(team1["Losses"]),
        team1["Win Percentage"],
        int(team1["Points Scored"]),
        int(team1["Points Allowed"]),
        int(team1["Point Differential"])
    ],
    team2_name: [
        int(team2["Wins"]),
        int(team2["Losses"]),
        team2["Win Percentage"],
        int(team2["Points Scored"]),
        int(team2["Points Allowed"]),
        int(team2["Point Differential"])
    ]
})

st.dataframe(comparison, use_container_width=True)

st.markdown('<div class="section-title">Visual Comparison</div>', unsafe_allow_html=True)

metrics = ["Wins", "Points Scored", "Points Allowed", "Point Differential"]

chart_data = pd.DataFrame({
    "Metric": metrics,
    team1_name: [team1[m] for m in metrics],
    team2_name: [team2[m] for m in metrics]
})

fig, ax = plt.subplots(figsize=(10, 5))
x = range(len(metrics))

ax.bar(
    [i - 0.2 for i in x],
    chart_data[team1_name],
    width=0.4,
    label=team1_name,
    color=team1_color
)

ax.bar(
    [i + 0.2 for i in x],
    chart_data[team2_name],
    width=0.4,
    label=team2_name,
    color=team2_color
)

ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.3)

ax.set_xticks(list(x))
ax.set_xticklabels(metrics, rotation=20)
ax.set_title(f"{team1_name} vs {team2_name}", fontsize=15, fontweight="bold")
ax.set_ylabel("Value")
ax.legend()

plt.tight_layout()
st.pyplot(fig)