from enum import Enum

#Prefix of the r2rml namespace
prefix = "PREFIX rr: <http://www.w3.org/ns/r2rml#>"


class R2RMLqueries(Enum):
  '''Holds queries used to parse R2RML'''

  ###############################################################
  ###############################################################
  #### QUERIES FOR TRIPLES OF FORM subject rdf:type class   #####
  ###############################################################
  ###############################################################

  typeTableTemplate  = prefix + """
                       SELECT ?triplesMap ?tableName ?subjectTemplate ?class WHERE {
                       ?triplesMap rr:logicalTable ?logicalTableBlank.
                       ?logicalTableBlank rr:tableName ?tableName.
                       ?triplesMap rr:subjectMap ?subjectMapBlank.
                       ?subjectMapBlank rr:template ?subjectTemplate.
                       ?subjectMapBlank rr:class ?class.} """

  typeTableColumn =  prefix + """
                     SELECT ?triplesMap ?tableName ?subjectColumn ?class WHERE {
                     ?triplesMap rr:logicalTable ?logicalTableBlank.
                     ?logicalTableBlank rr:tableName ?tableName.
                     ?triplesMap rr:subjectMap ?subjectMapBlank.
                     ?subjectMapBlank rr:column ?subjectColumn.
                     ?subjectMapBlank rr:class ?class.} """

  typeQueryTemplate =  prefix + """
                       SELECT ?triplesMap ?sqlQuery ?subjectTemplate ?class WHERE {
                       ?triplesMap rr:logicalTable ?logicalTableBlank.
                       ?logicalTableBlank rr:sqlQuery ?sqlQuery.
                       ?triplesMap rr:subjectMap ?subjectMapBlank.
                       ?subjectMapBlank rr:template ?subjectTemplate.
                       ?subjectMapBlank rr:class ?class.}"""

  typeQueryColumn =  prefix + """
                     SELECT ?triplesMap ?sqlQuery ?subjectColumn ?class WHERE {
                     ?triplesMap rr:logicalTable ?logicalTableBlank.
                     ?logicalTableBlank rr:sqlQuery ?sqlQuery.
                     ?triplesMap rr:subjectMap ?subjectMapBlank.
                     ?subjectMapBlank rr:column ?subjectColumn.
                     ?subjectMapBlank rr:class ?class.}"""

  typeConstant =  prefix + """
                  SELECT ?triplesMap ?subjectConstant ?class WHERE {
                  ?triplesMap rr:logicalTable _:logicalTableBlank.
                  ?triplesMap rr:subjectMap ?subjectMapBlank.
                  ?subjectMapBlank rr:constant ?subjectConstant.
                  ?subjectMapBlank rr:class ?class.}"""

  typePredicateObjectTemplate = prefix + """
                     SELECT ?triplesMap ?subjectTemplate ?predciate ?columnName WHERE {
                     ?triplesMap rr:subjectMap ?subjectMapBlank.
                     ?subjectMapBlank rr:template ?subjectTemplate.
                     ?triplesMap rr:predicateObjectMap ?logicalObjectMap.
                     ?logicalObjectMap rr:predicate ?predciate.
                     ?logicalObjectMap rr:objectMap ?objectMapBlank.
                     ?objectMapBlank rr:column  ?columnName.}"""

  typePredicateObjectColumn = prefix + """
                     SELECT ?triplesMap ?subjectTemplate ?predciate ?subjectColumn WHERE {
                     ?triplesMap rr:subjectMap ?subjectMapBlank.
                     ?subjectMapBlank rr:column ?subjectColumn.
                     ?triplesMap rr:predicateObjectMap ?logicalObjectMap.
                     ?logicalObjectMap rr:predicate ?predciate.
                     ?logicalObjectMap rr:objectMap ?objectMapBlank.
                     ?objectMapBlank rr:column  ?columnName.}"""



  ###############################################################
  ###############################################################
  ##########   QUERIES FOR TRIPLES OF OTHER FORM   ##############
  ###############################################################
  ###############################################################

#The following queries have to be implemented and tested

#  query1 =  prefix
#  query1 += "SELECT ?tableName ?subjectTemplate ?predicate ?ObjectTemplate WHERE {"
#  query1 += "  ?triplesMap rr:logicalTable ?logicalTableBlank. \n"
#  query1 += "  ?logicalTableBlank rr:tableName ?tableName. \n"
#  query1 += "  ?triplesMap rr:subjectMap ?subjectMapBlank. \n"
#  query1 += "  ?subjectMapBlank rr:template ?subjectTemplate. \n"
#  query1 += "  ?triplesMap rr:predicateObjectMap ?predicateObjectBlank. \n"
#  query1 += "  ?predicateObjectBlank rr:predicate ?predicate. \n"
#  query1 += "  ?predicateObjectBlank rr:ObjectMap ?ObjectBlank. \n"
#  query1 += "  ?ObjectBlank rr:template ?ObjectTemplate. \n}"
