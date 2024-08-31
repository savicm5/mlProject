import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_rides_by_day(data):
    data['DAY'] = data['DATETIME'].dt.day_name()
    day_counts = data['DAY'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=day_counts.index, y=day_counts.values, palette='viridis', hue=day_counts.index, legend=False)
    plt.title('Number of rides by day of the week')
    plt.xlabel('Day of the week')
    plt.ylabel('Number of rides')
    plt.show()

def plot_rides_by_hour(data):
    data['HOUR'] = data['DATETIME'].dt.hour
    hour_counts = data['HOUR'].value_counts().sort_index()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=hour_counts.index, y=hour_counts.values, palette='viridis', hue=hour_counts.index, legend=False)
    plt.title('Number of rides by hour of the day')
    plt.xlabel('Hour of the day')
    plt.ylabel('Number of rides')
    plt.show()

def plot_rides_by_month(data, month_order):
    data['MONTH'] = data['DATETIME'].dt.month_name()
    month_counts = data['MONTH'].value_counts().reindex(month_order)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=month_counts.index, y=month_counts.values, palette='viridis', hue=month_counts.index, legend=False)
    plt.title('Number of rides by month')
    plt.xlabel('Month')
    plt.ylabel('Number of rides')
    plt.show()
