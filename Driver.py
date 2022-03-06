from Job import Job
from Person import Person


class Driver(Person, Job):

    def __init__(self, lisenceID="-", activeUntil="-", vehicleType="-"):
        self.__lisenceID = lisenceID
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType

    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType

    def setLisenceID(self, lisenceID):
        self.__lisenceID = lisenceID

    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def setvehicleType(self, vehicleType):
        self.__vehicleType = vehicleType

    def getActiveUntil(self):
        return self.__activeUntil

    def getvehicleType(self):
        return self.__vehicleType

    def getLisenceID(self):
        return self.__lisenceID

    def getVehicleType(self):
        return self.__vehicleType
