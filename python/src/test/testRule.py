import unittest
from ..data.rule  import  Rule


class TestRule(unittest.TestCase):

    def test_create_rule(self):
        rule_id = "http://www.test.com/TriplesMap1"
        table = "PROFESSOR"
        template = "http://data.example.com/prof/{ProfID}"
        class_value = "ex:Employee"
        predicate = "ex:name"
        value = "LastName"

        rule = Rule(rule_id)
        rule.add_logical_table("rr:tableName", table)
        rule.create_subject_map("rr:template", template, class_value)
        rule.add_predicate_object_map(predicate, "rr:column", value)

        s, p, o = rule.get_subject_map()

        self.assertEqual(s, template)
        self.assertEqual(p, "rdf:type")
        self.assertEqual(o, class_value)

        p, o = rule.next_predicate_map()
        self.assertEqual(p, predicate)
        self.assertEqual(o, value)

        sql = rule.get_logical_table_sql()
        expected_sql = "Select * from " + table
        self.assertEqual(sql, expected_sql)

    def test_create_rule_column(self):
        rule_id = "http://www.test.com/TriplesMap4"
        column = "University"
        class_value = "ex:University"
        column_template = "http://data.example.com/university/{University}"
        predicate = "ex:works"

        rule = Rule(rule_id)
        rule.create_subject_map("rr:column", column, class_value)

        s, p, o = rule.get_subject_map()

        self.assertEqual(s, column)
        self.assertEqual(p, "rdf:type")
        self.assertEqual(o, class_value)

        rule.add_predicate_object_map(predicate, "rr:template", column_template)
        p, o = rule.next_predicate_map()
        self.assertEqual(predicate, p)
        self.assertEqual(column_template, o)