import streamlit as st

st.set_page_config(
    page_title="NFL Analytics Platform",
    page_icon="🏈",
    layout="wide"
)

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    padding: 40px;
    border-radius: 20px;
    margin-bottom: 30px;
}

.hero h1 {
    color: white;
    font-size: 3rem;
    margin-bottom: 8px;
}

.hero p {
    color: #dbeafe;
    font-size: 1.1rem;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,.05);
}

.section {
    margin-top: 30px;
    margin-bottom: 10px;
    font-size: 1.6rem;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🏈 NFL Analytics Platform</h1>
    <p>
        Explore NFL teams, compare franchises, analyze league leaders,
        and visualize football data through an interactive analytics platform
        built with Python, Pandas, and Streamlit.
    </p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        "<div class='card'><h2>32</h2><p>NFL Teams</p></div>",
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        "<div class='card'><h2>2</h2><p>Conferences</p></div>",
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        "<div class='card'><h2>8</h2><p>Divisions</p></div>",
        unsafe_allow_html=True,
    )

with c4:
    st.markdown(
        "<div class='card'><h2>Python</h2><p>Pandas + Streamlit</p></div>",
        unsafe_allow_html=True,
    )

st.markdown("<div class='section'>🚀 Platform Features</div>", unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    st.success("🔍 Team Explorer")
    st.success("⚔️ Team Comparison")
    st.success("🏆 League Leaders")

with right:
    st.success("📊 Interactive Charts")
    st.success("🐼 Pandas Data Processing")
    st.success("💻 Multi-Page Analytics App")

st.markdown("<div class='section'>⭐ About</div>", unsafe_allow_html=True)

st.info("""
My name is Rebecca and this project demonstrates software engineering, data analysis,
interactive visualization, and UI development skills using Python.
It is designed as a portfolio project showcasing modern analytics
concepts and scalable application structure.
""")