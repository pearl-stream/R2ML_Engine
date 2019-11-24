import rdflib

''' This module holds SPARQL queries needed to parse an R2RML file. '''



#Prefix of the r2rml namespace
prefix = "PREFIX rr: <http://www.w3.org/ns/r2rml#> \n"

###############################################################
###############################################################
#### QUERIES FOR TRIPLES OF FORM subject rdf:type class   #####
###############################################################
###############################################################

typeTableTemplate  = prefix
typeTableTemplate += "SELECT ?tableName ?subjectTemplate ?class WHERE { \n"
typeTableTemplate += "  ?triplesMap rr:logicalTable ?logicalTableBlank. \n"
typeTableTemplate += "  ?logicalTableBlank rr:tableName ?tableName.  \n"
typeTableTemplate += "  ?triplesMap rr:subjectMap ?subjectMapBlank. \n"
typeTableTemplate += "  ?subjectMapBlank rr:template ?subjectTemplate. \n"
typeTableTemplate += "  ?subjectMapBlank rr:class ?class. \n}"

##Not tested
typeTableColumn =  prefix
typeTableColumn += "SELECT ?tableName ?subjectColumn ?class WHERE { \n"
typeTableColumn += "  ?triplesMap rr:logicalTable ?logicalTableBlank. \n"
typeTableColumn += "  ?logicalTableBlank rr:tableName ?tableName.  \n"
typeTableColumn += "  ?triplesMap rr:subjectMap ?subjectMapBlank. \n"
typeTableColumn += "  ?subjectMapBlank rr:column ?subjectColumn. \n"
typeTableColumn += "  ?subjectMapBlank rr:class ?class. \n}"

typeQueryTemplate =  prefix
typeQueryTemplate += "SELECT ?sqlQuery ?subjectTemplate ?class WHERE { \n"
typeQueryTemplate += "  ?triplesMap rr:logicalTable ?logicalTableBlank. \n"
typeQueryTemplate += "  ?logicalTableBlank rr:sqlQuery ?sqlQuery.  \n"
typeQueryTemplate += "  ?triplesMap rr:subjectMap ?subjectMapBlank. \n"
typeQueryTemplate += "  ?subjectMapBlank rr:template ?subjectTemplate. \n"
typeQueryTemplate += "  ?subjectMapBlank rr:class ?class. \n}"

##Not tested
typeQueryColumn =  prefix
typeQueryColumn += "SELECT ?sqlQuery ?subjectColumn ?class WHERE { \n"
typeQueryColumn += "  ?triplesMap rr:logicalTable ?logicalTableBlank. \n"
typeQueryColumn += "  ?logicalTableBlank rr:sqlQuery ?sqlQuery.  \n"
typeQueryColumn += "  ?triplesMap rr:subjectMap ?subjectMapBlank. \n"
typeQueryColumn += "  ?subjectMapBlank rr:column ?subjectColumn. \n"
typeQueryColumn += "  ?subjectMapBlank rr:class ?class. \n}"

typeConstant =  prefix
typeConstant += "SELECT ?subjectConstant ?class WHERE { \n"
typeConstant += "  ?triplesMap rr:logicalTable _:logicalTableBlank. \n"
typeConstant += "  ?triplesMap rr:subjectMap ?subjectMapBlank. \n"
typeConstant += "  ?subjectMapBlank rr:constant ?subjectConstant. \n"
typeConstant += "  ?subjectMapBlank rr:class ?class. \n}"


###############################################################
###############################################################
##########   QUERIES FOR TRIPLES OF OTHER FORM   ##############
###############################################################
###############################################################

query1 =  prefix
query1 += "SELECT ?tableName ?subjectTemplate ?predicate ?ObjectTemplate WHERE {"
query1 += "  ?triplesMap rr:logicalTable ?logicalTableBlank. \n"
query1 += "  ?logicalTableBlank rr:tableName ?tableName. \n"
query1 += "  ?triplesMap rr:subjectMap ?subjectMapBlank. \n"
query1 += "  ?subjectMapBlank rr:template ?subjectTemplate. \n"
query1 += "  ?triplesMap rr:predicateObjectMap ?predicateObjectBlank. \n"
query1 += "  ?predicateObjectBlank rr:predicate ?predicate. \n"
query1 += "  ?predicateObjectBlank rr:ObjectMap ?ObjectBlank. \n"
query1 += "  ?ObjectBlank rr:template ?ObjectTemplate. \n}"


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

allTabelStatementsDict = {'typeTableTemplate' : typeTableTemplate, 'typeQueryTemplate' : typeQueryTemplate}
allTriples = []
for key in allTabelStatementsDict:
    sparqlQuery = allTabelStatementsDict[key]
    rows = exeucteSparqlQuery(sparqlQuery)
    result = executeFuctionForQueryResult(key, rows)
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
