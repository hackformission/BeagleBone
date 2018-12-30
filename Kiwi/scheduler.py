"""
Demonstrates how to schedule a job to be run in a process pool on 3 second intervals.
"""
# from kiwirecorder import kiwirecorder
import json
from datetime import datetime

import mysql
from mysql.connector import Error

from Kiwi.parameters import DB_HOSTNAME, DB_NAME, DB_USER, DB_PASSWORD
from record import record as rssi_record

import logging
import os

from apscheduler.schedulers.background import BackgroundScheduler

logger = logging.getLogger(__name__)
logging.basicConfig()

class Scheduler:
    def __init__(self):
        # intervals = input('how many seconds?')
        logger.info("start")
        self.scheduler = BackgroundScheduler(logger=logger)
        # scheduler.add_job(information, 'interval', seconds=15)
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

        self.scheduler.start()

    def addJob(self, params):
        print("Adding job to run at {}...".format(params['time']))
        self.scheduler.add_job(self._record, 'date', run_date=params['time'], args=[params])
        
    def _record(self, params):
        print("Recording from {}:{} for frequency {} in mode {} for duration {}s for time {}".format(
            params['station'],
            params['port'],
            params['freq'],
            params['mode'],
            params['duration'],
            params['time']
        ))
        rssi_values, filename, schedule_id = rssi_record(params['station'], params['port'], params['freq'], params['mode'], params['duration'], params['schedule_id'])
        saveRecording(rssi_values, filename, schedule_id)

    def stop(self):
        self.scheduler.shutdown()


# Save the given recording to the database.
def saveRecording(rssiValues, recordingFilename, scheduleId):
    try:
        connection = mysql.connector.connect(host=DB_HOSTNAME,
                                             database=DB_NAME,
                                             user=DB_USER,
                                             password=DB_PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()

            # Insert the given rssi values and recording filename into the recordings table
            recordingFile = readFile(recordingFilename)

            rssiJson = json.dumps(rssiValues)
            cursor.execute(
                "INSERT INTO recording (schedule, RSSI_file, recording) VALUES (%s, %s, %s)",
                (
                    scheduleId,
                    rssiJson,
                    recordingFile
                )
            )
            connection.commit()

            print("Saved recording for schedule ID: {}".format(scheduleId))
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


# Load the file into memory and return it.
def readFile(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo

if __name__ == '__main__':
    scheduler = Scheduler()

    from datetime import datetime, timedelta
    import time as t
    time = datetime.now() + timedelta(seconds=10)   

    scheduler.addJob({ "station": "hat2018.twrmon.net", "port": 8075, "freq": 800, "mode": "am", "time": time, "schedule_id": 31, "duration": 10})

    t.sleep(15)
    scheduler.stop()