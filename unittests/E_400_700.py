import unittest
from pycodestyle import imports_on_separate_lines, compound_statements

class E_400_700_Tester(unittest.TestCase):
    def test_imports_on_seperate_lines(self):
            passes = ["from subprocess import Popen, PIPE","from myclas import MyClass",
                      "from foo.bar.yourclass import YourClass","import myclass",
                      "import foo.bar.yourclass", "import os\nimport sys"]
            fails = ["import sys, os", "import sys; import os", "import class, class2, class3"]
            
            for case in passes:
                for res in imports_on_separate_lines(case):
                    self.assertTrue(res == "")
            
            for case in fails:
                for res in imports_on_separate_lines(case):
                    self.assertTrue(res != "")

    def test_compound_statements(self):
            passes = ["do_one()", "do_two()", "do_three()"]
            fails = ["if foo == 'blah': do_blah_thing()","for x in lst: total += x",
                     "while t < 10: t = delay()","if foo == 'blah': do_blah_thing()",
                     "else: do_non_blah_thing()","try: something()","finally: cleanup()",
                     "if foo == 'blah': one(); two(); three()","do_one(); do_two(); do_three()",
                     "do_four();  # useless semicolon","def f(x): return 2*x","f = lambda x: 2*x"]
            
            for case in passes:
                for res in compound_statements(case):
                    print(res)
                    self.assertTrue(res == "")
            
            for case in fails:
                for res in compound_statements(case):
                    self.assertTrue(res != "")


if __name__ == '__main__':
    unittest.main()