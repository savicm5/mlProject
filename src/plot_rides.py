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

def plot_rides_by_day_of_month(data):
    plt.figure(figsize=(10,6))
    sns.histplot(data['Day'], bins=31, kde=False)
    plt.title('Distribution of Pickups by Days of Month')
    plt.xlabel('Day of the Month')
    plt.ylabel('Number of Pickups')
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

def plot_rides_by_month(data, month_order):
    month_counts = data['Month'].value_counts().reindex(month_order)
    print(month_counts)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=month_counts.index, y=month_counts.values, palette='viridis', hue=month_counts.index, legend=False)
    plt.title('Number of rides by month')
    plt.xlabel('Month')
    plt.ylabel('Number of rides')
    plt.show()
