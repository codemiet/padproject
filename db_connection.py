import sqlite3


def openConnection():
    conn = sqlite3.connect('./resources/ema-201508.db')
    return conn


def createTabels(conn):
    c = conn.cursor()
    # Create table
    c.executescript('''CREATE TABLE IF NOT EXISTS "station" (
        "lat"	INTEGER NOT NULL,
        "lon"	INTEGER NOT NULL,
    	"stationID"	INTEGER NOT NULL,
    	"stationName"	VARCHAR(128) NOT NULL,
    	PRIMARY KEY("stationID")
    	UNIQUE(stationID)
    );
    CREATE TABLE IF NOT EXISTS "observation" (
	"observationID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"stationID"	INTEGER NOT NULL,
    "humidity"	INTEGER NOT NULL,
	"precipitation"	INTEGER NOT NULL,
	"pressure"	INTEGER NOT NULL,
	"temperature"	REAL NOT NULL,
	"windDirection"	VARCHAR(4) NOT NULL,
	"windSpeed"	REAL NOT NULL ,
	"time" DATE NOT NULL,
    FOREIGN KEY(stationID) REFERENCES station(stationID)
    UNIQUE(observationID)
);
    ''')


def insertStationValues(conn, station_values):
    for values in station_values:
        query = (
            "INSERT OR IGNORE INTO station('lat', 'lon', 'stationID', 'stationName') VALUES (?,?,?,?)")
        with conn:
            cur = conn.cursor()
            cur.execute(query, values)


def insertObservationValues(conn, cur_observation_values):
    for values in cur_observation_values:
        query = (
            "INSERT OR IGNORE INTO observation('stationID', 'humidity', 'precipitation', 'pressure', 'temperature', 'windDirection', 'windSpeed', 'time') VALUES (?,?,?,?,?,?,?,?)")
        with conn:
            cur = conn.cursor()
            cur.execute(query, values)


def getAvgTemperatureByStation(conn, startStationID, endStationID):
    query = "SELECT avg(temperature), observation.stationID, station.stationName FROM observation INNER JOIN station ON observation.stationID = station.stationID GROUP BY observation.stationID ORDER BY AVG(temperature) ASC"
    with conn:
        cur = conn.cursor()
        cur.execute(query)
    return cur.fetchall()


def getTemperaturesByDate(conn, stationID, date):
    query = "SELECT temperature, stationID, time FROM observation WHERE stationID = ? AND time LIKE (?)"
    with conn:
        cur = conn.cursor()
        cur.execute(query, [stationID, '%' + date + '%'])
    return cur.fetchall()


def getWeatherDataOfLastMonths(conn, stationID):
    query = "SELECT time, AVG(humidity), AVG(precipitation), AVG(pressure), AVG(temperature), AVG(windSpeed), stationID from observation where stationID = ? group by strftime('%d', time)"
    with conn:
        cur = conn.cursor()
        cur.execute(query, [stationID])
    return cur.fetchall()


def closeConnection(conn):
    if conn:
        conn.close()
