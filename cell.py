
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

	def neighbors(self, x, y):
		offsets = [-1, 0, 1]
		for x_off in offsets:
			for y_off in offsets:
				if x_off == 0 and y_off == 0 or (x+x_off >= self.size) or (y+y_off >= self.size):
					continue
				if x + x_off < 0 or y + y_off < 0:
					continue
				yield (x + x_off, y+ y_off)

	def countNeighbors(self,x,y):
		neighbors = self.neighbors(x,y)
		return sum([int(self.get(x, y)) for x, y in neighbors])

	def nextState(self,x,y):
		c = self.countNeighbors(x,y)
		cur_state = self.get(x,y)
		return (cur_state and c == 2) or (c == 3)

	def tick(self):
		# new dict
		# for x in range(size), y in range(size)
		# if next state (x, y) new dict[x, y] = true
		# grid = new dict



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

	def testNeighbors(self):
		c = Game(10)
		self.assertTrue((0,0) in c.neighbors(1, 1))
		self.assertTrue((2,2) in c.neighbors(1, 1))
		self.assertEquals(8, len([1 for x in c.neighbors(1, 1)]))

	def testNeighborsOutOfBounds(self):
		c = Game(5)
		self.assertFalse((-1, -1) in c.neighbors(0, 0))
		self.assertFalse((5, 5) in c.neighbors(4, 4))

	def testCountNeighbors(self):
		c = Game(5) 
		c.set(0, 0)
		c.set(1, 0)
		self.assertEquals(2, c.countNeighbors(1,1))
		self.assertEquals(2, c.countNeighbors(0,1))
		self.assertEquals(0, c.countNeighbors(3, 3))

	def testNextState(self):
		c = Game(5)
		self.assertEquals(0, c.nextState(0,0))
		c.set(0,0)
		c.set(1, 0)
		c.set(2, 0)
		self.assertEquals(False, c.nextState(0, 0))
		self.assertEquals(True, c.nextState(1, 0))
		self.assertEquals(True, c.nextState(1, 1))
		self.assertEquals(False, c.nextState(2, 0))

        

if __name__ == '__main__':
    unittest.main()
