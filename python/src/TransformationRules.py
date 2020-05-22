import ruleParsing as triples
import mysql_con as mysql
import re

class TransformEngine():
  def __init__(self):
      print("ConnectingToDb")
      self.m = mysql.MySQL("127.0.0.1", 3306, "root", "", "mysql-development")

  def transformPredicateObjectMapTriple(self, subject, columnTriple, row, nameToIndex):
      object = columnTriple.getObject()
      column = object
      template = ""
      if isinstance(columnTriple, triples.TemplatePredicateObjectTriple):
          regex = "(.*){(.*)}(.*)"
          result = re.search(regex, object)
          if result:
              template = result.group(1)
              column = result.group(2)
          else:
              print("Template is wrong definied: " + object)
      if column not in nameToIndex:
          print("Error: The following column is not part of the table" + column)
          return
      index = nameToIndex[column]
      object = template + str(row[index])
      print(subject + " "+ columnTriple.getPredicate() + " " + object)

  def transformSubjectMapTriple(self, subjectTriple):
      print("Working on transformation for Mapping rule: " + subjectTriple.getId())
      self.m.execQuery(subjectTriple.sql)
      rows = self.m.getRows()
      nameToIndex = self.m.getColumnNameToKey()
      column = ""
      template = ""

      if isinstance(subjectTriple, triples.TemplateTriple):
          regex = "(.*){(.*)}(.*)"
          result = re.search(regex, subjectTriple.getSubject())
          if result:
              template = result.group(1)
              column = result.group(2)
      elif isinstance(subjectTriple, triples.ColumnTriple):
          column = str(subjectTriple.getSubject())
          template = ""
      #https://stackoverflow.com/questions/5010042/mysql-get-column-name-or-alias-from-query
      #To Discuss: Would it maybe better if we give the SQL statements an order
      for row in rows:
          index = nameToIndex[column]
          subject = template + str(row[index])
          predicate = subjectTriple.getPredicate()
          object = subjectTriple.getObject()
          print(subject + " " + predicate + " " + str(object))
          trippleId = subjectTriple.getId()
          if trippleId in triples.mappingRuleToColumnMap:
              matchingColumnMap  = triples.mappingRuleToColumnMap[trippleId]
              self.transformPredicateObjectMapTriple(subject, matchingColumnMap , row, nameToIndex)

  def transform(self, abstractTriple):
      if isinstance(abstractTriple, triples.ColumnTriple) or isinstance(abstractTriple, triples.TemplateTriple):
          self.transformSubjectMapTriple(abstractTriple)

print("Starting the execution of SubjectMap translations")
ts = TransformEngine()
print("Connection Done")
triples.setup()
print("Finished translating Sparql rules into classes")
for x in triples.allSubjectTriples:
    ts.transform(x)
