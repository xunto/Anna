from core import build
import unittest


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        self.maxDiff = 2500

    def test_brackets(self):
        cases = [
            "((A->B)->((A->(B->C))->(A->C)))",
            "(A->B)->((A->(B->C))->(A->C))",
            "(A->B)->(A->B->C)->(A->C)",
            "(A->B)->(A->B->C)->A->C",
        ]

        table1 = build(cases.pop())
        for case in cases:
            table2 = build(case)
            self.assertEquals(table1.to_json(), table2.to_json())