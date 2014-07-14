'''
Created on 14.07.2014

@author: lyckade
'''
import unittest
import classes

class TestClassAptDat(unittest.TestCase):
    def setUp(self):
        self.aptDatInst = classes.AptDat('../src/apt.dat')
    
    
    def testParseLine(self):

        aptDatInst = self.aptDatInst
        line1 = "100 30.00 1 0 0.25 0 2 0 12  41.25261908 -072.03575022    0   69 2 0 0 1 30  41.25141173 -072.02738496    0   71 2 0 0 1"
        line2 = "1     53 1 0 EDDH Hamburg Airport"
        l = aptDatInst.parseLine(line1)
        self.assertEqual(l[0], '100')
        self.assertEqual(l[4], '0.25')
        l = aptDatInst.parseLine(line2)
        self.assertEqual(l[0], '1')
        self.assertEqual(l[1], '53')
        self.assertEqual(l[-2], 'Hamburg')
        self.assertEqual(l[4], 'EDDH')

        
