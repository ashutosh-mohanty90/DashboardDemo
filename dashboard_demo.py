# -*- coding: utf-8 -*-
"""Dashboard Demo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qv9SxM9HXdNZN-sDW3kABC5rjrMT166L
"""

import pandas as pd
import plotly.express as px
import streamlit as st
import glob

st.set_page_config(page_title="Dashboard Demo",
                   page_icon=":bar_chart:",
                   layout="wide")

# get the absolute path of all Excel files
allExcelFiles = glob.glob("https://github.com/ashutosh-mohanty90/DashboardDemo.git/*.xlsx")

# read all Excel files at once
df = pd.concat(pd.read_excel(excelFile,sheet_name='Sheet1',skiprows=2,usecols='B:H',nrows=8) for excelFile in allExcelFiles)

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
ProjectName = st.sidebar.multiselect(
    "Select the Project:",
    options=df["Project_Name"].unique(),
    default=df["Project_Name"].unique()
)

df_selection = df.query("Project_Name == @ProjectName")
st.dataframe(df_selection)

