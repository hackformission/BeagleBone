import mysql.connector
from mysql.connector import Error
import datetime

from parameters import *

def loadSchedules():
    try:
        connection = mysql.connector.connect(host=DB_HOSTNAME,
                                             database=DB_NAME,
                                             user=DB_USER,
                                             password=DB_PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()

            schedules = []

            # Create query to load the schedule records from the database and return a dictionary of the parameters
            now = datetime.datetime.now()
            cursor.execute("SELECT * FROM schedule WHERE timestamp >= '{}'".format(now))

            for row in cursor.fetchall():
                # For each row in the result set create a dictionary of "parameters" for the scheduled job
                params = dict()
                params['schedule_id'] = row[0]
                params['time'] = row[1]
                params['filename'] = row[2]
                params['freq'] = row[3]
                params['station'] = row[4]
                params['port'] = row[5]
                params['mode'] = row[6]
                params['duration'] = row[7]

                schedules.append(params)

            return schedules
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