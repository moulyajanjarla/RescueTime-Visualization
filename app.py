import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("activitywatch_data.csv")

st.title("ActivityWatch Data Dashboard")
fig = px.bar(df, x="app", y="timestamp", title="Time Spent on Applications")
st.plotly_chart(fig)
