class AptDat():
    """
    Information about the apt.dat file
    """
    
    def __init__(self):
        self.aptDatFile = ''
        
        # Row codes for the node definition
        self.nodeCodes = ["111","112","113","114","115","116"]
        
        # Row code filter
        self.filterCodes = ["1"] + self.nodeCodes
        
        self.aptDatData = {}
        #self.lines = self.loadFile(self.aptDatFile)
        
    
    def getIcao(self,line):
        vals = self.parseLine(line)
        if vals[0] is not '1':
            return False
        return vals[4]
    
    def getAirportArea(self,icao):
        area = Area()
        latlng = {
            'lat':{'min':180,'max':-180},
            'lng':{'min':180,'max':-180}}
        
        for vals in self.aptDatData[icao]:
            if vals[0] in self.nodeCodes:
                area.addPoint(vals[1], vals[2])
        return area
        
    def loadFile(self,aptDatFile=''):
        if aptDatFile=='':
            aptDatFile = self.aptDatFile
        self.aptDatData = {'':[]}
        icao = ''
        aptDatFile = open(aptDatFile,'r')
        for line in aptDatFile:
            newIcao = False
            newIcao = self.getIcao(line)
            if newIcao:
                icao = newIcao
                if newIcao not in self.aptDatData:
                    self.aptDatData[newIcao] = []
            vals = self.parseLine(line)
            if vals[0] in self.filterCodes:
                self.aptDatData[icao].append(vals)
        aptDatFile.close()
        
    def parseLine(self,line):
        values = line.strip().split()
        if len(values) == 0:
            values.append('')
        return values
    
    def searchIcaoCodes(self):
        """
        Returns a list with all the ICAO codes find in the apt.dat file of the
        scenery. If there is no apt.dat file the list will be empty []
        """
        icaoCodes = []
        for icao in self.aptDatData:
            icaoCodes.append(icao)
        return icaoCodes

class Area():
    def __init__(self):
        self.latMin = 180.0
        self.latMax = -180.0
        self.lngMin = 180.0
        self.lngMax = -180.0
        self.corners = self.makeCorners()
        
    def addArea(self,Area):
        self.addPoint(Area.latMin, Area.lngMin)
        self.addPoint(Area.latMax, Area.lngMax)
        
    def addPoint(self,lat,lng):
        lat = float(lat)
        lng = float(lng)
        if self.latMin > lat:
            self.latMin = lat
        if self.latMax < lat:
            self.latMax = lat
        if self.lngMin > lng:
            self.lngMin = lng
        if self.lngMax < lng:
            self.lngMax = lng
        self.corners = self.makeCorners()
            
    def echo(self,printVals=True):
        output = "latMin: %s, latMax: %s, lngMin: %s, lngMax: %s" % (self.latMin,self.latMax,self.lngMin,self.lngMax)
        if printVals:
            print output
        else:
            return output
    
    def makeCorners(self):
        corners = [
                        (self.latMin,self.lngMin),
                        (self.latMax,self.lngMin),
                        (self.latMin,self.lngMax),
                        (self.latMax,self.lngMax)]
        return corners

        
    
class DSFTool():
    
    def __init__(self):
        self.dsfFiles = {}
        self.Area = Area()
        
    
    def addAreaProperty(self,property,Area):
        self.Area.addArea(Area)
        self.areaPropertyToFile(property, Area)
        
    def areaPropertyToFile(self,property,Area):
        pass
        
        
    
    #def addSimpleProperty(self,property,string):
    #    return True
    
    #def makeFiles(self):
    #    return True
    
    def koordinateToString(self,koordinate,fill=2,round=1):
        from math import floor
        koordinate = float(koordinate)/round
        if koordinate >= 0.0:
            prefix = '+'
        else:
            prefix = '-'
        value = str(int(abs(floor((koordinate)))*round))
        string = '%s%s' % (prefix,value.zfill(fill))
        return string
        
            
    def makeFilesFromArea(self,Area):
        files = []
        for point in Area.corners:
            fileName = self.makeFileName(point[0],point[1])
            if fileName not in files:
                files.append(fileName)
        return files
             
    
    def makeFileName(self,south,west):
        fileName = '%s%s.txt' % (self.koordinateToString(south, 2, 1),self.koordinateToString(west, 3, 1))
        return fileName
        
    
    def makeHeader(self,south,west):
        headerDef = [
                     'I',
                     '800',
                     'DSF2TEXT',
                     '',
                     'PROPERTY sim/planet earth',
                     'PROPERTY sim/overlay 1',
                     'PROPERTY sim/creation_agent XPExclusionMaker']
        #headerDef.append(PROPERTY sim/west)
    
    
    
    