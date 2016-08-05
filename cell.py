
import unittest
        
class Game:
	def __init__(self, size):
		self.grid = {}
		self.size = size

	def set(self, x, y):
		self.check(x)
		self.check(y)
		self.grid[(x, y)] = True

	def get(self,x,y):
		self.check(x)
		self.check(y)
		if (x,y) in self.grid:
			return self.grid[(x,y)]
		else:
			return False
    
	def check(self, index):
		if index > self.size or index < 0:
			raise ValueError('Bad index')

class ConwayTest(unittest.TestCase):
	def testGetSet(self):
		c = Game(5)
		c.set(1, 1)
		self.assertTrue(c.grid[(1, 1)])
	def testGet(self):
		c = Game(5)
		c.set(2,2)
		self.assertTrue(c.get(2,2))

	def testCheck(self):
		c = Game(5)
		with self.assertRaises(ValueError):
			c.set(6,6)
		with self.assertRaises(ValueError):
			c.set(-1, 0)

                
        

if __name__ == '__main__':
    unittest.main()
