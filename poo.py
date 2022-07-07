import math

class Robot:
    garantie=10
    nr_roboti=0
    def __init__(self,nume,serial_number,hardware,software,sleep,age):
        self.nume = nume
        self.serial_number = serial_number
        self.hardware = hardware
        self.software = software
        self.sleep=sleep
        self.age=age
        Robot.nr_roboti=+1

    def turn_on(self):
        if self.sleep==False:
            return f'{self.nume} is already running'
        else:
            self.sleep=False
            return f'{self.nume} is not already running'

    def end_of_life(self):
        if self.age>self.garantie:
            print(f'{self.nume} is end of life')
        else:
            print(f'{self.nume} has {self.garantie-self.age} age')

    @property
    def identify(self):
        return self.nume+'->'+self.serial_number

    @identify.setter
    def identify(self,ident):
        nume,serial=ident.split(' ')
        self.nume=nume
        self.serial_number=serial

    @classmethod
    def seteaza_garantia(cls,ani):
        cls.garantie=ani

    @classmethod
    def from_list(cls,lst):
        nume,serial_number,hardware,software,age,sleep=lst
        return cls(nume,serial_number,hardware,software,age,sleep)

    @staticmethod
    def dimensiune_cerc(raza):
        return 2*math.pi*raza,math.pi*raza*raza


    def __repr__(self):
        return f'Robot("{self.nume}", "{self.serial_number}", "{self.hardware}", "{self.software}", {self.garantie}, {self.sleep})'

    def __str__(self):
        return self.nume

    def __add__(self, other):
        return self.nume+other.nume

r1=Robot("John","12345","i5","Python",True,11)
r2 = Robot("Mark", "22333", "i5", "C++", True, 3)
# print(r1.hardware)
# print(r1.sleep)
# print(r1.turn_on())
# print(r1.sleep)
# print(Robot.garantie)
# print(Robot.end_of_life(r1))
# print(Robot.nr_roboti)
# r1=Robot()
# r2=Robot()
# print(r1)
# print(r2)
# r1.nume="John"
# r1.serial_number="12344"
# r1.hardware="i5"
# r1.software="python"
#
# r2.nume="Mark"
# r2.serial_number="12345"
# r2.hardware="i5"
# r2.software="C++"
#
# print(r1.nume)

class Aspirator(Robot):
    garantie=15
    def __init__(self,nume,serial_number,hardware,software,sleep,age,power):
        super().__init__(nume,serial_number,hardware,software,sleep,age)
        self.power=power
robot_attributes=['Michal','33333','i7','Python',1,True]
nume,serial_number,hardware,software,age,sleep=robot_attributes
r3=Robot(nume,serial_number,hardware,software,age,sleep)
# print(r3.serial_number)
#
# Robot.seteaza_garantia(11)
# print(Robot.garantie)
# print(Robot.dimensiune_cerc(9))
a1=Aspirator("George","42333","i5","C++",True,3,"1kw")
print(a1.serial_number)
print(r1.identify)
r1.nume="Jonny"
print(r1.identify)
r1.identify='Marcus 123321'
print(r1.nume)