class AptDat():
    """
    Information about the apt.dat file
    """
    
    def __init__(self,aptDatFile):
        self.aptDatFile = aptDatFile
        
        # Row codes for the node definition
        self.nodeCodes = ["111","112","113","114","115","116"]
        
        # Row code filter
        self.filterCodes = ["1"] + self.nodeCodes
        
        self.aptDatLines = []
        
    
    def loadFile(self):
        self.aptDatLines = []
        aptDatFile = open(self.aptDatFile)
        for line in aptDatFile:
            print line.strip()
        aptDatFile.close()
        
    def parseLine(self,line):
        values = line.strip().split()
        return values
    
    def searchIcaoCodes(self):
        """
        Returns a list with all the ICAO codes find in the apt.dat file of the
        scenery. If there is no apt.dat file the list will be empty []
        """
        # If there is no apt.dat an empty list is returned
        if not self.aptDat:
            return []
        
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