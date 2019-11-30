import tripleFromQuery as triples
import mysql_con as mysql
import re

class TransformSubjectMap():
  def __init__(self):
      self.m = mysql.MySQL("192.168.99.100", 3306, "root", "", "mysql-development")

  def transformSubjectMapTriple(self, subjectTriple):
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

  def transform(self, abstractTriple):
      if isinstance(abstractTriple, triples.ColumnTriple) or isinstance(abstractTriple, triples.TemplateTriple):
          self.transformSubjectMapTriple(abstractTriple)

print("Starting the execution of SubjectMap translations")
ts = TransformSubjectMap()
triples.createAllTriples()
for x in triples.allTriples:
    ts.transform(x)


#    print("Tuple:")
#    print(x.getSql())
#    print(x.getSubject())
#    print(x.getPredicate())
#    print(x.getObject())
#    print("---")
#    print("")
#    ts.transform(x)
