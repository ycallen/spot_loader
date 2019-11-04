import json
import os
from collections import defaultdict
from urllib.parse import urlparse
import numpy as np
import rdflib
import copy
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from rdflib import Graph
import pandas as pd

#This class inserts rdf into elastic search
class Inserter:
  def __init__(self, logger):
      self.logger = logger
      self.es = Elasticsearch(timeout=60, http_compress=True)
      self.index_settings = {
          "settings": {
              "number_of_shards": 1,
              "number_of_replicas": 0,
              "refresh_interval" : "60s",
          },
          "mappings": {
              "properties": {
                  "subject": {
                      "type": "text"
                  },
                  "predicate": {
                      "type": "text",
                  },
                  "object": {
                      "type": "text",
                  }
              }
          }
      }

  def add_action(self,subject, predicate, object, index_name):
      #if pd.isnull(object) == True:
      #    self.logger.info("nan  subject = %s predicate = %s object %s",subject,predicate,object)
      #    object = "NA"
      #if len(subject) > 32766 or len(predicate) > 32766 or len(object) > 32766:
      #    return  None
      article = {}
      article['subject'] = subject
      article['predicate'] = predicate
      article['object'] = object

      action = {
          "_index": index_name,
          '_op_type': 'index',
          "_source": article
      }

      return action

  #deletes the index and recreates it using the data in the filename
  def insert(self, file_name, index_name):

    total = 0
    actions = []
    not_inserted = 0
    chunk_size = 5000

    self.es.indices.delete(index=index_name, ignore=[400, 404])
    self.logger.info("deleted es index " + index_name)
    self.es.indices.create(index=index_name, body=self.index_settings)
    self.logger.info("created es index " + index_name)
    #self.logger.info('before chunk')
    for chunk in pd.read_table(file_name, sep='\t', header=None, na_filter = False,chunksize=chunk_size, low_memory=False, names=['fact_id', 'subject', 'predicate', 'object', 'number']):
        #self.logger.info('next chunk')
        if chunk.shape[1] != 5:
            raise Exception(file_name + ' does not contain 5 columns')
        actions = np.vectorize(self.add_action)(chunk['subject'], chunk['predicate'], chunk['object'], index_name)

        #self.logger.info('before bulk')
        for success, info in helpers.parallel_bulk(client=self.es, actions=actions , thread_count=5):
            if not success:
                print("Insert failed: ", info)
        #self.logger.info('after bulk')
        #del actions[0:len(actions)]
        total = total + chunk_size
        if total % 1000000 == 0:
            self.logger.info("sent a total of " + str(total) + " messages to es")
        #insert the last rows
    self.logger.info("total inserted : " + str(total) + " total not inserted : " + str(not_inserted))
#main
#if __name__ == '__main__':
