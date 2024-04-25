import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

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

# Create sidebar for choosing nation
chosen_country = st.sidebar.selectbox('Choose Country:', df['nationality'].unique())

# Filter data based on chosen country and include players with dual nationalities
filtered_df = df[df['nationality'].apply(lambda x: chosen_country in x)]

# Create bar graph for each player's market value by nationality using Plotly
fig = go.Figure()
for player in filtered_df['name'].unique():
    player_data = filtered_df[filtered_df['name'] == player]
    fig.add_trace(go.Bar(x=[player_data['nationality'].iloc[0]], y=[player_data['price'].iloc[0]], name=player))

# Customize the layout
fig.update_layout(title=f'Market Value of Players by Nationality ({chosen_country})',
                  xaxis_title='Nationality', yaxis_title='Market Value', barmode='group')

# Show plot
st.plotly_chart(fig)



# df = load_data()

# # Create sidebar for choosing nation
# chosen_country = st.sidebar.selectbox('Choose Country:', df['nationality'].unique())

# # Filter data based on chosen country and include players with dual nationalities
# filtered_df = df[df['nationality'].apply(lambda x: chosen_country in x)]

# # Create scatter plot for nationality vs. market value
# fig = px.scatter(filtered_df, x='nationality', y='price',
#                  title=f'Relationship between Player Nationality ({chosen_country}) and Market Value',
#                  hover_name='name', hover_data={'nationality': True, 'price': ':$,.0f'})

# # Set axis labels
# fig.update_xaxes(title_text='Nationality')
# fig.update_yaxes(title_text='Market Value')

# # Show plot
# st.plotly_chart(fig)