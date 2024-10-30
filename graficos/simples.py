import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import io

def distance_over_time(records):
    # Extracting data for plotting
    distances = [record[1] for record in records]
    dates = [datetime.strptime(record[3], '%Y-%m-%d') for record in records]

    # Creating the plot
    plt.figure(figsize=(10, 5))
    plt.plot(dates, distances, color='tab:blue', marker='o', label='Distance (km)')

    # Formatting the x-axis to show dates properly
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()

    # Adding labels and title
    plt.xlabel('Date')
    plt.ylabel('Distance (km)')
    plt.title('Distance over Time')
    plt.legend()

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img

def duration_over_time(records):
    # Extracting data for plotting
    minutes = [record[2] for record in records]
    dates = [datetime.strptime(record[3], '%Y-%m-%d') for record in records]

    # Creating the plot
    plt.figure(figsize=(10, 5))
    plt.plot(dates, minutes, color='tab:red', marker='x', label='Minutes')

    # Formatting the x-axis to show dates properly
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()

    # Adding labels and title
    plt.xlabel('Date')
    plt.ylabel('Minutes')
    plt.title('Minutes over Time')
    plt.legend()

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img

def total_sums(records):
    # Save all the values to variable
    minutes = [record[2] for record in records]
    distances = [record[1] for record in records]

    # Sum all values and then round 2 decimals
    total_minutes = round(sum(minutes),2)
    total_distances = round(sum(distances),2)

    return [total_distances,total_minutes]
