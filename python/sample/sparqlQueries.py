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
###############################################################

allTabelStatementsDict = {'tableTypeTemplate' : typeTableTemplate, 'typeTableColumn' : typeTableColumn}
allTriples = []
for key in allTableStatementsDict:
  sparqlQuery = allTableStatementsDict[key]
  rows = exeucteSparqlQuery(sparqlQuery)
  result = returnRightFunc(key, rows)
  allTriples.append(result)
sortBySQLTale(allTriples)
for x in sortTriplesRight:
  crateTriple(x)


def returnRightFunct(queryType, rows):
  if queryType == 'tableTypeTemplate':
    return handleQuery1(rows)
  elif queryType == 'typeTableColumn':
    return handleQuery2(query)
  #[...]


def handleQuery2(rows):
  triple_list = []
  for (sqlTable, template, class_n) in sparqlResult:
	t_n = AbstractTriple(sqlTable, ROW,  "rdf:type", class_n)
       tripe_list.append(t_n)
  return triple_list

class AbstractTriple:
	def __init__(self, sql,  subject, predicate, object):
		self.sql = sql
		self.subject = subject
		self.predicate = predicate
		self.object = object




