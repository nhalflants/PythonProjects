import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")
indicators = [col.replace("_", " ").capitalize() for col in list(df.columns)][1:]
x_label = st.selectbox("Select the data for the X-axis", indicators)
y_label = st.selectbox("Select the data for the Y-axis", indicators)
st.subheader(f"{x_label} and {y_label}")

x_col = x_label.replace(" ", "_").lower()
y_col = y_label.replace(" ", "_").lower()
figure = px.scatter(df, x=x_col, y=y_col, labels={"x": x_label, "y": y_label})
st.plotly_chart(figure)
