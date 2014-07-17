'''
Created on 16.07.2014

@author: lyckade
'''
import unittest
import classes

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testKoordinateToString(self):
        dsf = classes.DSFTool()
        #print dsf.koordinateToString(3.123123,3)
        self.assertEqual(dsf.koordinateToString(3.123123,2), '+03')
        self.assertEqual(dsf.koordinateToString(3.123123,3), '+003')
        self.assertEqual(dsf.koordinateToString(-33.9,2), '-34')
        
        self.assertEqual(dsf.koordinateToString('-33.9',2), '-34')
        self.assertEqual(dsf.koordinateToString('-081',3,10), '-090')
        self.assertEqual(dsf.koordinateToString(-33.9,2,10), '-40')
        self.assertEqual(dsf.koordinateToString(3.123123,3,10), '+000')
        self.assertEqual(dsf.koordinateToString(13.123123,3,10), '+010')
        
    def testMakeFileName(self):
        dsf = classes.DSFTool()
        self.assertEqual(dsf.makeFileName('-33.9273','151.393'), '-34+151')
        self.assertEqual(dsf.makeFileName('53.9273','10.393'), '+53+010')
        
    def testMakeFilesFromAres(self):
        dsf = classes.DSFTool()
        area = classes.Area()
        area.addPoint(53.65809636,10.00801022)
        area.addPoint(53.61470575,9.95672548)
        files = dsf.makeFilesFromArea(area)
        self.assertEqual(files, ['+53+009', '+53+010'])
    
    def testAddAreaProperty(self):
        dsf = classes.DSFTool()
        area = classes.Area()
        area.addPoint(53.65809636,10.00801022)
        area.addPoint(53.61470575,9.95672548)
        dsf.addAreaProperty('PROPERTY sim/exclude_fac',area)
        self.assertTrue('PROPERTY sim/exclude_fac 10.00000000/53.61470575/10.00801022/53.65809636' in dsf.dsfFiles['+53+010'])
        
        
    def testMakeDirFromFilename(self):
        dsf = classes.DSFTool()
        dir = dsf.makeDirFromFilename('+26-081')
        self.assertEqual(dir, '+20-090')
        dir = dsf.makeDirFromFilename('+46+005.dsf')
        self.assertEqual(dir, '+40+000')
        dir = dsf.makeDirFromFilename('-21-045.txt')
        self.assertEqual(dir, '-30-050')
        
    def testMakeHeader(self):
        dsf = classes.DSFTool()
        output = ['I', '800', 'DSF2TEXT', '', 'PROPERTY sim/planet earth', 'PROPERTY sim/overlay 1', 'PROPERTY sim/creation_agent XPExclusionMaker', 'PROPERTY sim/west -81', 'PROPERTY sim/east -80', 'PROPERTY sim/north 27', 'PROPERTY sim/south 26']
        self.assertEqual(dsf.makeHeader('+26-081.txt'), output)
        
    def testwriteFiles(self):
        dsf = classes.DSFTool()
        area = classes.Area()
        area.addPoint(53.65809636,10.00801022)
        area.addPoint(53.61470575,9.95672548)
        dsf.addAreaProperty('PROPERTY sim/exclude_fac',area)
        dsf.addAreaProperty('PROPERTY sim/exclude_obj',area)
        dsf.addAreaProperty('PROPERTY sim/exclude_lin',area)
        dsf.addAreaProperty('PROPERTY sim/exclude_net',area)
        dsf.addAreaProperty('PROPERTY sim/exclude_str',area)
        dsf.addAreaProperty('PROPERTY sim/exclude_pol',area)
        #dsf.
        dsf.writeFiles()





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()