import os
import glob
import shutil

#this file converts rdf files from various formats into the nt (triples) format using the rdf2rdf java library.
#put one or more files that should be converted into the input directory.
#the result is all of the input files merged and converted into onre output.nt file in the output directory.
#remark : an nt file can also be put in the input directory and it will also be merged.
class Converter:
    def __init__(self, logger):
        self.logger = logger
    def convert(self,file, output_file, java_path, jar_path):
        self.logger.info("started converting " + file)
        cmd = 'call %s -jar %s %s %s' % (java_path, jar_path, file, '"' + output_file + '"')
        os.system(cmd)
        self.logger.info("ended converting " + file)

#main
if __name__ == '__main__':

    #java_path = "\"jdk1.8.0_211\\bin\\java\""
    java_path = "\"C:\\Program Files\\Java\\jdk1.8.0_211\\bin\\java\""
    jar_path = "rdf2rdf-1.0.2-2.3.1.jar"
    output_path = "E:\\test"
    in_files = glob.glob("E:\\test\\*")
    for file in in_files:
        converter = Converter()
        head, tail = os.path.split(file)
        print("converting " + file)
        pre, ext = os.path.splitext(tail)
        converter.convert(file, output_path + pre + ".nt", java_path, jar_path)

