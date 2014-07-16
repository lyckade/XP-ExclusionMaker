'''
Created on 14.07.2014

@author: lyckade
'''
import unittest
import classes

class TestClassAptDat(unittest.TestCase):
    def setUp(self):
        self.aptDatInst = classes.AptDat()
        self.aptDatFile = '../src/apt.dat'
        # Examples for apt.dat lines
        self.line1 = "100 30.00 1 0 0.25 0 2 0 12  41.25261908 -072.03575022    0   69 2 0 0 1 30  41.25141173 -072.02738496    0   71 2 0 0 1"
        self.line2 = "1     53 1 0 EDDH Hamburg Airport"
    
    def testGetIcao(self):
        icao = self.aptDatInst.getIcao(self.line1)
        self.assertFalse(icao, "ICAO Definition just for linetype 1")
        icao = self.aptDatInst.getIcao(self.line2)
        self.assertEqual(icao, 'EDDH')
        
    def testParseLine(self):
        l = self.aptDatInst.parseLine(self.line1)
        self.assertEqual(l[0], '100')
        self.assertEqual(l[4], '0.25')
        l = self.aptDatInst.parseLine(self.line2)
        self.assertEqual(l[0], '1')
        self.assertEqual(l[1], '53')
        self.assertEqual(l[-2], 'Hamburg')
        self.assertEqual(l[4], 'EDDH')
        
    def testSearchIcaoCodes(self):
        self.aptDatInst.loadFile(self.aptDatFile)
        icaoCodes = self.aptDatInst.searchIcaoCodes()
        self.assertGreater(len(icaoCodes), 0, 'Minimum one icao should be found')
        self.assertTrue('EDDH' in icaoCodes, 'EDDH is part of the apt.dat')
    
    def testGetAirportArea(self):
        self.aptDatInst.loadFile(self.aptDatFile)
        latlng = self.aptDatInst.getAirportArea('EDDH')
        self.assertEqual(latlng.latMax, 53.65809636)
        self.assertEqual(latlng.latMin, 53.61470575)
        self.assertEqual(latlng.lngMax, 10.00801022)
        self.assertEqual(latlng.lngMin, 9.95672548)
        

        


        
