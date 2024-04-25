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
    # Remove extra spaces from nationality column and split by double spaces
    df['nationality'] = df['nationality'].str.strip().str.split('\s\s')
    # Explode the nationality column to separate names into their own rows
    df = df.explode('nationality')
    return df

df = load_data()

# Group by Nationality and League Affiliation and count the number of players
player_counts = df.groupby(['nationality', 'league']).size().reset_index(name='count')

# Create sidebar for choosing nation
chosen_nation = st.sidebar.selectbox('Choose Nation:', df['nationality'].unique())

# Filter data based on chosen nation
filtered_player_counts = player_counts[player_counts['nationality'] == chosen_nation]

# Create bar graph for distribution of players by league affiliation
fig = px.bar(filtered_player_counts, x='league', y='count', color='league',
             title=f'Distribution of Players from {chosen_nation} by League Affiliation',
             hover_name='league', hover_data={'count': True})

# Set axis labels
fig.update_xaxes(title_text='League')
fig.update_yaxes(title_text='Player Count')

# Show bar graph
st.plotly_chart(fig, use_container_width=True)