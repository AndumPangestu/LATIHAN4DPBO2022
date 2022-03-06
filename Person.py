class Person():

    def __init__(self, NIK="-", Name="-", Gender="-"):
        self.__NIK = NIK
        self.__Name = Name
        self.__Gender = Gender

    def setNIK(self, NIK):
        self.__NIK = NIK

    def setName(self, Name):
        self.__Name = Name

    def setGender(self, Gender):
        self.__Gender = Gender

    def getName(self):
        return self.__Name

    def getGender(self):
        return self.__Gender

    def getNIK(self):
        return self.__NIK

    def sleep(self):
        if (self.__Name != "-"):
            return self.__Name + " is sleeping"
        else:
            return "this person is sleeping"
