import pandas as pd
import os
import matplotlib.pyplot as plt

__location__ = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(__location__, 'fullseason_stats.csv'))
df["FTA/2PTFGA"] = df['FTA'] / (df['FGA'] - df['3PA'])


print(df)

plt.plot(df["Season"], df["FTA/2PTFGA"])
plt.gca().invert_xaxis()
plt.xticks(rotation=75)
plt.xlabel('Season')
plt.ylabel('FTA/2PT FGA')
plt.title('FTA per 2pt FGA by Season')
plt.show()