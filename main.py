from analysis import buildAvgTemperatureByStation, buildTemperatureByDate, buildWeatherDataOfLastWeeks
from db_connection import createTabels, openConnection, insertStationValues, closeConnection, insertObservationValues, \
    getAvgTemperatureByStation, getTemperaturesByDate, getWeatherDataOfLastMonths
from parse_csv import parseStations, parseObservations


def main():
    createDBTabels = True
    insertValues = True

    conn = openConnection()
    if (createDBTabels):
        createTabels(conn)

    if (insertValues):
        station_values = parseStations()
        observationValues = parseObservations()

        insertStationValues(conn, station_values)
        insertObservationValues(conn, observationValues)

    avg_temperature = getAvgTemperatureByStation(conn, 540, 550)
    temperature_by_date = getTemperaturesByDate(conn, 789, '2015-08-03')
    weather_data = getWeatherDataOfLastMonths(conn, 575)
    buildTemperatureByDate(temperature_by_date)
    buildAvgTemperatureByStation(avg_temperature)
    buildWeatherDataOfLastWeeks(weather_data)
    closeConnection(conn)


if __name__ == "__main__":
    main()
