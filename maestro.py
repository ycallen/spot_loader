import glob
import os

from scipy.spatial.ckdtree import ordered_pairs

from es.inserter import Inserter
from logger.logger import Logger
import os, operator, sys

if __name__ == '__main__':
    #in_files = glob.glob("E:\\yago\\in_progress\\*")



    dirpath = os.path.abspath("E:\\yago\\in_progress\\")
    # make a generator for all file paths within dirpath
    all_files = (os.path.join(basedir, filename) for basedir, dirs, files in os.walk(dirpath) for filename in files)
    sorted_files = sorted(all_files, key=os.path.getsize, reverse=True)

    for file in sorted_files:
        head, tail = os.path.split(file)
        pre, ext = os.path.splitext(tail)
        logger = Logger("E:\\log\\" + tail + ".log", pre)

        es_inserter = Inserter(logger.logger)
        es_inserter.insert(file, pre.lower())