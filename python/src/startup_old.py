'''This module tests if the implemented SPARQL querie are working properly'''

import queries as q
import rdflib


#Load the example R2RML file
graph = rdflib.Graph()
graph.load("r2rml.n3", format="n3")


def selectQuery(query):
  '''Decide how queries need to be handled based on the query name'''
  if query.name == 'typeTableTemplate':
    result = graph.query(query.value) #Execute sparql query
    for row in result:
      print(row['tableName'])
      print(row['subjectTemplate'])
      print(row['class'])
  if query.name == 'typeTableColumn':
    result = graph.query(query.value)
    for row in result:
      print(row['tableName'])
      print(row['subjectColumn'])
      print(row['class'])
  if query.name == 'typeQueryTemplate':
    result = graph.query(query.value)
    for row in result:
      print(row['sqlQuery'])
      print(row['subjectTemplate'])
      print(row['class'])
  if query.name == 'typeQueryColumn':
    result = graph.query(query.value)
    for row in result:
      print(row['sqlQuery'])
      print(row['subjectColumn'])
      print(row['class'])
  if query.name == 'typeConstant':
    result = graph.query(query.value)
    for row in result:
      print(row['subjectConstant'])
      print(row['class'])
# [...]


for query in q.R2RMLqueries: #iterate over queries
  selectQuery(query)


