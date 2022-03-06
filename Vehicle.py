class Vehicle():

    def __init__(self, fuelType="-", maxPassengers=0):
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassengers

    def setFuelType(self, fuelType):
        self.__fuelType = fuelType

    def setmaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers

    def getFuelType(self):
        return self.__fuelType

    def getmaxPassengers(self):
        return self.__maxPassengers

    def move(self, type):
        if type == True:
            return "this vehicle is moving"
        else:
            return "this vehicle is not moving"
