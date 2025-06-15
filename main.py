import json
import os

FILENAME = "contacts.json"

# Загрузка контактов из файла
def load_contacts():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []

# Сохранение контактов в файл
def save_contacts(contacts):
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(contacts, file, ensure_ascii=False, indent=4)
        print("Контакты успешно сохранены.")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

# Показать все контакты
def show_all_contacts(contacts):
    if not contacts:
        print("Телефонный справочник пуст.")
        return
    for contact in contacts:
        print(
            f"[ID: {contact['id']}] {contact['name']} - {contact['phone']} ({contact['comment']})"
        )

# Создать контакт
def create_contact(contacts):
    name = input("Введите имя: ").strip()
    phone = input("Введите номер телефона: ").strip()
    comment = input("Введите комментарий: ").strip()

    if not name or not phone:
        print("Имя и телефон обязательны для заполнения.")
        return

    new_id = max((c["id"] for c in contacts), default=0) + 1
    contacts.append({"id": new_id, "name": name, "phone": phone, "comment": comment})
    print("Контакт успешно создан.")

# Найти контакт
def find_contact(contacts):
    query = input("Введите поисковое слово (имя, телефон или комментарий): ").lower().strip()
    results = [
        c for c in contacts
        if query in c["name"].lower() or
           query in c["phone"].lower() or
           query in c["comment"].lower()
    ]
    if results:
        print(f"Найдено {len(results)} совпадений:")
        show_all_contacts(results)
    else:
        print("Контактов не найдено.")

# Изменить контакт
def edit_contact(contacts):
    try:
        contact_id = int(input("Введите ID контакта для редактирования: "))
        for contact in contacts:
            if contact["id"] == contact_id:
                print(f"Редактирование контакта: {contact['name']}")
                contact["name"] = input(f"Имя [{contact['name']}]: ") or contact["name"]
                contact["phone"] = input(f"Телефон [{contact['phone']}]: ") or contact["phone"]
                contact["comment"] = input(f"Комментарий [{contact['comment']}]: ") or contact["comment"]
                print("Контакт успешно обновлен.")
                return
        print("Контакт с таким ID не найден.")
    except ValueError:
        print("Неверный формат ID.")

# Удалить контакт
def delete_contact(contacts):
    try:
        contact_id = int(input("Введите ID контакта для удаления: "))
        for i, contact in enumerate(contacts):
            if contact["id"] == contact_id:
                del contacts[i]
                print("Контакт успешно удален.")
                return
        print("Контакт с таким ID не найден.")
    except ValueError:
        print("Неверный формат ID.")

# Главное меню
def main_menu():
    print("\n📞 Телефонный справочник")
    print("1. Показать все контакты")
    print("2. Добавить контакт")
    print("3. Поиск контакта")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Сохранить и выйти")
    print("7. Выйти без сохранения")
    choice = input("Выберите действие (1-7): ")
    return choice

# Основная функция
def main():
    contacts = load_contacts()
    changed = False

    while True:
        choice = main_menu()
        match choice:
            case "1":
                show_all_contacts(contacts)
            case "2":
                create_contact(contacts)
                changed = True
            case "3":
                find_contact(contacts)
            case "4":
                edit_contact(contacts)
                changed = True
            case "5":
                delete_contact(contacts)
                changed = True
            case "6":
                save_contacts(contacts)
                print("Выход из программы.")
                break
            case "7":
                print("Выход без сохранения.")
                break
            case _:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()