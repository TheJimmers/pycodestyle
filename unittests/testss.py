import unittest
from pycodestyle import maximum_line_length, tabs_or_spaces, imports_on_separate_lines, whitespace_before_comment

class testlines(unittest.TestCase):
    def test_linesize(self):
        s = "mkmmkmkmmkmkmkmkmkmkkkmkmkmkmkmkmkmmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkkkmkmkmkmkmkmkm"
        m = "poop"
        assert(len(s) > 79)
        self.assertTrue(maximum_line_length(s, 79, 0, 0,0))
        assert(len(m) < 79)
        self.assertFalse(maximum_line_length(m, 79,0,0,0))
    def test_tabs(self):
        g = "wuddlewuddle"
        p = " wuddlewuddle"
        m = ' '
        tab = chr(9)
        h = tab + g
        z = h + p
        assert m == ' '
        self.assertFalse(tabs_or_spaces(p, m))
        self.assertFalse(tabs_or_spaces(h, chr(9)))
        self.assertTrue(tabs_or_spaces(z,m))
    def testimports(self):
        s = "import taco, bunghole"
        h = "import taco"

        self.assertTrue(imports_on_separate_lines(s))
        self.assertFalse(imports_on_separate_lines(h)==imports_on_separate_lines(s))
    def testwhitespace_before_comment(self):
        s = "   #poop"
        h = "#poop"
        self.assertTrue(whitespace_before_comment(s,s))
        self.assertFalse(whitespace_before_comment(h,h)==whitespace_before_comment(s,s,))


if __name__ == '__main__':
    unittest.main()
