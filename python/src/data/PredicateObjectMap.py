
class AbstractPredicateObjectMap:
    """
    A class that is the parent class of all predicate map details (rr:predicateObjectMap)
    """
    def __init__(self, predicate, object_map):
        self.object_map = object_map
        self.predicate = predicate

    def get_predicate(self):
        return str(self.predicate)

    def get_object_map(self):
        return str(self.object_map)

    def get_tuple(self):
        return self.predicate, self.object_map


class ColumnPredicateObjectMap(AbstractPredicateObjectMap):
    """
    This class defines a representation of a rr:predicateObjectMap that uses the rr:column predicate to define
    the objectMap details
    """
    def __init__(self, predicate, object_map):
        AbstractPredicateObjectMap.__init__(self, predicate, object_map)
        self.type = "ColumnObjectMap"

    def getType(self):
        return self.type


class TemplatePredicateObjectMap(AbstractPredicateObjectMap):
    """
        This class defines a representation of a rr:predicateObjectMap that uses the rr:template predicate to define
        the objectMap details
    """
    def __init__(self, predicate, object_map):
        AbstractPredicateObjectMap.__init__(self, predicate, object_map)
        self.type = "TemplateObjectMap"

    def getType(self):
        return self.type