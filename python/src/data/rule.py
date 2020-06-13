'''This module describes defines a r2ml rule in an object oriented way '''

from .SubjectMap import AbstractSubjectMap
from .SubjectMap import ColumnSubjectMap
from .SubjectMap import TemplateSubjectMap


class Rule:
    def __init__(self, rule_id):
        self.subject_map = None
        self.predicate_object_maps = []
        self.rule_id = rule_id
        self.sql_statement = None

    def create_subject_map(self, subject_map):
        if not isinstance(subject_map, AbstractSubjectMap):
            pass
        self.subject_map = subject_map

    def create_subject_map(self, rr_type, subject_placeholder, class_value):
        if rr_type == "rr:template":
            self.subject_map = TemplateSubjectMap(subject_placeholder, class_value)
        elif rr_type == "rr:column":
            self.subject_map = ColumnSubjectMap(subject_placeholder, class_value)

    def add_logical_table(self, type, value):
        if type == "rr:tableName":
            self.sql_statement = "Select * from " + value
        elif type == "rr:sqlQuery":
            self.sql_statement = value
        else:
            print("This is an unsported type")

    def create_subject_map_with_template(self, subject, predicate, class_value):
        pass

    def add_predicate_object_map(self):
        pass
