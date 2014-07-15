'''
Created on 15.07.2014

@author: lyckade
'''
import unittest
import classes


class Test(unittest.TestCase):
    
    def setUp(self):
        self.AreaInst = classes.Area()


    def testAddPoint(self):
        self.AreaInst.addPoint(-80.1,26.01)
        self.AreaInst.addPoint(-79.2,27.123)
        self.AreaInst.addPoint(-79.4,27.123)
        self.assertEqual(self.AreaInst.latMin, -80.1)
        self.assertEqual(self.AreaInst.latMax, -79.2)
        self.assertEqual(self.AreaInst.lngMin, 26.01)
        self.assertEqual(self.AreaInst.lngMax, 27.123)
    
    def testAddArea(self):
        Area2 = classes.Area()
        Area2.addPoint(53.0003,10.123)
        Area2.addPoint(53.123,9.883)
        self.AreaInst.addArea(Area2)
        self.assertEqual(self.AreaInst.echo(False), Area2.echo(False))
        Area3 = classes.Area()
        Area3.addPoint(53.4,10.01)
        Area3.addPoint(53.1,10.01)
        self.AreaInst.addArea(Area3)
        self.assertEqual(self.AreaInst.echo(False), 'latMin: 53.0003, latMax: 53.4, lngMin: 9.883, lngMax: 10.123')
        

    def testEcho(self):
        self.AreaInst.addPoint(-80.1,26.01)
        self.AreaInst.addPoint(-79.2,27.123)
        self.assertEqual(self.AreaInst.echo(False), 'latMin: -80.1, latMax: -79.2, lngMin: 26.01, lngMax: 27.123')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAddPoint']
    unittest.main()