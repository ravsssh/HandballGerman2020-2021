import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify

totalattemp_df = pd.read_csv("totalattemp_df.csv", delimiter=',')
totalattemp_df.set_index('Team', inplace=True)
color_palette = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightblue']
st.title('What a Team Tendencies To Shot Per 100 :man-playing-handball:')
selected_team = st.selectbox('Select a team', totalattemp_df.index)
shot_attempts = totalattemp_df.loc[selected_team]
total_attempts = shot_attempts.sum()
shot_percentages = shot_attempts / total_attempts
labels = [f'{label}\n({percentage:.1%})' for label, percentage in zip(shot_percentages.index, shot_percentages.values)]
sizes = shot_percentages.values
fig, ax = plt.subplots(figsize=(8, 8))
squarify.plot(sizes=sizes, label=labels, color=color_palette, ax=ax)
ax.set_title(f'Shot Attempts for {selected_team}')
ax.set_xlabel('Shot Type')
ax.set_ylabel('Total Shot Attempt')
plt.tick_params(axis='both', which='both', bottom=False, left=False)
st.pyplot(fig)
