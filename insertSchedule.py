import mysql.connector
from mysql.connector import Error
import datetime

from parameters import *


def insertSchedules(data):
    print(data)
    try:
        connection = mysql.connector.connect(host=DB_HOSTNAME,
                                             database=DB_NAME,
                                             user=DB_USER,
                                             password=DB_PASSWORD)

        if connection.is_connected():
            cursor = connection.cursor()

            dataValues = (data["timestamp"], data["filename"], data["frequency"], data["hostname"], data["port"], data["band"], data["duration"])
            insert_stmp = "INSERT INTO schedule (timestamp, filename, frequency, hostname, port, band, duration) VALUES (%s, %s, %s, %s, %s, %s)"

            cursor.execute(insert_stmp, dataValues)

        else:
            raise RuntimeError("Could not connect to database")
    except Error as e:
        print ("Error while connecting to MySQL", e)
        raise e
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
