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
        width=700,
        height=400
    ).interactive()

    return chart

# Load data from CSV file
data = load_data()

# Display the data table
st.title('Club Market Value Comparison')
st.write("This visualization serves as a comprehensive tool for understanding the value distribution among clubs within the selected league. Its primary function is to depict the relative values of all clubs, enabling us to identify the most valuable club in each league. Additionally, this visualization facilitates the assessment of value disparities within the league, shedding light on the economic dynamics and financial strengths of individual clubs.")
st.write("Furthermore, this visualization offers a valuable opportunity to compare leagues directly. By juxtaposing multiple leagues side by side and examining the values of their respective clubs, users can gain insights into the comparative financial landscapes of different football leagues. This comparative analysis extends beyond individual clubs to provide a broader perspective on the economic competitiveness and market dynamics across various football leagues.")
st.write("In essence, this visualization empowers users to explore and analyze the financial aspects of football leagues, offering a nuanced understanding of club values, league disparities, and inter-league comparisons.")
st.write("To intact with this visualization you only have to choose what league or leagues you want to visualize and it will make a bar graph visualizing it for you")
st.write("")


# Sidebar for selecting leagues
selected_leagues = st.sidebar.multiselect('Select Leagues', data['league'].unique())

# Plot the bar chart
st.altair_chart(plot_bar_chart(data, selected_leagues))