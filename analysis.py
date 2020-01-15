import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

temperature = []
stations = []
temp_by_date = []
time = []
date = []
humidity = []
temp_last_weeks = []
precipitation = []
pressure = []
windSpeed = []


def buildAvgTemperatureByStation(values):
    for value in values[0:2]:
        temperature.append(value[0])
        stations.append(value[2])

    for value in values[-2::1]:
        temperature.append((value[0]))
        stations.append(value[2])

    y_pos = np.arange(len(stations))

    plt.bar(y_pos, temperature, align='center', alpha=0.5)
    plt.xticks(y_pos, stations)
    plt.title('Two lowest and highest average temperatures measuered by stations')
    plt.ylabel('Average temperature by stations')

    plt.show()


def buildTemperatureByDate(values):
    station = values[0][1]

    for value in values:
        temp_by_date.append(value[0])
        date_value = str(value[2].partition('T')[0])
        time_value = str(value[2].partition('T')[2])
        time.append(time_value)

    plt.plot(time, temp_by_date, color='g')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Temperature measured on ' + date_value + ' from station ' + str(station))
    plt.show()


def buildWeatherDataOfLastWeeks(values):
    station = values[0][6]
    for value in values:
        date.append(value[0])
        humidity.append(value[1])
        precipitation.append(value[2])
        pressure.append(value[3])
        temp_last_weeks.append(value[4])
        windSpeed.append(value[5])

    date_labels = []
    date_labels_text = []
    for value in date[::3]:
        date_labels.append(value)
        date_labels_text.append(str(value.partition('T')[0]))

    plt.plot(date, humidity, color='b', label='Humidity')
    plt.plot(date, precipitation, color='g', label='Precipitation')
    plt.plot(date, temp_last_weeks, color='y', label='Temperature')
    plt.plot(date, windSpeed, color='c', label='Wind Speed')
    plt.legend(loc="upper left")
    plt.xlabel('Date')
    plt.xticks(date_labels, date_labels_text)
    plt.ylabel('Weather Data')
    plt.title('Weather data from station ' + str(station) + ' of the last days')
    plt.show()
