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
        latlng = {
            'lat':{'min':180,'max':-180},
            'lng':{'min':180,'max':-180}}
        
        for vals in self.aptDatData[icao]:
            if vals[0] in self.nodeCodes:
                if latlng['lat']['min']>float(vals[1]):
                    latlng['lat']['min']=float(vals[1])
                if latlng['lat']['max']<float(vals[1]):
                    latlng['lat']['max']=float(vals[1])
                if latlng['lng']['min']>float(vals[2]):
                    latlng['lng']['min']=float(vals[2])
                if latlng['lng']['max']<float(vals[2]):
                    latlng['lng']['max']=float(vals[2])
        return latlng
        
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