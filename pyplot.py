import pandas as pd
import matplotlib.pyplot as plt
x=[1,2,3,4]
y={'y=f(x)':[2,8,4,6], 'z=g(x)':[4,6,8,2]}
df=pd.DataFrame(y, x)
df.plot(grid=True, title='My first line graph', xlabel='x  -->', ylabel='y=f(x), z=g(x)  -->', ylim=(1,10), xlim=(1,5))
plt.show()