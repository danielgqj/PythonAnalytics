import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
st.title('Reporte de emisiones Co2 en vehículos de Canadá')



data = pd.read_csv('./Co2/CO2 Emissions_Canada.csv')



st.sidebar.header("Please Filter Here:")
Marca = st.sidebar.multiselect(
    "Select the City:",
    options=data["Make"].unique(),
    default=data["Make"].unique()
)

data_selection = data.query(
    "Make == @Marca"
)
st.dataframe(data_selection)



