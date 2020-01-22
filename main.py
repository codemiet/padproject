from analysis import buildAvgTemperatureByStation, buildTemperatureByDate, buildAllWeatherData
from db_connection import createTabels, openConnection, insertStationValues, closeConnection, insertObservationValues, \
    getTemperaturesByDate, getAllWeatherData, getAvgTemperature
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
        print('Database schema created...')

    if insert_values:
        print('Parsing the input file...')
        station_values = parseStations()
        observation_values = parseObservations()
        print('Input file parsed...')

        print('Inserting values into the database...')
        insertStationValues(conn, station_values)
        insertObservationValues(conn, observation_values)
        print('Values inserted...')

    avg_temperature = getAvgTemperature(conn)
    temperature_by_date = getTemperaturesByDate(conn, station, date)
    weather_data = getAllWeatherData(conn, station)
    buildTemperatureByDate(temperature_by_date)
    buildAvgTemperatureByStation(avg_temperature)
    buildAllWeatherData(weather_data)
    closeConnection(conn)


if __name__ == "__main__":
    main()
