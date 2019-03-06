import unittest
import automated_tests as A
import manual_test as B
import E_400_700 as C
import testss as D

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(A))
suite.addTests(loader.loadTestsFromModule(B))
suite.addTests(loader.loadTestsFromModule(C))
suite.addTests(loader.loadTestsFromModule(D))

unittest.TextTestRunner().run(suite)