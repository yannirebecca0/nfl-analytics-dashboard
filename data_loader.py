import pandas as pd
import streamlit as st


@st.cache_data
def load_team_data():
    teams = pd.read_csv("data/teams.csv")
    return teams