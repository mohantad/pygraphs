import pandas as pd
import matplotlib.pyplot as plt
months=["Jan", "Feb", "Mar", "Apr"]
temp=[2,8,4,6]
aqi=[4,6,8,2]
df=pd.DataFrame({'temp':temp, 'aqi':aqi}, months)
df2=pd.DataFrame([[temp[0],aqi[0]],[temp[1],aqi[1]],[temp[2],aqi[2]], [temp[3],aqi[3]]], columns=["temp", "aqi"])

df.plot(kind='line', title='Temperature~Air quality line chart', grid=True, xlabel='months  -->', ylabel='temp, aqi  -->', ylim=(1,10), xlim=(0,5), figsize=(10, 8))
df.plot(kind='bar', title='Temperature~Air quality bar chart', grid=True, xlabel='months  -->', ylabel='temp, aqi  -->', ylim=(1,10), xlim=(0,5), figsize=(10, 8))
df.plot(kind='area', title='Temperature~Air quality area chart', grid=True, xlabel='months  -->', ylabel='temp, aqi  -->', ylim=(1,10), xlim=(0,5), figsize=(10, 8))
df2.plot(kind='scatter', title='Temperature~Air quality scatter chart', x="temp", y="aqi", s=100, c=['tomato', 'aqua', 'peachpuff', 'yellowgreen'], grid=True, xlabel='aqi  -->', ylabel='temp -->', ylim=(0,10), xlim=(0,10), figsize=(10, 8))
df.plot(kind='pie', title='Temperature~Air quality Pie chart', subplots=True, shadow = True, startangle = 180, explode =(0,0.05,0,0.05),  autopct ='%1.1f%%', colors=['tomato', 'aqua', 'peachpuff', 'yellowgreen'], figsize=(10, 8))
plt.show()