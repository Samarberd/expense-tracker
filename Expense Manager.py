import json
# Подсчёт общей стоимости всех покупок
def calculate_total(shopping_list):
    total = 0
    for item in shopping_list:
        total = total + item["total"]
    return total
# Класс пользователя: хранит имя, возраст и список покупок
class User:
    def __init__(self, name, age, shopping_list):
        self.name = name
        self.shopping_list = shopping_list
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):    
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным")
# Создание нового пользователя или загрузка сохранённого
while True:
    choice = input("1 — Создать нового пользователя" "\n2 — Загрузить сохранённого пользователя" "\nВаш выбор: ")
        # Создание нового пользователя
    if choice == "1":
        while True:
            name = input("Введите имя: ")
            if name.isalpha():
                break
            else:
                print("Имя должно содержать только буквы")
        while True:
            try:
                age = int(input("Введите возраст: "))
                if age >= 0:
                    break
                else:
                    print("Возраст не может быть отрицательным")
            except ValueError:
                print("Введите возраст целым числом")
        shopping_list = []
        while True:
            while True:
                item_name = input("Введите название покупки: ").strip()
                if item_name != "" and not item_name.isdigit():
                    break
                else:
                    print("Введите корректное название")
            while True:
                try:
                    quantity = int(input("Введите количество: "))
                    if quantity > 0:
                        break
                    else:
                        print("Количество должно быть больше нуля")
                except ValueError:
                    print("Введите целое число")
            while True:
                try:
                    price = float(input("Введите цену за одну единицу товара (сом): "))
                    if price > 0:
                        break
                    else:
                        print("Цена должна быть больше нуля")
                except ValueError:
                    print("Введите число")
            item = {"name": item_name, "quantity": quantity, "price": price, "total": quantity * price}
            shopping_list.append(item)
            while True:
                answer = input("Добавить ещё одну покупку? (да/нет): ")
                if answer == "да":
                    break
                elif answer == "нет":
                    break
                else:
                    print("Введите только «да» или «нет»")
            if answer == "нет":
                break
        user = User(name, age, shopping_list)
        break
    # Загрузка пользователя из JSON-файла
    elif choice == "2":
        try:
            with open("user.json", "r", encoding="utf-8") as file:
                loaded_data = json.load(file)
            user = User(loaded_data["name"], loaded_data["age"], loaded_data["shopping_list"])
            print("Данные пользователя загружены")
            break
        except FileNotFoundError:
            print("Сохранённый файл не найден. Сначала создайте пользователя")
    else:
        print("Введите 1 или 2")
# Изменение имени пользователя
while True:
    answer = input("Хотите изменить имя? (да/нет): ")
    if answer == "да":
        while True:
            new_name = input("Введите новое имя: ")
            if new_name.isalpha():
                user.name = new_name
                break
            else:
                print("Имя должно содержать только буквы")
        break
    elif answer == "нет":
        break
    else:
        print("Введите только «да» или «нет»")
# Изменение возраста пользователя
while True:
    answer = input("Хотите изменить возраст? (да/нет): ")
    if answer == "да":
        while True:
            try:
                new_age = int(input("Введите новый возраст: "))
                if new_age >= 0:
                    user.set_age(new_age)
                    break
                else:
                    print("Возраст не может быть отрицательным")
            except ValueError:
                print("Введите возраст целым числом")
        break
    elif answer == "нет":
        break
    else:
        print("Введите только «да» или «нет»")
# Добавление новой покупки в список
while True:
    answer = input("Хотите добавить покупку в список? (да/нет): ")
    if answer == "да":
        while True:
            new_item_name = input("Введите название покупки: ").strip()
            if new_item_name != "" and not new_item_name.isdigit():
                break
            else:
                print("Введите корректное название")
        while True:
            try:
                quantity = int(input("Введите количество: "))
                if quantity > 0:
                    break
                else:
                    print("Количество должно быть больше нуля")
            except ValueError:
                print("Введите целое число")
        while True:
            try:
                price = float(input("Введите цену за одну единицу товара (сом): "))
                if price > 0:
                    break
                else:
                    print("Цена должна быть больше нуля")
            except ValueError:
                print("Введите число")

        item = {"name": new_item_name, "quantity": quantity, "price": price, "total": quantity * price}
        user.shopping_list.append(item)
        break
    elif answer == "нет":
        break
    else:
        print("Введите только «да» или «нет»")
# Удаление покупки из списка
while True:
    answer = input("Хотите удалить покупку из списка? (да/нет): ")
    if answer == "да":
        old_shopping_list = input("Введите название покупки: ").strip()
        for item in user.shopping_list:
            if item["name"] == old_shopping_list:
                user.shopping_list.remove(item)
                print("Покупка удалена")
                break
        else:
            print("Такой покупки нет в списке")
        break
    elif answer == "нет":
        break
    else:
        print("Введите только «да» или «нет»")
# Вывод информации о пользователе и его покупках
print("Имя:", user.name)
print("Возраст:", user.get_age())
print("Список покупок:")
for item in user.shopping_list:
    print("Название:", item["name"], "| Количество:", item["quantity"], "| Цена:", item["price"], "сом", "| Сумма:", item["total"], "сом")
# Подсчёт и вывод общей суммы расходов
total_sum = calculate_total(user.shopping_list)
print("Общая сумма расходов:", total_sum, "сом")
# Сохранение данных пользователя в JSON-файл
user_data = {"name": user.name, "age": user.get_age(), "shopping_list": user.shopping_list}
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user_data, file, ensure_ascii=False, indent=4)
print("Данные сохранены")