import random

# ENCAPSULATION

# -> Hiding Information / Properties
# -> Inject Information / Properties
# Konsep method Getter (nampilin properties)
# & Setter (inject properties)


class Smartphone:

    def __init__(self, brand, type) -> None:
        self.__brand = brand  # properties public
        self.__type = type  # properties private (hide)
        self.__series = random.random()

    def getBrand(self):  # method getter
        return self.__brand

    def setType(self, type):  # method setter, control properties yang mau diganti
        if (type == '14 pro'):
            self.__type = type

    def getType(self):  # method getter
        return self.__type

    def getFullInfo(self):  # getter -> ngontrol properties yang mau dikeluarin
        return self.__brand + ' ' + self.__type + ' ' + str(self.__series)


iphone = Smartphone('apple', '13 Pro')

iphone.setType('redmi 12')

print(iphone.getFullInfo())
