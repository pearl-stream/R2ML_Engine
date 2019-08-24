import rdflib


graph = rdflib.Graph()
graph.load("r2rml.n3", format="n3")

prefix = "PREFIX rr: <http://www.w3.org/ns/r2rml#> "


tripleMapQuery = prefix + """
SELECT ?tableName ?sqlQuery ?subjectTemplate ?subjectConstant ?class ?predicate ?objectConstant ?objectTemplate ?objectColumn
WHERE
{?tripleMap rr:logicalTable ?logicalTableBlank.
{?logicalTableBlank rr:tableName ?tableName} 
UNION 
{?logicalTableBlank rr:sqlQuery ?sqlQuery}
?tripleMap rr:subjectMap ?subjectMapBlank
{?subjectMapBlank rr:template ?subjectTemplate}
UNION 
{?subjectMapBlank rr:constant ?subjectConstant}
OPTIONAL
{?subjectMapBlank rr:class ?class}
OPTIONAL
{?tripleMap rr:predicateObjectMap ?predicateObjectMapBlank.
?predicateObjectMapBlank rr:predicate ?predicate.
?predicateObjectMapBlank rr:objectMap ?objectMapBlank.
{?objectMapBlank rr:constant ?objectConstant}
UNION
{?objectMapBlank rr:template ?objectTemplate}
UNION
{?objectMapBlank rr:column ?objectColumn}
}
}
"""


result = graph.query(tripleMapQuery)
for row in result:
  print(row)
