import tripleFromQuery as triples
import mysql_con as mysql

class TransformSubjectMap():
  def __init__(self):
      self.m = mysql.MySQL("192.168.99.100", 3306, "root", "", "mysql-development")

  def transformColumnTriple(self, columnTriple):
      print(columnTriple.sql)
      self.m.execQuery(columnTriple.sql)
      rows = self.m.getRows()
      for row in rows:
          print(row)

  def transform(self, abstractTriple):
      if isinstance(abstractTriple, triples.ColumnTriple):
          self.transformColumnTriple(abstractTriple)

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
