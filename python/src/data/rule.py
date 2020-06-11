'''This module describes defines a r2ml rule in an object oriented way '''

from .SubjectMap import AbstractSubjectMap
from .SubjectMap import ColumnSubjectMap
from .SubjectMap import TemplateSubjectMap


class Rule:
    def __init__(self):
        self.subject_map = None
        self.predicate_object_maps = []

    def create_subject_map(self, subject_map):
        if not isinstance(subject_map, AbstractSubjectMap):
            pass
        self.subject_map = subject_map

    def create_subject_map(self, id, type, sql, subject, predicate, object):
        if type == "rr:template":
            self.subject_map = TemplateSubjectMap(id, sql, subject, predicate, object)
        elif type == "rr:column":
            self.subject_map = ColumnSubjectMap(id, sql, subject, predicate, object)

    def create_subject_map_with_template(self, id, sql, subject, predicate, object):
        pass

    def add_predicate_object_map(self):
        pass