import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data on the winners and losers of Superbowl finals
df = pd.read_csv("superbowl_winners_losers.csv")

# Create a bar plot of the number of wins and losses for each team
plt.bar(df["Team"], df["Wins"], label="Wins")
plt.bar(df["Team"], df["Losses"], bottom=df["Wins"], label="Losses")
plt.legend()
plt.xlabel("Team")
plt.ylabel("Number of Wins and Losses")

# Display the bar plot in the Streamlit web page
st.pyplot()
