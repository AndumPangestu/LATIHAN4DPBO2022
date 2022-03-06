from Vehicle import Vehicle


class Ship(Vehicle):

    def __init__(self, age=0, type="-", countryOfManufacture=0):
        self.__age = age
        self.__type = type
        self.__countryOfManufacture = countryOfManufacture

    def setAge(self, age):
        self.__age = age

    def setType(self, type):
        self.__type = type

    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture

    def getType(self):
        return self.__type

    def getCountryOfManufacture(self):
        return self.__countryOfManufacture

    def getAge(self):
        return self.__age
