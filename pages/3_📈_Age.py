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
st.title("Age Vs League")
st.write("This visualization displays the average age for each league. Understanding the average age of players is crucial as it significantly impacts both player valuation and the overall league value. To create this visualization, I collected age data from each league, calculated the average, and plotted the results.")
# Create scatter plot
fig = px.scatter(df, x='league', y='age', text='age', title='Average Player Age Across Top 5 Leagues')
# Update text position    
fig.update_traces(textposition='top center')

# Display the scatter plot
st.plotly_chart(fig)


df=load_data()

st.title('Average Price by age')

if 'age' in df.columns and 'price' in df.columns and df['age'].dtype in [int, float] and df['price'].dtype in [int, float]:
    st.write("This graph is depicting the market value of players in top leagues across different ages reveals intriguing trends. Initially, from around age 14 to 24, we observe a consistent rise in the average market value. However, a notable decline becomes evident after the age of 25-26, indicating a shift in market dynamics as players mature.")
    st.write("A striking peak is noticeable at age 23, suggesting a potential prime age where players command higher market values. This finding aligns with common perceptions of athletes hitting their peak performance levels around this age.")
    st.write("Despite these trends depicted by the graph, soccer, like many sports, showcases outliers that challenge these conventional patterns. Players such as Lionel Messi (aged 36) and Cristiano Ronaldo (aged 38) defy the expected decline in market value with age. Their sustained high valuations, even at older ages, highlight the complexities of player valuation in soccer.")
    st.write("This discrepancy between expected trends and real-world examples underscores the nuanced nature of player valuation in the soccer industry. It emphasizes the influence of exceptional talent, longevity, and market demand in shaping player market values, adding layers of complexity to our understanding of player economics in top leagues.")
    # Create line plot using seaborn with hover information
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x='age', y='price', ax=ax, markers=True, dashes=False)
    ax.set_title('Price vs Age')
    ax.set_xlabel('Age')
    ax.set_ylabel('Price')

    # Add hover information
    hover_data = {
        'Age': df['age'],
        'Price': df['price']
    }
    for line in ax.lines:
        line.set_picker(True)
    ax.format_xdata = lambda x: f'Age: {x:.2f}'
    ax.format_ydata = lambda y: f'Price: {y:.2f}'
    ax.legend(labels=['Price vs Age'], loc='upper left')

    # Display the plot using st.pyplot()
    st.pyplot(fig)
else:
    st.write('Error: Unable to plot. Check column names and data types.')
# Display the plot using st.pyplot()
