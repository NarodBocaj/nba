import pandas as pd
import os
import matplotlib.pyplot as plt


__location__ = os.path.dirname(os.path.abspath(__file__))

df_reg_season = pd.read_csv(os.path.join(__location__, 'reg_season_gmscore.csv'))
df_playoff = pd.read_csv(os.path.join(__location__, 'playoff_gmscore.csv'))


def make_plot(df, playoff = False):
    df["Date"] = pd.to_datetime(df["Date"])
    
    mask = (df["Date"].dt.year == 2020) & (df["Date"].dt.month >= 12) | (df["Date"].dt.month > 9) & (df["Date"].dt.year != 2020)

    df["Season"] = (df["Date"].dt.year + mask)

    
    season_counts = df["Season"].value_counts()
    season_counts_sorted = season_counts.sort_index()
    year_min = df['Season'].min()
    year_max = df['Season'].max()
    
    years_range = range(year_min, year_max + 1)
    plt.bar(season_counts_sorted.index, season_counts_sorted.values)

    plt.xlim(right=df['Season'].max() + 1)
    plt.xlabel('Year')
    plt.xticks(years_range, years_range)
    plt.xticks(rotation=75)
    plt.ylabel('Count')
    if playoff:
        plt.title('Top 100 Playoff Gamescores by Season')
        plt.savefig("playoff_gm_score.png", dpi = 200)
    else:
        plt.title('Top 100 Regular Season Gamescores by Season')
        plt.savefig("reg_season_gm_score.png", dpi = 200)
    plt.clf()


make_plot(df_playoff, True)
make_plot(df_reg_season)