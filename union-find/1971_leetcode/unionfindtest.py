import unittest

from unionfind import unionfind as uf

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.ins = uf(6)
    
    def test_union(self):
        self.ins.union(0,1)
        self.ins.union(2,3)
        
        self.assertTrue(self.ins.connected(0,1))
        self.assertTrue(self.ins.connected(2,3))
        self.ins.print_unionfind()
        self.assertFalse(self.ins.connected(0,3))

        self.ins.union(0, 3)

        self.assertTrue(self.ins.connected(1,2))
        self.ins.print_unionfind()
        
if __name__ == "__main__":
    unittest.main()