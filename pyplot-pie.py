import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
  "2016": [160, 60, 70, 60],
  "2017": [175, 65, 75, 65]},
  index= ["Python", "Java", "C++", "C"]
)

#creating the plot
df.plot.pie(subplots=True, figsize=(10, 6))

#displaying the plot
plt.show()