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
            self.aptDatData[icao].append(self.parseLine(line))
            #vals = self.parseLine(line)
            #if vals[0] in self.filterCodes[]
            #self.aptDatLines.append()
        aptDatFile.close()
        print self.aptDatData
        
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
        # If there is no apt.dat an empty list is returned
       
        aptDatFile = open(self.aptDatFile)
        icaoCodes = []
        for line in aptDatFile:
            if line.strip().startswith("1 "):
                entries = line.strip().split()
                icaoCode = entries[4]
                if icaoCode not in icaoCodes:
                    icaoCodes.append(icaoCode)
        aptDatFile.close()
        return icaoCodes