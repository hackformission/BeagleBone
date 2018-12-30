import threading

class RecordingThread(threading.Thread):
   def __init__(self, parameters):
      threading.Thread.__init__(self)
      self.parameters = parameters

   def run(self):
      print "Starting {} with parameters {}".format(self.name, self.parameters)

      # TODO: create the scheduler object for this recording instance.

      print "Exiting " + self.name