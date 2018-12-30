import os
import subprocess
import re


def record(station, port, freq, mode, time, schedule_id):
    """Record takes a string station (web address), an integer port, an integer freq, a string mode, and a integer time
     in seconds, and returns the RSSI data of the recording being saved, as a list of floats.
    The recording is saved in the directory that the script is run on under the default file name,
     which has the format (YYYYMMDDTHHMMSSZ_station_mode).wav"""

    dirname = os.path.dirname(os.path.realpath(__file__))
    outputDir = "{}/audioFiles".format(dirname)
    filenamePrefix = "schedule_{}".format(str(schedule_id))
    totalFilename = '{}/{}_{}.wav'.format(outputDir, filenamePrefix, station)

    command = ["python", "{}/kiwirecorder.py".format(dirname), "-k", str(30), "--station", str(station) ,"-s", str(station), "-p", str(port), "-f", str(freq), "-m", mode,
               "--tlimit="+str(time), "-d", outputDir, "--fn", filenamePrefix]
    data = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = data.communicate()[0]
    data.wait()
    d =  re.sub("\r  ", ",", re.sub("Block: [0-9a-f]*, RSSI:", "", output)).split(",")[1:-1]
    return [float(i) for i in d], totalFilename, schedule_id
