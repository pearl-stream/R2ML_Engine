'''This module describes the classes that store the subjectMap details '''


class AbstractSubjectMap:
    """A class that is the parent class of all subject map details

    """
    def __init__(self, id, sql,  subject, predicate, object):
        self.sql = sql
        self.subject = subject
        self.predicate = predicate
        self.object = object
        self.id = id

    def __str__(self):
        return  ": " + self.sql + " " + self.subject + " " + self.predicate + " " + self.object

    def __repr__(self):
        return ": " + self.sql + " " + self.subject + " " + self.predicate + " " + self.object

    def get_object(self):
        return self.object

    def get_predicate(self):
        return self.predicate

    def get_subject(self):
        return str(self.subject)

    def get_sql(self):
        return self.sql

    def get_id(self):
        return str(self.id)


class ColumnSubjectMap(AbstractSubjectMap):
    def __init__(self, id, sql,  subject, predicate, object):
        AbstractSubjectMap.__init__(self, id, sql, subject, predicate, object)
        self.type = "Column"

    def __str__(self):
        return AbstractSubjectMap.__str__(self)

    def __repr__(self):
        return AbstractSubjectMap.__repr__(self)


class TemplateSubjectMap(AbstractSubjectMap):
    def __init__(self, id, sql,  subject, predicate, object):
        AbstractSubjectMapTriple.__init__(self, id, sql, subject, predicate, object)
        self.type = "Template"

    def __str__(self):
        return AbstractSubjectMap.__str__(self)

    def __repr__(self):
        return AbstractSubjectMap.__repr__(self)
