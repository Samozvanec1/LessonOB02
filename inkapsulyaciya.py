class Test():
    def __init__(self):
        self.public = "публичный атрибут"
        self._protected = "защищённый атрибут"
        self.__private = "ПРИВАТНЫЙ АТРИБУТ"

    def get_private(self):
        return self.__private #передача (возвращение) функции
    def set_private (self, value):
        self.__private = value # value  локальная переменная, обитает только в функции set_private
        # при попытку вытащить, анигилируетсяю. value является документально подтверждённым миражом

test = Test()
print(test.public)
print(test._protected)
#print(test.__private)

bb = test.get_private()
print(test.get_private())
print(bb)

test.set_private("получили значение приватного атрибута")
print(test.get_private())



