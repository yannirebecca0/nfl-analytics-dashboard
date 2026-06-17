import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_team_data

st.set_page_config(page_title="League Leaders", page_icon="🏆", layout="wide")

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #111827, #ca8a04);
    padding: 34px;
    border-radius: 22px;
    margin-bottom: 28px;
}
.hero h1 {
    color: white;
    font-size: 2.7rem;
}
.hero p {
    color: #fef3c7;
}
.section-title {
    font-size: 1.45rem;
    font-weight: 800;
    margin-top: 28px;
    margin-bottom: 14px;
}
.rank-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    margin-bottom: 18px;
}
</style>
""", unsafe_allow_html=True)

df = load_team_data()

st.markdown("""
<div class="hero">
    <h1>🏆 League Leaders</h1>
    <p>Explore the NFL’s top teams by wins, win percentage, scoring, defense, and point differential.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

most_wins = df.loc[df["Wins"].idxmax()]
best_offense = df.loc[df["Points Scored"].idxmax()]
best_defense = df.loc[df["Points Allowed"].idxmin()]
best_diff = df.loc[df["Point Differential"].idxmax()]

col1.metric("Most Wins", most_wins["Team"], int(most_wins["Wins"]))
col2.metric("Top Offense", best_offense["Team"], int(best_offense["Points Scored"]))
col3.metric("Best Defense", best_defense["Team"], int(best_defense["Points Allowed"]))
col4.metric("Best Point Differential", best_diff["Team"], int(best_diff["Point Differential"]))

st.markdown('<div class="section-title">Ranking Controls</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    ranking_metric = st.selectbox(
        "Rank teams by",
        ["Wins", "Win Percentage", "Points Scored", "Points Allowed", "Point Differential"]
    )

with c2:
    top_n = st.slider("Teams to display", 5, 32, 10)

with c3:
    view_type = st.selectbox("View", ["Top Teams", "Bottom Teams"])

ascending = ranking_metric == "Points Allowed"

if view_type == "Bottom Teams":
    ascending = not ascending

ranked_df = df.sort_values(by=ranking_metric, ascending=ascending).reset_index(drop=True)
top_df = ranked_df.head(top_n).copy()

top_df.insert(0, "Rank", range(1, len(top_df) + 1))

medals = {
    1: "🥇",
    2: "🥈",
    3: "🥉"
}

top_df["Rank"] = top_df["Rank"].apply(lambda x: f"{medals.get(x, '')} {x}")

st.markdown('<div class="section-title">Ranked Teams</div>', unsafe_allow_html=True)

st.dataframe(
    top_df[
        [
            "Rank",
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

st.markdown(f'<div class="section-title">{view_type} by {ranking_metric}</div>', unsafe_allow_html=True)

chart_df = ranked_df.head(top_n)

fig, ax = plt.subplots(figsize=(11, 6))

colors = chart_df["Primary Color"].tolist()

ax.barh(chart_df["Team"], chart_df[ranking_metric], color=colors)
ax.set_title(f"{view_type} by {ranking_metric}", fontsize=16, fontweight="bold")
ax.set_xlabel(ranking_metric)
ax.invert_yaxis()
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="x", linestyle="--", alpha=0.3)

plt.tight_layout()
st.pyplot(fig)

leader = ranked_df.iloc[0]

st.markdown(
    f"""
    <div class="rank-card" style="border-left: 8px solid {leader["Primary Color"]};">
        <h3>Quick Insight</h3>
        <p>
            Based on <strong>{ranking_metric}</strong>, the leading team in this view is 
            <strong>{leader["Team"]}</strong> with a value of 
            <strong>{leader[ranking_metric]}</strong>.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)