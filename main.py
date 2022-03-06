
import imp
from Ship import Ship
from Airplane import Airplane
from Driver import Driver

ship = [Ship() for i in range(5)]

ship[0].setAge(10)
ship[0].setType("Feri")
ship[0].setCountryOfManufacture("Indonesia")
ship[0].setFuelType("Bensin")
ship[0].setmaxPassengers(1000)

ship[1].setAge(20)
ship[1].setType("Feri")
ship[1].setCountryOfManufacture("Inggris")
ship[1].setFuelType("Solar")
ship[1].setmaxPassengers(2000)


ship[2].setAge(30)
ship[2].setType("Barang")
ship[2].setCountryOfManufacture("Indonesia")
ship[2].setFuelType("Bensin")
ship[2].setmaxPassengers(50)


ship[3].setAge(40)
ship[3].setType("Barang")
ship[3].setCountryOfManufacture("UEA")
ship[3].setFuelType("Solar")
ship[3].setmaxPassengers(10)

ship[4].setAge(10)
ship[4].setType("Feri")
ship[4].setCountryOfManufacture("Malaysia")
ship[4].setFuelType("Bensin")
ship[4].setmaxPassengers(1000)

i = 0

for i in range(5):
    print("Data Kapal : ")
    print("===========================")
    print("Age : ", ship[i].getAge())
    print("Type : ", ship[i].getType())
    print("Negara Pembuat : ", ship[i].getCountryOfManufacture())
    print("Tipe Bahan Bakar : ", ship[i].getFuelType())
    print("Max Penumpang : ", ship[i].getmaxPassengers())
    print("Keadaan Kapal : ", ship[i].move(True))
    print("===========================")

airplane = Airplane()
airplane.setAge(10)
airplane.setFuelType("Bensin")
airplane.setmaxPassengers(200)
airplane.setType("Komersial")
airplane.setWingsLength(30)

print("Data Pesawat : ")
print("===========================")
print("Tipe : ", airplane.getType())
print("Usia : ", airplane.getAge())
print("Tipe Bahan Bakar : ", airplane.getFuelType())
print("Max Penumpang : ", airplane.getmaxPassengers())
print("Panjang sayap : ", airplane.getWingsLength())
print("Keadaan Pesawat : ", airplane.move(True))
print("===========================")


driver = Driver()
driver.setNIK("1010")
driver.setName("Asep")
driver.setGender("Pria")
driver.setNIP("0021")
driver.setCompanyName("Gojek")
driver.setPosition("Driver")
driver.setLisenceID("0201")
driver.setActiveUntil("27 Januari 2030")
driver.setvehicleType("Mobil")


print("Data Driver : ")
print("===========================")
print("NIK : ", driver.getNIK())
print("Nama : ", driver.getName())
print("Gender : ", driver.getGender())
print("NIP : ", driver.getNIP())
print("Perusahaan : ", driver.getCompanyName())
print("Jabatan : ", driver.getPosition())
print("LIsence ID : ", driver.getLisenceID())
print("Masa Aktif : ", driver.getActiveUntil())
print("Tipe Kendaraan : ", driver.getvehicleType())
print("===========================")
