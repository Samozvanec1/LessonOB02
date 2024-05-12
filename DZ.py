class User():
    def __init__(self, name, id, dost_Us):
        self.public_name = name
        self._protected_id = id
        self._protected_dost_Us = dost_Us

class User:
    def __init__(self, id, name):
        self._protected_id = id
        self.public_name = name
        self._protected_dost_Us = 'user'

    #нужно задуйствовать аргументы  ПОЛУЧИЛИ И ВЕРНУЛИ   (написали передали)
    def get_protected_id(self):
        return self._protected_id

    def get_name(self):
        return self.public_name


    def get_protected_dost_Us(self):
        return self._protected_dost_Us


    def __str__(self):
        return f"Номер пользователя: {self._protected_id}, Зови меня: {self.public_name}, Всё тебе доступно: {self._protected_dost_Us})"


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__private_dost_AD= 'admin'

    def get_private_dost_AD(self):
        return self.__private_dost_AD

    def add_user(self, user_list, user):
        if isinstance(user, User):  #функция проверки объекта к классу
            user_list.append(user) #добавляем в список
            print(f"Уважаемый(-ая) {user.get_name()} тебе повезло, ты в списке.")
        else:
            print("Промашка вышла, нет тут никого")

    def remove_user(self, user_list, id):
        for I in user_list:
            if I.get_protected_id() == id:
                user_list.remove(I)
                print(f"Номер пользователя {id} Чё выпинали тебя?")
                return
        print(f"Номер пользователя  {id} не обнаружен")

    def __str__(self):
        return f"Номер господина управителя: {self.get_protected_id()}, Управитель: {self.get_name()}, Всемерный доступ: {self.get_private_dost_AD()})"



if __name__ == "__main__":
    # проектируем и строим список пользователей
    users = []

    # вводим переменную админ и присваиваем к классу даём ему имя и звание(номер)
    admin = Admin("A1", "Velimir")

    # зову юзеров
    user1 = User("U1", "Egor")
    user2 = User("U2", "Lenya")

    # адмн добавляет пользователей (в список (users) и даёт id)
    admin.add_user(users, user1)
    admin.add_user(users, user2)

    # вывод пользователей на печать  Вывод списка на печать
    for user in users:
        print(user)

    # удаление админом
    admin.remove_user(users, "U1")

    # результат удаления в печати. Вывод списка на печать
    for user in users:
        print(user)

    # все об админе
    print(admin)

