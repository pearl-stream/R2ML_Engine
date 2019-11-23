'''This module parses a r2rml mapping and returns the values needed to generate RDF triples from relational data'''
import rdflib

def prettyPrintResult(result):
  '''Kind of pretty prints variable bindings'''
  for row in result:
    print("tableName:        " + str(row["tableName"]))
    print("sqlQuery:         " + str(row["sqlQuery"]))
    print("subjectTemplate:  " + str(row["subjectTemplate"]))
    print("subjectConstant:  " + str(row["subjectConstant"]))
    print("class:            " + str(row["class"]))
    print("predicate:        " + str(row["predicate"]))
    print("objctConstant:    " + str(row["objectConstant"]))
    print("objectTemplate:   " + str(row["objectTemplate"]))
    print("objectColumn:     " + str(row["objectColumn"]))
    print("______________________________________\n\n")


#Create rdf graph and load file to graph
graph = rdflib.Graph()
graph.load("r2rml.n3", format="n3")

#Define prefix for query
prefix = "PREFIX rr: <http://www.w3.org/ns/r2rml#> "


#Query looks a bit ugly feel free to format.
tripleMapQuery = prefix + """
SELECT ?tableName ?sqlQuery ?subjectTemplate ?subjectConstant ?class ?predicate ?objectConstant ?objectTemplate ?objectColumn #Projection of variables
WHERE{
  ?tripleMap rr:logicalTable ?logicalTableBlank.  #match triple map by rr:logicalTable
  {?logicalTableBlank rr:tableName ?tableName}     #get table Name of source relation
  UNION                                            #use UNION in because only one of ?tableName and ?sqlQuery can be matche
  {?logicalTableBlank rr:sqlQuery ?sqlQuery}       #match sql Query as source relation
  ?tripleMap rr:subjectMap ?subjectMapBlank        #match blank node of subject map
  {?subjectMapBlank rr:template ?subjectTemplate}
  UNION                                            #match subjectTemplate and subjectConstant and create union because only one can match
  {?subjectMapBlank rr:constant ?subjectConstant}
  OPTIONAL                                         #?class is optional because a subjectmap does not require a class
    {?subjectMapBlank rr:class ?class}
  OPTIONAL                                         #matching ?predicateObjectMapBlank is OPTIONAL because predicateObjectMap is not required
    {?tripleMap rr:predicateObjectMap ?predicateObjectMapBlank.
     ?predicateObjectMapBlank rr:predicate ?predicate.
     ?predicateObjectMapBlank rr:objectMap ?objectMapBlank.
     {?objectMapBlank rr:constant ?objectConstant}
     UNION                                            #create UNION of constant template and column because only one can match
     {?objectMapBlank rr:template ?objectTemplate}
     UNION
     {?objectMapBlank rr:column ?objectColumn}
    }
}
"""

result = graph.query(tripleMapQuery) #Execute sparql query
prettyPrintResult(result)
print(type(result))
