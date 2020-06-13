
class AbstractPredicateObjectMap:

    def __init__(self, predicate, object_map):
        self.object_map = object_map
        self.predicate = predicate

    def get_predicate(self):
        return str(self.predicate)

    def get_object_map(self):
        return str(self.object_map)

    def get_tuple(self):
        return self.object_map, self.predicate

class ColumnPredicateObjectMap(AbstractPredicateObjectMap):

    def __init__(self, id, predicate, object_map):
        AbstractPredicateObjectMap.__init__(self, predicate, object_map)
        self.type = "ColumnObjectMap"

    def getType(self):
        return self.type


class TemplatePredicateObjectMap(AbstractPredicateObjectMap):

    def __init__(self, id, predicate, object_map):
        AbstractPredicateObjectMap.__init__(self, predicate, object_map)
        self.type = "TemplateObjectMap"

    def getType(self):
        return self.type