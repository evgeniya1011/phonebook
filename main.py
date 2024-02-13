from utils import TXTSaver


def user_interaction(phonebook_saver: TXTSaver):
    """
    Функция взаимодействия с пользователем

    :param phonebook_saver: Экземпляр класса TXTSaver для сохранения и загрузки данных.
    """
    contacts = phonebook_saver.load_records()
    while True:
        print('Выберие одно из доступных действий:')
        print('1. Вывести постраничный список контактов')
        print('2. Добавить контакт')
        print('3. Отредактировать контакт')
        print('4. Поиск контакта')
        print('5. Выйти')

        user_input = input('> ')
        if user_input == '1':
            page = int(input('Введите номер страница: '))
            phonebook_saver.display_contacts(contacts, page)
        elif user_input == '2':
            phonebook_saver.add_record(contacts)
            print('Контакт успешно добавлен')
        elif user_input == '3':
            family_input = input('Введите фамилию контакта для редактирования: ')
            phonebook_saver.update_record(contacts, family_input)
        elif user_input == '4':
            search_word = input('Введите организацию: ')
            contacts = phonebook_saver.load_records()
            for contact in contacts:
                if search_word in contact['employer'].lower():
                    print(contact)
        elif user_input == '5':
            break
        else:
            print('Неккоректный ввод')


if __name__ == '__main__':
    txt_saver = TXTSaver()
    user_interaction(txt_saver)
