import json
from abc import ABC, abstractmethod


class MyEncoder(json.JSONEncoder):
    """
    Класс MyEncoder для кодирования пользовательских объектов в формат JSON.
    """
    def default(self, obj):
        """
        Переопределенный метод для обработки пользовательских объектов при сериализации.

        :param obj: Объект, который необходимо сериализовать.
        :return: Сериализованный объект или вызов базового метода, если невозможно сериализовать.
        """
        if isinstance(obj, str):
            return obj
        return super(MyEncoder, self).default(obj)


class TXTAbc(ABC):

    @abstractmethod
    def load_records(self) -> list:
        pass

    @abstractmethod
    def display_contacts(self, contacts: list, page: int, page_size: int) -> list:
        pass

    @abstractmethod
    def add_record(self, contacts: list) -> list:
        pass

    @abstractmethod
    def update_record(self, contacts: list, record: str) -> list:
        pass


class TXTSaver(TXTAbc):
    """Класс для сохранения, добавления и вывода контактов"""

    def load_records(self) -> list:
        """
            Загрузка данных из телефонного справочника.
        """
        try:
            with open('phonebook.txt', 'r', encoding='utf-8') as file:
                contacts = json.load(file)
                return contacts
        except FileNotFoundError:
            return []

    def display_contacts(self, contacts: list, page: int, page_size=4):
        """
            Выводит список контактов на указанной странице.

            :param contacts: Список контактов.
            :param page: Номер страницы для отображения.
            :param page_size: Количество контактов на странице (по умолчанию 4).
        """
        if contacts:
            start_i = (page-1)*page_size
            end_i = start_i + page_size
            for i, contact in enumerate(contacts[start_i:end_i], start=start_i + 1):
                print(i, contact)
        else:
            print('Список контактов пуст')

    def add_record(self, contacts: list):
        """
            Добавление записи в телефонный справочник.

            :param contacts: Список контактов.
        """
        name = input('Заполните имя: ')
        surname = input('Заполните отчество: ')
        family = input('Заполните фамилию: ')
        employer = input('Заполните название организации: ')
        phone_working = input('Заполните рабочий телефон: ')
        phone_personal = input('Заполните личный телефон: ')
        contact = {
            'name': name,
            'surname': surname,
            'family': family,
            'employer': employer,
            'phone_working': phone_working,
            'phone_personal': phone_personal,
        }
        contacts.append(contact)
        with open('phonebook.txt', 'a', encoding='utf-8') as file:
            json.dump(contacts, file, ensure_ascii=False, indent=2, cls=MyEncoder)

    def update_record(self, contacts: list, record: str):
        """
            Обновление данных в телефонном справочнике.

            :param contacts: Список контактов.
            :param record: Введнная фамилия контакта.
        """
        for contact in contacts:
            if contact['family'] == record:
                contact['name'] = input('Введите новое имя: ')
                contact['family'] = input('Введите новую фамилию: ')
                contact['surname'] = input('Введите новое отчество: ')
                contact['employer'] = input('Введите новую организацию: ')
                contact['phone_working'] = input('Введите новый рабочий телефон: ')
                contact['phone_personal'] = input('Введите новый личный телефон: ')

                with open('phonebook.txt', 'w', encoding='utf-8') as f:
                    json.dump(contacts, f, ensure_ascii=False, indent=2, cls=MyEncoder)
                    print('Контакт успешно изменен')
                    return
        print('Контакт с такой фамилией не найден')
