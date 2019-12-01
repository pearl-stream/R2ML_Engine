import tripleFromQuery as triples
import mysql_con as mysql
import re

class TransformSubjectMap():
  def __init__(self):
      self.m = mysql.MySQL("192.168.99.100", 3306, "root", "", "mysql-development")

  def transformColumnMapTriple(self, subject, columnTriple, row, nameToIndex):
      object = columnTriple.getObject()
      column = object
      template = ""
      if isinstance(columnTriple, triples.TemplateColumnMapTriple):
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
      print("Working on: " + subjectTriple.getId())
      self.m.execQuery(subjectTriple.sql)
      rows = self.m.getRows()
      nameToIndex = self.m.getColumnNameToKey()
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
          if trippleId in triples.subjectToColumnMap:
              tripleSubject = subjectTriple.getSubject()
              matchingColumnMap  = triples.subjectToColumnMap[trippleId]
              self.transformColumnMapTriple(subject, matchingColumnMap , row, nameToIndex)

  def transform(self, abstractTriple):
      if isinstance(abstractTriple, triples.ColumnTriple) or isinstance(abstractTriple, triples.TemplateTriple):
          self.transformSubjectMapTriple(abstractTriple)

print("Starting the execution of SubjectMap translations")
ts = TransformSubjectMap()
triples.createAllSubjectTriples()
triples.createAllColumnTriples()
for x in triples.allSubjectTriples:
    ts.transform(x)


#    print("Tuple:")
#    print(x.getSql())
#    print(x.getSubject())
#    print(x.getPredicate())
#    print(x.getObject())
#    print("---")
#    print("")
#    ts.transform(x)
