import datetime
import os
import sys
import time

import mysql
from mysql.connector import Error

from Kiwi.scheduler import Scheduler
from scheduler_creator import loadSchedules

'''
Run me to start.

Edit the parameters.py file for things like database connection parameters.
'''

def main(argv):
    reloadSchedulesFromDatabase()

    return 0

def reloadSchedulesFromDatabase():
    # Load the schedules from the database
    schedules = loadSchedules()

    scheduler = Scheduler()

    for parameters in schedules:

        # Hack the time for the next scheduled instance to run in 1 second from now.
        #now = datetime.datetime.now()
        #parameters['time'] = now + datetime.timedelta(seconds=1)

        scheduler.addJob(parameters)

    print("Waiting for the scheduled recordings to be run...")
    while True:
        time.sleep(1)


if __name__ == '__main__':
    # Pass any command line args to the main function and make the process exit with the return code returned from main()
    sys.exit(main(sys.argv))