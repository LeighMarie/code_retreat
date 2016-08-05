
import unittest
        
class Game:
	def __init__(self):
		self.grid = {}

	def set(self, x, y):
		self.grid[(x, y)] = True

	def get(self,x,y):
		if (x,y) in self.grid:
			return self.grid[(x,y)]
		else:
			return False
                

class ConwayTest(unittest.TestCase):
	def testGetSet(self):
		c = Game()
		c.set(1, 1)
		self.assertTrue(c.grid[(1, 1)])
	def testGet(self):
		c = Game()
		c.set(2,2)
		self.assertTrue(c.get(2,2))
                
        

if __name__ == '__main__':
    unittest.main()
