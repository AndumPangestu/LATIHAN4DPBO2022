from Vehicle import Vehicle


class Airplane(Vehicle):

    def __init__(self, age=0, type="-", wingsLength=0):
        self.__age = age
        self.__type = type
        self.__wingsLength = wingsLength

    def setAge(self, age):
        self.__age = age

    def setType(self, type):
        self.__type = type

    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength

    def getType(self):
        return self.__type

    def getWingsLength(self):
        return self.__wingsLength

    def getAge(self):
        return self.__age
