import subprocess
import re


def record(station, port, freq, mode, time):
    """Record takes a string station (web address), an integer port, an integer freq, the frequency, in kHz,
    a string mode (e.g. am), and a integer time, in seconds for the length of the recording.
    It returns the RSSI data of the recording being saved, as a list of floats.
    The recording is saved in the directory that the script is run on under the default file name,
     which has the format (YYYYMMDDTHHMMSSZ_station_mode).wav"""
    command = ["python", "Kiwi/kiwirecorder.py", "-k", str(30), "-s", str(station), "-p", str(port), "-f", str(freq), "-m", mode,
               "--tlimit="+str(time)]
    data = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = data.communicate()[0]
    d =  re.sub("\r  ", ",", re.sub("Block: [0-9a-f]*, RSSI:", "", output)).split(",")[1:-1]
    return [float(i) for i in d]


data = record("hat2018.twrmon.net", 8075, 800, "am", 10)