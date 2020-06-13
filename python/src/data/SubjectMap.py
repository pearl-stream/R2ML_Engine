'''This module describes the classes that store the subjectMap details '''


class AbstractSubjectMap:
    """
    A class that is the parent class of all subject map details
    """
    def __init__(self, subject_placeholder, class_value):
        self.subject_placeholder = subject_placeholder
        self.predicate = "rdf:type"
        self.class_value = class_value

    def __str__(self):
        return  ": " + self.subject_placeholder + " " + self.predicate + " " + self.class_value

    def __repr__(self):
        return ": " + self.subject_placeholder + " " + self.predicate + " " + self.class_value

    def get_object(self):
        return self.class_value

    def get_predicate(self):
        return self.predicate

    def get_subject(self):
        return str(self.subject_placeholder)

    def get_triple(self):
        return self.subject_placeholder, self.predicate, self.class_value


class ColumnSubjectMap(AbstractSubjectMap):
    """
    This class defines a representation of a subjectMap that uses the rr:column predicate to define the subject of the
    created rdf triple by the r2ml rule
    """
    def __init__(self, subject_placeholder, class_value):
        AbstractSubjectMap.__init__(self, subject_placeholder, class_value)
        self.type = "Column"

    def __str__(self):
        return AbstractSubjectMap.__str__(self)

    def __repr__(self):
        return AbstractSubjectMap.__repr__(self)


class TemplateSubjectMap(AbstractSubjectMap):
    """
    This class defines a representation of a subjectMap that uses the rr:template predicate to define the subject of the
    created rdf triple by the r2ml rule
    """
    def __init__(self, subject_placeholder, class_value):
        AbstractSubjectMap.__init__(self, subject_placeholder, class_value)
        self.type = "Template"

    def __str__(self):
        return AbstractSubjectMap.__str__(self)

    def __repr__(self):
        return AbstractSubjectMap.__repr__(self)