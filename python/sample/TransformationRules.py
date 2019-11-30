import tripleFromQuery as triples
import mysql_con as mysql

class TransformSubjectMap():
  def __init__(self):
      self.m = mysql.MySQL("192.168.99.100", 3306, "root", "", "mysql-development")

  def transformColumnTriple(self, columnTriple):
      self.m.execQuery(columnTriple.sql)
      rows = self.m.getRows()
      nameToIndex = self.m.getColumnNameToKey()
      column = str(columnTriple.getSubject())
      #https://stackoverflow.com/questions/5010042/mysql-get-column-name-or-alias-from-query
      #To Discuss: Would it maybe better if we give the SQL statements an order
      for row in rows:
          index = nameToIndex[column]
          subject = str(row[index])
          predicate = columnTriple.getPredicate()
          object = columnTriple.getObject()
          print(subject + " " + predicate + " " + str(object))

  def transform(self, abstractTriple):
      if isinstance(abstractTriple, triples.ColumnTriple):
          self.transformColumnTriple(abstractTriple)

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
