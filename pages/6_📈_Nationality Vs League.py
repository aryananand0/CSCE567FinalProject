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
st.title("Nationality by League Affiliation")
st.write("This graph visually represents the distribution of players from each country across the top 5 soccer leagues. It provides insight into nations with the most top players, as countries with players in these elite leagues are often considered to have a stronger footballing pedigree. This is because players who regularly compete in the top 5 leagues gain invaluable experience facing the best competition week in and week out, enhancing their skills and adaptability. Consequently, players from these nations tend to command higher values due to their exposure to top-level football and the competitive edge it fosters. This graph serves as a reflection of the global talent pool in football, showcasing the countries that produce players capable of thriving in the most prestigious leagues worldwide.")
st.write("To interact with this graph effectively, you can utilize the sidebar to select and view the distribution of players from any country you're interested in. Simply choose the country you want to explore, and the graph will dynamically update to show you how many players from that country are present in each of the top 5 soccer leagues. Additionally, hovering over each segment of the graph provides detailed information, giving you precise numbers of players in each league right at your fingertips. This interactive functionality enhances your ability to analyze and understand the global distribution of players across these prestigious leagues, offering a comprehensive view of football talent worldwide.")
# Create bar graph for distribution of players by league affiliation
fig = px.bar(filtered_player_counts, x='league', y='count', color='league',
             title=f'Distribution of Players from {chosen_nation} by League Affiliation',
             hover_name='league', hover_data={'count': True})

# Set axis labels
fig.update_xaxes(title_text='League')
fig.update_yaxes(title_text='Player Count')

# Show bar graph
st.plotly_chart(fig, use_container_width=True)
