
import unittest
        
class Game:
	def __init__(self):
		self.grid = {}

	def set(self, x, y):
		self.grid[(x, y)] = True
                

class ConwayTest(unittest.TestCase):
	def testGetSet(self):
		c = Game()
		c.set(1, 1)
		self.assertTrue(c.grid[(1, 1)])
                
        

if __name__ == '__main__':
    unittest.main()
