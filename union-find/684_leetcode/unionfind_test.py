import unittest

from unionfind import unionfindrank as uf

class Test(unittest.TestCase):
    
    def test1(self):
        ins = uf(3)
        ins.union(1,2)
        self.assertTrue(ins.connected(1,2))
        self.assertFalse(ins.connected(0,1))


    def test2(self):
        ins = uf(10)
        ins.union(0,8)
        ins.union(0,1)
        ins.union(2,0)
        ins.union(9,4)
        ins.union(7,6)
        ins.union(7,9)

        ins.print_union()


        self.assertTrue(ins.connected(2, 8))
        self.assertTrue(ins.connected(4, 6))
        self.assertFalse(ins.connected(9, 0))


if __name__ == "__main__":
    unittest.main()