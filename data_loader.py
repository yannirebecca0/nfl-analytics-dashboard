import pandas as pd
import streamlit as st


@st.cache_data
def load_team_data():
    teams = pd.read_csv("data/teams.csv")

    teams["Point Differential"] = teams["Points Scored"] - teams["Points Allowed"]
    teams["Win Percentage"] = (teams["Wins"] / (teams["Wins"] + teams["Losses"])).round(3)

    return teams