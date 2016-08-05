"""Test example for python."""

import unittest

class FooTest(unittest.TestCase):
    def testBar(self):
       self.assertTrue('FOO'.isupper())
       self.assertFalse('Foo'.isupper())

    def testCell(self):
        cell = Cell((0,0), is_alive=True)
        self.assertTrue(cell.is_alive)
        

if __name__ == '__main__':
    unittest.main()
