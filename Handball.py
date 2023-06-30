import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

color_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

st.set_page_config(
    page_title="Liqui Moly Handball 2021-2022 Statistic",
    page_icon=":man-playing-handball:"
)
df = pd.read_csv('Player.csv', delimiter=';')
totalteam_df = df.groupby('Team')[['7M Goal', '7M Shot', '6M Goal', '6M Shot', '9M Goal', '9M Shot',
                                   'Wing Goal', 'Wing Shot', 'Pivot Goal', 'Pivot Shot', 'Fastbreak Goal',
                                   'Fastbreak Shot']].sum()
totalteam_df = totalteam_df.reset_index()
totalteam_df['7M Accuracy'] = (totalteam_df['7M Goal'] / totalteam_df['7M Shot']).round(2)
totalteam_df['6M Accuracy'] = (totalteam_df['6M Goal'] / totalteam_df['6M Shot']).round(2)
totalteam_df['9M Accuracy'] = (totalteam_df['9M Goal'] / totalteam_df['9M Shot']).round(2)
totalteam_df['Wing Accuracy'] = (totalteam_df['Wing Goal'] / totalteam_df['Wing Shot']).round(2)
totalteam_df['Pivot Accuracy'] = (totalteam_df['Pivot Goal'] / totalteam_df['Pivot Shot']).round(2)
totalteam_df['Fastbreak Accuracy'] = (totalteam_df['Fastbreak Goal'] / totalteam_df['Fastbreak Shot']).round(2)
totalteamacc_df = totalteam_df.loc[:, ['Team', '7M Accuracy', '6M Accuracy', '9M Accuracy', 'Pivot Accuracy',
                                       'Fastbreak Accuracy', 'Wing Accuracy']]
totalteam_df = totalteam_df.drop(
    ['7M Accuracy', '6M Accuracy', '9M Accuracy', 'Pivot Accuracy', 'Fastbreak Accuracy', 'Wing Accuracy'],
    axis=1)
totalteamacc_df['Team Rank'] = [3, 11, 5, 16, 13, 17, 12, 14, 9, 8, 18, 10, 1, 4, 6, 2, 15, 7]
totalteamacc_df = totalteamacc_df.sort_values('Team Rank').reset_index(drop=True)
totalteamacc_df = totalteamacc_df.drop('Team Rank', axis=1)
shot_types = totalteamacc_df.columns[1:]
st.subheader("Shot Accuracy In League Per Team :dart:")
selected_shot_type = st.selectbox("Select Shot Type", shot_types, key="shot_acc_dropdown")
filtered_data = totalteamacc_df[['Team', selected_shot_type]]
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Team'], filtered_data[selected_shot_type] * 100,
         color=color_palette[shot_types.get_loc(selected_shot_type)],
         linewidth=2, marker='o', markersize=6)
plt.xlabel('Team Rank 1-18', fontsize=12)
plt.ylabel(selected_shot_type + ' (%)', fontsize=12)
plt.title(f'{selected_shot_type} For Each Team', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
ymin = (filtered_data[selected_shot_type] * 100).min() - 10
ymax = (filtered_data[selected_shot_type] * 100).max() + 10
plt.ylim(ymin, ymax)
col_average = filtered_data[selected_shot_type].mean() * 100
plt.axhline(y=col_average, color='red', linestyle='--', linewidth=2, label='Average')
plt.legend(loc='upper right')
plt.tight_layout()
st.pyplot(plt)
df = pd.read_csv("Player.csv", delimiter=';')
totalteam_df = df.groupby('Team')[['7M Goal', '7M Shot', '6M Goal', '6M Shot', '9M Goal', '9M Shot',
                                   'Wing Goal', 'Wing Shot', 'Pivot Goal', 'Pivot Shot', 'Fastbreak Goal',
                                   'Fastbreak Shot']].sum()
noteam_df = totalteam_df.copy()
if 'Team' in noteam_df.columns:
    noteam_df.drop('Team', axis=1, inplace=True)
st.subheader("3 Highest Shot Attemp or Shot Goal In League :goal_net:")
selected_type = st.selectbox('Select Shot Type', noteam_df.columns)
top_three = totalteam_df[selected_type].nlargest(3)
plt.figure(figsize=(8, 6))
ax = sns.barplot(x=top_three.index, y=top_three.values, linewidth=0.2, edgecolor='black')
plt.title(f'Top 3 \n {selected_type}', fontsize=14)
plt.xticks(range(len(top_three.index)), top_three.index, rotation=45, ha='right') 
for i, v in enumerate(top_three.values):
    ax.text(i, v, str(v), horizontalalignment='center', verticalalignment='bottom', fontweight='light')
ax.set_xlabel('')
plt.tight_layout()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()  
