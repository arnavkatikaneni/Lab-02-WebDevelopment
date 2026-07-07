# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on TV watching habits.")

# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.
if os.path.exists("data.csv"):
    csvData = pd.read_csv("data.csv")
if os.path.exists("data.json"):
    infile = open("data.json", "r")
    jsonData = json.load(infile)
    infile.close()
jsonData = pd.DataFrame(jsonData["data_points"])
st.success("Data Loaded!")

# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.
st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Hours Watched Per TV Show") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.
st.write("This graph shows the number of hours spent watching each TV show per week.")
st.bar_chart(jsonData, x="Show", y="Hours")

# GRAPH 2: DYNAMIC GRAPH
st.subheader("Choose a TV Show")
# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.
st.write("Choose a TV show from the dropdown or check the box to show all TV shows.")
if "chosenShow" not in st.session_state:
    st.session_state.chosenShow = csvData["Category"][0]
if "showAll" not in st.session_state:
    st.session_state.showAll = False
show = st.selectbox("Choose a TV show:", csvData["Category"], key="chosenShow") #NEW
showAll = st.checkbox("Show all TV shows", key="showAll") #NEW
if showAll:
    graphData = csvData
else:
    graphData = csvData[csvData["Category"] == show]
st.line_chart(graphData, x="Category", y="Value")

# GRAPH 3: DYNAMIC GRAPH
st.subheader("TV Shows Based on Hours Watched")
st.write("Use the sliders to choose the minimum and maximum hours watched.")
if "minHours" not in st.session_state:
    st.session_state.minHours = 0
if "maxHours" not in st.session_state:
    st.session_state.maxHours = 25
minHours = st.slider("Minimum hours watched:", 0, 25, key="minHours") #NEW
maxHours = st.slider("Maximum hours watched:", 0, 25, key="maxHours") #NEW
graph3Data = jsonData[
    (jsonData["Hours"] >= minHours) &
    (jsonData["Hours"] <= maxHours)]
st.area_chart(graph3Data, x="Show", y="Hours")
