import rdflib
import queries as q


###############################################################
################# Freddy Test 23.11.19 ########################
# -- Sorting by SQL is missing:
#       We want to sort by SQL so that all triples related to the same SQL Statement will be executed sequentialy
#       This way only the result of the last sql statement hast to be cached, by our code
#       How to sort the statements can be a task. For not it would be enough by name/alpha-numeric
#       Queries that are semantic similar, or by involved table, could be a way to go in the future
###############################################################
class AbstractTriple:
	def __init__(self, sql,  subject, predicate, object):
		self.sql = sql
		self.subject = subject
		self.predicate = predicate
		self.object = object
	def __str__(self):
		return  ": " + self.sql + " " + self.subject + " " + self.predicate + " " + self.object
	def __repr__(self):
		return ": " + self.sql + " " + self.subject + " " + self.predicate + " " + self.object
	def getObject(self):
		return self.object
	def getPredicate(self):
		return self.predicate
	def getSubject(self):
		return self.subject
	def getSql(self):
		return self.sql


class ColumnTriple(AbstractTriple):
	def __init__(self, sql,  subject, predicate, object):
		AbstractTriple.__init__(self, sql, subject, predicate, object)
		self.type = "Column"
	def __str__(self):
		return AbstractTriple.__str__(self)
	def __repr__(self):
		return AbstractTriple.__repr__(self)

class TemplateTriple(AbstractTriple):
	def __init__(self, sql,  subject, predicate, object):
		AbstractTriple.__init__(self, sql, subject, predicate, object)
		self.type = "Template"
	def __str__(self):
		return AbstractTriple.__str__(self)
	def __repr__(self):
		return AbstractTriple.__repr__(self)

def exeucteSparqlQuery(sparqlResult):
    #Create rdf graph and load file to graph
    graph = rdflib.Graph()
    graph.load("r2rml.n3", format="n3")
    result = graph.query(sparqlQuery) #Execute sparql query
    return result
#?tableName ?subjectTemplate ?class
def handleTypeTableTemplate(sparqlResult):
    triple_list = []
    for (tableName, template, class_n) in sparqlResult:
        sqlTable = "select * from " + tableName
        t_n = TemplateTriple(sqlTable, template,  "rdf:type", class_n)
        triple_list.append(t_n)
    return triple_list

#?tableName ?subjectColumn ?class
def handleTypeTableColumn(sparqlResult):
    triple_list = []
    for (tableName, subjectColumn, class_n) in sparqlResult:
        sqlTable = "select * from " + tableName
        t_n = ColumnTriple(sqlTable, subjectColumn,  "rdf:type", class_n)
        triple_list.append(t_n)
    return triple_list

def handleTypeQueryTemplate(sparqlResult):
    triple_list = []
    for (sqlquery, template, class_n) in sparqlResult:
        t_n = TemplateTriple(sqlquery, template,  "rdf:type", class_n)
        triple_list.append(t_n)
    return triple_list

# ?sqlQuery ?subjectColumn ?class
def handleTypeQueryColumn(sparqlResult):
    triple_list = []
    for (sqlQuery, subjectColumn, class_n) in sparqlResult:
        t_n = ColumnTriple(sqlQuery, subjectColumn,  "rdf:type", class_n)
        triple_list.append(t_n)
    return triple_list

def executeFuctionForQueryResult(queryType, rows):
    if queryType == 'typeTableTemplate':
        return handleTypeTableTemplate(rows)
    elif queryType == 'typeTableColumn':
        return handleTypeTableColumn(rows)
    elif queryType == 'typeQueryTemplate':
        return handleTypeQueryTemplate(rows)
    elif queryType == 'typeQueryColumn':
        return handleTypeQueryColumn(rows)

allTabelStatementsDict = {query.name: query.value for query in q.R2RMLqueries}
#print(allTabelStatementsDict)
#allTabelStatementsDict = {'typeTableTemplate' : q.R2RMLqueries.typeTableTemplate.value, 'typeQueryTemplate' : q.R2RMLqueries.typeQueryTemplate.value}
allTriples = []
for key in allTabelStatementsDict:
    sparqlQuery = allTabelStatementsDict[key]
    rows = exeucteSparqlQuery(sparqlQuery)
    result = executeFuctionForQueryResult(key, rows)
    if result:
    	allTriples = allTriples + result

print("Lenght of result: " + str(len(allTriples)))
#sortBySQLTale(allTriples)
for x in allTriples:
    #print(x) --> Result looks strange. Has to be fixed
    print("Tuple:")
    print(x.getSql())
    print(x.getSubject())
    print(x.getPredicate())
    print(x.getObject())


    print("---")
    print("")
    #createTriple(x)


  #[...]
