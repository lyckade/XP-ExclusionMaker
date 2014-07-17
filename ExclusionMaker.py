'''
Created on 17.07.2014

@author: lyckade
'''
import lib.classes

properties = ['PROPERTY sim/exclude_fac',
              'PROPERTY sim/exclude_obj',
              'PROPERTY sim/exclude_lin',
              'PROPERTY sim/exclude_net',
              'PROPERTY sim/exclude_str',
              'PROPERTY sim/exclude_pol']
skipIcaos = ['Y55','4B7','WT18','W23']

aptDat = lib.classes.AptDat()
aptDat.loadFile('src/apt.dat')
icaoCodes = aptDat.searchIcaoCodes()
for icaoCode in icaoCodes:
    if icaoCode in skipIcaos:
        continue
    print "Making exclusion scenery for %s" % (icaoCode)
    airportArea = aptDat.getAirportArea(icaoCode)
    dsfTool = lib.classes.DSFTool()
    dsfTool.icao = icaoCode
    dsfTool.sceneryPath = 'examples/ExclusionScenery/Exclusion_%s' % (icaoCode)
    for p in properties:
        dsfTool.addAreaProperty(p,airportArea)
    dsfTool.writeFiles()
