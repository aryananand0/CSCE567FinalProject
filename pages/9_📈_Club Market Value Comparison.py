import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import csv
from bokeh.plotting import figure
import altair as alt

def load_data():
    df = pd.read_csv('top5_leagues_player.csv')
    return df

def plot_bar_chart(data, selected_leagues):
    filtered_data = data[data['league'].isin(selected_leagues)]
    chart = alt.Chart(filtered_data).mark_bar().encode(
        x='club',
        y=alt.Y('price', title='Market Value'),
        tooltip=['club', 'price']
    ).properties(
        title='Club Market Value Comparison',
        width=700,
        height=400
    ).interactive()

    return chart

# Load data from CSV file
data = load_data()

# Display the data table
st.title('Club Market Value Comparison')


# Sidebar for selecting leagues
selected_leagues = st.sidebar.multiselect('Select Leagues', data['league'].unique())

# Plot the bar chart
st.write("## Vertical Bar Chart")
st.altair_chart(plot_bar_chart(data, selected_leagues))