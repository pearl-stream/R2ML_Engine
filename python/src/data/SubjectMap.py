'''This module describes the classes that store the subjectMap details '''


class AbstractSubjectMap:
    """A class that is the parent class of all subject map details

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


class ColumnSubjectMap(AbstractSubjectMap):
    def __init__(self, subject_placeholder, class_value):
        AbstractSubjectMap.__init__(self, subject_placeholder, class_value)
        self.type = "Column"

    def __str__(self):
        return AbstractSubjectMap.__str__(self)

    def __repr__(self):
        return AbstractSubjectMap.__repr__(self)


class TemplateSubjectMap(AbstractSubjectMap):
    def __init__(self, subject_placeholder, class_value):
        AbstractSubjectMap.__init__(self, subject_placeholder, class_value)
        self.type = "Template"

    def __str__(self):
        return AbstractSubjectMap.__str__(self)

    def __repr__(self):
        return AbstractSubjectMap.__repr__(self)