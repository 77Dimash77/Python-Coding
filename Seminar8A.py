def create_contact_file():
    filename = 'contacts.txt'

    contacts = []
    while True:
        surname = input("Введите фамилию (или Enter для завершения): ")
        if not surname:
            break
        first_name = input("Введите имя: ")
        patronymic = input("Введите отчество: ")
        phone_number = input("Введите номер телефона: ")
        contact = f"{surname},{first_name},{patronymic},{phone_number}"
        contacts.append(contact)

    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(contact + '\n')

    print(f"Файл {filename} успешно создан с контактами.")


def display_contacts():
    filename = 'contacts.txt'  

    
    with open(filename, 'r') as file:
        contacts = file.readlines()

    print("Список контактов:")
    for contact in contacts:
        surname, first_name, patronymic, phone_number = contact.strip().split(',')
        print(f"Фамилия: {surname}, Имя: {first_name}, Отчество: {patronymic}, Телефон: {phone_number}")


def search_contacts():
    filename = 'contacts.txt' 

    search_criteria = input("Введите критерий для поиска (фамилию, имя, отчество или номер телефона): ")
    matching_contacts = []

    
    with open(filename, 'r') as file:
        contacts = file.readlines()

    for contact in contacts:
        surname, first_name, patronymic, phone_number = contact.strip().split(',')
        if search_criteria.lower() in (surname.lower(), first_name.lower(), patronymic.lower(), phone_number.lower()):
            matching_contacts.append(contact)

    
    if matching_contacts:
        print("Найденные контакты:")
        for contact in matching_contacts:
            surname, first_name, patronymic, phone_number = contact.strip().split(',')
            print(f"Фамилия: {surname}, Имя: {first_name}, Отчество: {patronymic}, Телефон: {phone_number}")
    else:
        print("Контакты с заданным критерием не найдены.")


def add_contact():
    filename = 'contacts.txt' 

    surname = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    contact = f"{surname},{first_name},{patronymic},{phone_number}"


    with open(filename, 'a') as file:
        file.write(contact + '\n')

    print("Контакт успешно добавлен.")


def edit_contact():
    filename = 'contacts.txt' 

    search_criteria = input("Введите критерий для поиска контакта (фамилию, имя, отчество или номер телефона): ")
    matching_contacts = []


    with open(filename, 'r') as file:
        contacts = file.readlines()

    for contact in contacts:
        surname, first_name, patronymic, phone_number = contact.strip().split(',')
        if search_criteria.lower() in (surname.lower(), first_name.lower(), patronymic.lower(), phone_number.lower()):
            matching_contacts.append(contact)

    
    if matching_contacts:
        print("Найденные контакты:")
        for i, contact in enumerate(matching_contacts):
            surname, first_name, patronymic, phone_number = contact.strip().split(',')
            print(f"{i + 1}. Фамилия: {surname}, Имя: {first_name}, Отчество: {patronymic}, Телефон: {phone_number}")

        contact_index = int(input("Введите номер контакта, который вы хотите редактировать: ")) - 1

        if 0 <= contact_index < len(matching_contacts):
            new_surname = input("Введите новую фамилию: ")
            new_first_name = input("Введите новое имя: ")
            new_patronymic = input("Введите новое отчество: ")
            new_phone_number = input("Введите новый номер телефона: ")

            matching_contacts[contact_index] = f"{new_surname},{new_first_name},{new_patronymic},{new_phone_number}"

            
            with open(filename, 'w') as file:
                for contact in matching_contacts:
                    file.write(contact)

            print("Контакт успешно отредактирован.")
        else:
            print("Некорректный номер контакта.")
    else:
        print("Контакты с заданным критерием не найдены.")


def delete_contact():
    filename = 'contacts.txt'  

    search_criteria = input("Введите критерий для поиска контакта (фамилию, имя, отчество или номер телефона): ")
    matching_contacts = []

    
    with open(filename, 'r') as file:
        contacts = file.readlines()

    for contact in contacts:
        surname, first_name, patronymic, phone_number = contact.strip().split(',')
        if search_criteria.lower() in (surname.lower(), first_name.lower(), patronymic.lower(), phone_number.lower()):
            matching_contacts.append(contact)

    
    if matching_contacts:
        print("Найденные контакты:")
        for i, contact in enumerate(matching_contacts):
            surname, first_name, patronymic, phone_number = contact.strip().split(',')
            print(f"{i + 1}. Фамилия: {surname}, Имя: {first_name}, Отчество: {patronymic}, Телефон: {phone_number}")

        contact_index = int(input("Введите номер контакта, который вы хотите удалить: ")) - 1

        if 0 <= contact_index < len(matching_contacts):
            
            deleted_contact = matching_contacts.pop(contact_index)

            with open(filename, 'w') as file:
                for contact in contacts:
                    if contact != deleted_contact:
                        file.write(contact)

            print("Контакт успешно удален.")
        else:
            print("Некорректный номер контакта.")
    else:
        print("Контакты с заданным критерием не найдены.")



create_contact_file()

while True:
    print("\nВыберите действие:")
    print("1. Просмотреть список контактов")
    print("2. Поиск контакта")
    print("3. Добавить новый контакт")
    print("4. Редактировать контакт")
    print("5. Удалить контакт")
    print("6. Выйти")

    choice = input("Введите номер действия: ")

    if choice == "1":
        display_contacts()
    elif choice == "2":
        search_contacts()
    elif choice == "3":
        add_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Программа завершена.")
        break
    else:
        print("Некорректный выбор.")
