import streamlit as st
from data_loader import load_team_data

st.set_page_config(
    page_title="NFL Analytics Platform",
    page_icon="🏈",
    layout="wide"
)

df = load_team_data()

best_record = df.loc[df["Wins"].idxmax()]
top_offense = df.loc[df["Points Scored"].idxmax()]
best_defense = df.loc[df["Points Allowed"].idxmin()]
best_diff = df.loc[df["Point Differential"].idxmax()]

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    padding: 42px;
    border-radius: 24px;
    margin-bottom: 30px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.12);
}
.hero h1 {
    color: white;
    font-size: 3.1rem;
    margin-bottom: 10px;
}
.hero p {
    color: #dbeafe;
    font-size: 1.12rem;
    max-width: 900px;
}
.card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    margin-bottom: 18px;
}
.card h3 {
    margin-bottom: 8px;
}
.section-title {
    font-size: 1.5rem;
    font-weight: 800;
    margin-top: 32px;
    margin-bottom: 16px;
}
.small-text {
    color: #4b5563;
    font-size: 0.95rem;
}
.footer {
    margin-top: 35px;
    color: #6b7280;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🏈 NFL Analytics Platform</h1>
    <p>
        A modern sports analytics platform for exploring NFL teams, comparing performance,
        ranking league leaders, and visualizing football insights with Python, Pandas, Streamlit, and Matplotlib.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Platform Snapshot</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("<div class='card'><h3>🏈 32</h3><p class='small-text'>NFL Teams</p></div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='card'><h3>🏆 2</h3><p class='small-text'>Conferences</p></div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='card'><h3>📍 8</h3><p class='small-text'>Divisions</p></div>", unsafe_allow_html=True)

with c4:
    st.markdown("<div class='card'><h3>📊 CSV + Pandas</h3><p class='small-text'>Data Processing</p></div>", unsafe_allow_html=True)

st.markdown('<div class="section-title">Featured Insights</div>', unsafe_allow_html=True)

i1, i2, i3, i4 = st.columns(4)

with i1:
    st.markdown(
        f"<div class='card'><h3>🏆 Best Record</h3><p><strong>{best_record['Team']}</strong></p><p class='small-text'>{int(best_record['Wins'])}-{int(best_record['Losses'])}</p></div>",
        unsafe_allow_html=True
    )

with i2:
    st.markdown(
        f"<div class='card'><h3>🔥 Top Offense</h3><p><strong>{top_offense['Team']}</strong></p><p class='small-text'>{int(top_offense['Points Scored'])} points</p></div>",
        unsafe_allow_html=True
    )

with i3:
    st.markdown(
        f"<div class='card'><h3>🛡️ Best Defense</h3><p><strong>{best_defense['Team']}</strong></p><p class='small-text'>{int(best_defense['Points Allowed'])} points allowed</p></div>",
        unsafe_allow_html=True
    )

with i4:
    st.markdown(
        f"<div class='card'><h3>📈 Best Differential</h3><p><strong>{best_diff['Team']}</strong></p><p class='small-text'>+{int(best_diff['Point Differential'])}</p></div>",
        unsafe_allow_html=True
    )

st.markdown('<div class="section-title">Explore the Platform</div>', unsafe_allow_html=True)

n1, n2 = st.columns(2)

with n1:
    st.markdown("""
    <div class="card">
        <h3>🔍 Team Explorer</h3>
        <p class="small-text">Search, filter, and explore NFL teams by conference, division, record, and scoring metrics.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>⚔️ Team Comparison</h3>
        <p class="small-text">Compare any two teams side by side with team-colored charts and winner insights.</p>
    </div>
    """, unsafe_allow_html=True)

with n2:
    st.markdown("""
    <div class="card">
        <h3>🏆 League Leaders</h3>
        <p class="small-text">Rank teams by wins, win percentage, point differential, scoring, and defensive performance.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>ℹ️ About</h3>
        <p class="small-text">Learn about the project goals, technologies, and future enhancements.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">Built With</div>', unsafe_allow_html=True)

b1, b2, b3, b4 = st.columns(4)

with b1:
    st.markdown("<div class='card'><h3>🐍 Python</h3><p class='small-text'>Core programming language</p></div>", unsafe_allow_html=True)

with b2:
    st.markdown("<div class='card'><h3>🐼 Pandas</h3><p class='small-text'>Data loading and analysis</p></div>", unsafe_allow_html=True)

with b3:
    st.markdown("<div class='card'><h3>📊 Streamlit</h3><p class='small-text'>Interactive web application</p></div>", unsafe_allow_html=True)

with b4:
    st.markdown("<div class='card'><h3>📈 Matplotlib</h3><p class='small-text'>Data visualizations</p></div>", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    Designed to demonstrate interactive data analysis, visualization, and software engineering concepts through NFL statistics.
</div>
""", unsafe_allow_html=True)