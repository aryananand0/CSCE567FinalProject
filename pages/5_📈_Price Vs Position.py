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
df=load_data()
st.title("Position Distribution of Players")
st.write("This graph illustrates the distribution of players across different positions, highlighting that defensive center backs are the most populated position, followed by central midfielders and central attackers. Additionally, this graph indicates positions with a higher likelihood of entry, as these roles often require more personnel due to factors such as player injuries or increased usage of these positions by teams on the field. ")
position_counts = df['position'].value_counts().reset_index()
position_counts.columns = ['Position', 'Count']

# Create bar chart for position distribution with hover information
fig = px.bar(position_counts, x='Position', y='Count',hover_data={'Position': True, 'Count': True})

# Set axis labels
fig.update_xaxes(title_text='Position')
fig.update_yaxes(title_text='Count')

# Show plot with hover information
st.plotly_chart(fig)





def load_data():
    df = pd.read_csv('top5_leagues_player.csv')
    return df
df=load_data()

st.title('Average Price by Position')
st.write("Numerous player attributes in soccer contribute to determining a player's value. While quantitative analysis is crucial in this assessment, having domain knowledge adds depth to understanding the results, potentially leading to better decision-making.")

avg_prices = df.groupby('position')['price'].mean().reset_index()

# Display bar chart using Streamlit
st.bar_chart(avg_prices.set_index('position'))
st.write("The data presented above reveals that the most valuable players are often 'second-strikers,' also known as central-attacking midfielders (CAM). Unlike traditional strikers or midfielders, second-strikers are playmakers, directing the team's gameplay. They are prized for their intelligence, spatial awareness, technical skills, finishing ability, and above all, their creativity. It's logical to observe that this position holds the highest value in the top 5 soccer leagues since a team's success often hinges on the performance of their second-striker.")
st.write("Upon analyzing the graphs, distinct patterns emerge regarding market values across different positions in soccer. Notably, midfield positions command higher prices compared to defensive roles, likely due to their significant contribution to team success through assists and playmaking. Conversely, strikers hold a premium value, which is expected given their pivotal role in scoring goals.")
st.write("In summary, there exists a clear correlation between a player's position on the field and their market value.")
