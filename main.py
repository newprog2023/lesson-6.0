class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        self.__access_level = access_level

    def __str__(self):
        return f"Пользователь (ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'

    def _add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"\nПользователь {user.get_name()} добавлен.")
        else:
            print("неправильный пользователь, не добавлен")

    def _remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"\nПользователь ID {user_id} удален.")
                return
        print(f"\nПользователь ID {user_id} не найден.")

    def __str__(self):
        return f"Администратор (ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self.__access_level})"
        

# Пример использования
print (__name__)
if __name__ == "__main__":
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    admin = Admin(3, "Charlie")

    user_list = [user1, user2, admin]

    print("\nСписок пользователей:")
    for u in user_list:
        print(u)

    # Admin добавляет нового пользователя
    new_user = User(4, "Dave")
    admin._add_user(user_list, new_user)

    print("\nСписок пользователей:")
    for user in user_list:
        print(user)

    # Admin удаляет пользователя
    admin._remove_user(user_list, 2)

    print("\nСписок пользователей:")
    for user in user_list:
        print(user)