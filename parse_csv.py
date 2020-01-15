import csv

csvfile = './resources/data.csv'
stations = []
observations = []

f1 = open(csvfile, encoding='utf-8')


def parseStations():
    readCSV = csv.reader(f1, delimiter=',')
    # Skip the first entry (descriptors) of the csv
    iterCsv = iter(readCSV)
    next(iterCsv)

    for row in iterCsv:
        lat = row[7]
        lon = row[8]
        stationID = row[9]
        stationName = row[10]
        values = (lat, lon, stationID, stationName)
        if values not in stations:
            stations.append(values)
    f1.close()
    return stations


def parseObservations():
    f1 = open(csvfile, encoding='utf-8')
    readCSV = csv.reader(f1, delimiter=',')
    # Skip the first entry (descriptors) of the csv
    iterCsv = iter(readCSV)
    next(iterCsv)

    for row in iterCsv:
        stationID = row[9]
        humidity = row[0]
        precipitation = row[1]
        pressure = row[2]
        temperature = row[3]
        windDirection = row[4]
        # TODO: Null if not there
        windSpeed = row[5]
        time = row[6]
        values = (stationID, humidity, precipitation, pressure, temperature, windDirection, windSpeed, time)
        if values not in observations:
            observations.append(values)
    f1.close()
    return observations
