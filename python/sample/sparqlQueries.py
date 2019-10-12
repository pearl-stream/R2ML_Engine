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
