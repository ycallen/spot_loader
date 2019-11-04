import logging
import os

#This class inserts rdf into elastic search
class Logger:
  def __init__(self, file_name, logger_name):
      if os.path.exists(file_name):
          os.remove(file_name)
      self.logger = logging.getLogger(logger_name)
      self.logger.setLevel(logging.DEBUG)
      # create file handler which logs even debug messages
      fh = logging.FileHandler(file_name)
      fh.setLevel(logging.DEBUG)
      # create console handler with a higher log level
      ch = logging.StreamHandler()
      ch.setLevel(logging.DEBUG)
      # create formatter and add it to the handlers
      formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
      fh.setFormatter(formatter)
      ch.setFormatter(formatter)
      # add the handlers to the logger
      self.logger.addHandler(fh)
      self.logger.addHandler(ch)

  def get_logger(self):
      return logger



