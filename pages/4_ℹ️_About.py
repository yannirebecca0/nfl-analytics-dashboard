import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #111827, #2563eb);
    padding: 36px;
    border-radius: 20px;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 2.8rem;
    margin-bottom: 8px;
}

.hero p {
    color: #dbeafe;
    font-size: 1.1rem;
}

.card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>ℹ️ About the NFL Analytics Platform</h1>
    <p>
        An interactive analytics platform for exploring NFL teams, comparing performance,
        visualizing statistics, and demonstrating modern Python data engineering concepts.
    </p>
</div>
""", unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    st.markdown("""
    <div class="card">
        <h3>🏈 Features</h3>
        <ul>
            <li>Interactive Team Explorer</li>
            <li>Head-to-head Team Comparison</li>
            <li>League Leaders dashboard</li>
            <li>Search and filtering tools</li>
            <li>Dynamic team colors and visualizations</li>
            <li>Performance metrics and rankings</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="card">
        <h3>💻 Technologies</h3>
        <ul>
            <li>Python</li>
            <li>Streamlit</li>
            <li>Pandas</li>
            <li>Matplotlib</li>
            <li>CSV-based data processing</li>
            <li>Modular project architecture</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>🎯 Project Goal</h3>
    <p>
        This platform was designed to provide an intuitive way to explore NFL data while
        demonstrating software engineering, data analysis, and interactive visualization
        skills. The project emphasizes clean code organization, user-friendly design, and
        scalable architecture suitable for future enhancements.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>🚀 Future Enhancements</h3>
    <ul>
        <li>Live NFL data integration</li>
        <li>Additional advanced analytics</li>
        <li>Historical trend visualizations</li>
        <li>Expanded comparison metrics</li>
        <li>Enhanced interactive dashboards</li>
    </ul>
</div>
""", unsafe_allow_html=True)