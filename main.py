from analysis import buildAvgTemperatureByStation, buildTemperatureByDate, buildWeatherDataOfLastWeeks
from db_connection import createTabels, openConnection, insertStationValues, closeConnection, insertObservationValues, \
    getTemperaturesByDate, getWeatherDataOfLastMonths, getAvgTemperature
from parse_csv import parseStations, parseObservations
from user_interface import get_booleanParameter, get_intParameter, get_dateParameter


def main():
    # Handle the user inputs
    create_db_tabels = get_booleanParameter("Should the initial database model be loaded? ")
    insert_values = get_booleanParameter("Should values be inserted into the database? ")
    station = get_intParameter("Please enter a station ID: ")
    date = get_dateParameter("Please enter a date (in ISO Format): ")

    conn = openConnection()
    if create_db_tabels:
        createTabels(conn)

    if insert_values:
        station_values = parseStations()
        observation_values = parseObservations()

        insertStationValues(conn, station_values)
        insertObservationValues(conn, observation_values)

    avg_temperature = getAvgTemperature(conn)
    temperature_by_date = getTemperaturesByDate(conn, station, date)
    weather_data = getWeatherDataOfLastMonths(conn, station)
    buildTemperatureByDate(temperature_by_date)
    buildAvgTemperatureByStation(avg_temperature)
    buildWeatherDataOfLastWeeks(weather_data)
    closeConnection(conn)


if __name__ == "__main__":
    main()
