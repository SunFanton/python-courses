import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

# Clean data
filter_percentil_bottom_two_dot_five = df["value"] >= df["value"].quantile(0.025)
filter_percentil_top_two_dot_five = df["value"] <= df["value"].quantile(1 - 0.025)

df = df[filter_percentil_bottom_two_dot_five & filter_percentil_top_two_dot_five]


def draw_line_plot():
    df_copy = df.copy()
    
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15,6))
    ax.plot(df_copy.index, df_copy["value"], color="red")
    date_format = mdates.DateFormatter('%Y-%m') 
    ax.xaxis.set_major_formatter(date_format)
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_copy = df.copy()
    df_grouped = df_copy.groupby([df.index.year, df.index.month]).mean()
    df_grouped.index = pd.MultiIndex.from_tuples(df_grouped.index, names=['year', 'month'])
    df_grouped.columns = ["average_page_views"]
    df_grouped["average_page_views"] = df_grouped["average_page_views"].astype(int)
    df_pivot = df_grouped.reset_index().pivot(index='year', columns='month', values='average_page_views')

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8,8))
    df_pivot.plot.bar(ylabel="Average Page Views", xlabel="Years", legend=True, ax=ax)
    plt.legend(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], title="Months")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)
    df_box.sort_values('month',inplace=True)

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(25,8))
    sns.boxplot(
        x="year",
        y="value",
        hue="year",
        data=df_box,
        ax=ax1
    )
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    sns.boxplot(
        x="month",
        y="value",
        hue="month",
        data=df_box,
        ax=ax2
    )
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
