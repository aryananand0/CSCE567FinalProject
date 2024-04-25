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


target_leagues = ['EPL', "LaLiga","Bundesliga","SerieA","Ligue1","Other"]

def average_age(name):
    target_df = df[df['league'] == name]
    average_age_target_league = target_df['age'].mean()
    average_age_one_decimal = round(average_age_target_league, 1)
    return average_age_one_decimal
ages_of_top_5_league =[]

for i in target_leagues:
    ages_of_top_5_league. append(average_age(i))
    


data = {'league': target_leagues,
        'age': ages_of_top_5_league}
df = pd.DataFrame(data)
st.write("This Visulization show the league and there average age. This viulization shows the age")
# Create scatter plot
fig = px.scatter(df, x='league', y='age', text='age', title='Average Player Age Across Top 5 Leagues')

# Update text position    
fig.update_traces(textposition='top center')

# Display the scatter plot
st.plotly_chart(fig)