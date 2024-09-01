import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_rides_by_day(data):
    day_counts = data['DayOfWeek'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=day_counts.index, y=day_counts.values, palette='viridis', hue=day_counts.index, legend=False)
    plt.title('Number of rides by day of the week')
    plt.xlabel('Day of the week')
    plt.ylabel('Number of rides')
    plt.show()


def plot_rides_by_day_for_each_month(data, months_order):
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    data_agg = data.groupby(['Month', 'DayOfWeek']).size().reset_index(name='count')

    data_agg['Month'] = pd.Categorical(data_agg['Month'], categories=months_order, ordered=True)

    plt.figure(figsize=(14, 8))

    sns.barplot(data=data_agg, x='Month', y='count', hue='DayOfWeek', hue_order=days_order, palette='tab10')

    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Distribution of data by day of the week for each month')
    plt.legend(title='Day of the Week', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()

    plt.show()



def plot_rides_by_day_of_month(data):
    plt.figure(figsize=(10,6))
    sns.histplot(data['Day'], bins=31, kde=False)
    plt.title('Distribution of pickups by days of month')
    plt.xlabel('Day of the Month')
    plt.ylabel('Number of Pickups')
    plt.xticks(range(1, 32))
    plt.show()

def plot_rides_by_day_for_specific_month(data, month):
    month_data = data[data['Month'] == month]

    plt.figure(figsize=(10,6))
    sns.histplot(month_data['Day'], bins=31, kde=False)
    plt.title(f'Distribution of pickups by days in {month}')
    plt.xlabel('Day of the month')
    plt.ylabel('Number of pickups')
    plt.xticks(range(1, 32))
    plt.show()

def plot_rides_by_hour(data):
    hour_counts = data['Hour'].value_counts().sort_index()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=hour_counts.index, y=hour_counts.values, palette='viridis', hue=hour_counts.index, legend=False)
    plt.title('Number of rides by hour of the day')
    plt.xlabel('Hour of the day')
    plt.ylabel('Number of rides')
    plt.show()

def plot_rides_by_month(data):
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    month_counts = data['Month'].value_counts()
    
    month_counts = month_counts.reindex(month_order).dropna()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=month_counts.index, y=month_counts.values, palette='viridis', hue=month_counts.index, legend=False)
    plt.title('Number of rides by month')
    plt.xlabel('Month')
    plt.ylabel('Number of rides')
    plt.xticks(rotation=45)  
    plt.show()
