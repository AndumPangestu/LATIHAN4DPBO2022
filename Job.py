class Job():

    def __init__(self, NIP="-", companyName="-", position="-"):
        self.__NIP = NIP
        self.__companyName = companyName
        self.__position = position

    def setNIP(self, NIP):
        self.__NIP = NIP

    def setCompanyName(self, companyName):
        self.__companyName = companyName

    def setPosition(self, position):
        self.__position = position

    def getCompanyName(self):
        return self.__companyName

    def getPosition(self):
        return self.__position

    def getNIP(self):
        return self.__NIP
