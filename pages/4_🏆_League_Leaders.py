import streamlit as st
import matplotlib.pyplot as plt
from data_loader import load_team_data

st.set_page_config(page_title="League Leaders", page_icon="🏆", layout="wide")

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #111827, #1f2937);
    padding: 32px;
    border-radius: 22px;
    margin-bottom: 28px;
}
.hero h1 {
    color: white;
    font-size: 2.6rem;
    margin-bottom: 8px;
}
.hero p {
    color: #d1d5db;
    font-size: 1rem;
}
.section-title {
    font-size: 1.45rem;
    font-weight: 800;
    margin-top: 28px;
    margin-bottom: 14px;
}
.insight-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    margin-top: 18px;
}
</style>
""", unsafe_allow_html=True)

df = load_team_data()

st.markdown("""
<div class="hero">
    <h1>🏆 League Leaders</h1>
    <p>Explore the NFL’s top teams by wins, offense, defense, and point differential.</p>
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

st.markdown('<div class="section-title">Ranking Explorer</div>', unsafe_allow_html=True)

left, right = st.columns([1, 2])

with left:
    ranking_metric = st.selectbox(
        "Choose ranking metric",
        ["Wins", "Win Percentage", "Points Scored", "Points Allowed", "Point Differential"]
    )

    top_n = st.slider("Number of teams to show", 5, 15, 10)

ascending = ranking_metric == "Points Allowed"
ranked_df = df.sort_values(by=ranking_metric, ascending=ascending)
top_df = ranked_df.head(top_n)

with right:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(top_df["Team"], top_df[ranking_metric])
    ax.set_title(f"Top {top_n} Teams by {ranking_metric}", fontsize=15, fontweight="bold")
    ax.set_xlabel(ranking_metric)
    ax.invert_yaxis()
    plt.tight_layout()
    st.pyplot(fig)

st.markdown('<div class="section-title">Ranked Team Table</div>', unsafe_allow_html=True)

st.dataframe(
    ranked_df[
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

best_team = ranked_df.iloc[0]

st.markdown(
    f"""
    <div class="insight-card">
        <h3>Quick Insight</h3>
        <p>
            Based on <strong>{ranking_metric}</strong>, the top-ranked team is 
            <strong>{best_team["Team"]}</strong> with a value of 
            <strong>{best_team[ranking_metric]}</strong>.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)