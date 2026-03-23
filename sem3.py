import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

        if self.__side1 + self.__side2 <= self.__side3 or self.__side1 + self.__side3 <= self.__side2 or self.__side2 + self.__side3 <= self.__side1:
            raise ValueError("Wrong side")

        self.per = self.__side1 + self.__side2 + self.__side3
        p = self.per/2
        self.s = (p * (p - self.__side1) * (p - self.__side2) * (p - self.__side3)) ** 0.5
    
    def angle(self):
        cos_a = (self.__side1**2 + self.__side2**2 - self.__side3**2) / (2 * self.__side1 * self.__side2)
        cos_b = (self.__side1**2 + self.__side3**2 - self.__side2**2) / (2 * self.__side1 * self.__side3)
        cos_c = (self.__side3**2 + self.__side2**2 - self.__side1**2) / (2 * self.__side3 * self.__side2)

        print("Между а и б:", math.degrees(math.acos(cos_a)), "Между б и с:", math.degrees(math.acos(cos_b)), "Между а и c:", math.degrees(math.acos(cos_c)))

trngl1 = Triangle(int(input()), int(input()), int(input()))
trngl1.angle()
print(trngl1.per)