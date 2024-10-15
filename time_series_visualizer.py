import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Global variable for the DataFrame
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data
def clean_data(df):
    # Aplicamos un filtro y usamos .copy() para evitar el SettingWithCopyWarning
    df = df[(df['value'] <= df['value'].quantile(0.975)) & 
            (df['value'] >= df['value'].quantile(0.025))].copy()
    df.loc[:, "value"] = df["value"].astype(float)
  # Convertimos a float después del filtro
    return df

df = clean_data(df)

def draw_line_plot(df):
    # Draw line plot
    df['date'] = pd.to_datetime(df['date'])
    plt.figure(figsize=(20, 10))
    fig = sns.lineplot(data=df, x="date", y="value", color='blue')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save image and return fig
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot(df):
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["month"] = df_bar['date'].dt.strftime('%B')
    df_bar['Year'] = df_bar['date'].dt.year

    monthly_avg = df_bar.groupby(['Year', 'month'])['value'].mean().reset_index()

    # Order the months
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    monthly_avg['month'] = pd.Categorical(monthly_avg['month'], categories=months_order, ordered=True)

    monthly_avg.sort_values(['Year', 'month'], inplace=True)

    plt.figure(figsize=(10, 6))
    fig = sns.barplot(data=monthly_avg, x="Year", y="value", hue="month")
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.tight_layout()

    plt.savefig('bar_plot.png')
    return fig

def draw_box_plot(df):
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    plt.figure(figsize=(20, 10))
    
    # First subplot for yearly data
    plt.subplot(1, 2, 1)
    sns.boxplot(data=df_box, x='year', y='value')
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    # Second subplot for monthly data
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df_box, x='month', y='value', 
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save image and return fig
    plt.savefig('box_plot.png')
    return plt.gcf()