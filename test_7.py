# from datetime import datetime

# def data_obj(d):
#     # current_day = "2024.12.06"
#     if datetime.strptime(d, "%Y.%m.%d"):
#         d = datetime.strptime(d, "%Y.%m.%d")
#         return d

#     else:
    
#         print('Дата не по шаблону')
    

# print(data_obj("2022.01.12"))



# def string_to_date(date_string):
#     # date = datetime.strptime(date_string, "%Y.%m.%d")
  
#     # return datetime.date(date)
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def date_to_string(date):
#     date_string = datetime.strftime(date, "%Y.%m.%d")
#     return date_string

# date_string = "2024.01.01"
# converted_date = string_to_date(date_string)
# print(converted_date)
# date_string = date_to_string(converted_date)
# print(date_string)



# from datetime import datetime

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def prepare_user_list(user_data):
#     for el in user_data:
#         el["birthday"] = string_to_date(date_string=el["birthday"])
#     return user_data
        
# users = [
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.3.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# prepared_users = prepare_user_list(users)
# print(prepared_users)


# from datetime import datetime

# def string_to_date(date_string):
#     # date = datetime.strptime(date_string, "%Y.%m.%d")
  
#     # return datetime.date(date)
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def find(date):
#     return string_to_date(date).weekday()

# def date_to_string(date):
#     date_string = datetime.strftime(date, "%Y.%m.%d")
#     return date_string

# date_string = "2024.01.01"
# converted_date = string_to_date(date_string)
# print(converted_date)
# day = find(date_string)
# print(day)
# # date_string = date_to_string(converted_date)
# # print(date_string)



# from datetime import datetime, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def find_next_weekday(start_date, weekday):
#     day_start_date = start_date.weekday()
#     if weekday - day_start_date <= 0:
#         return start_date + timedelta(weekday - day_start_date + 7)
#     else:
#         return start_date + timedelta(weekday - day_start_date)
    
        
# start_date = string_to_date("2024.03.26")  # Перетворення рядка на дату
# next_monday = find_next_weekday(start_date, 0)  # Знайти наступний понеділок
# print(next_monday)
# next_friday = find_next_weekday(start_date, 4)  # Знайти наступну п'ятницю
# print(next_friday)
    

# from datetime import datetime, date


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")

# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     print(prepared_list)
#     return prepared_list

# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = string_to_date("2024.12.30")

#     for user in users:
#         birthday_this_year = user["birthday"].replace(year=today.year)
#         if birthday_this_year < today:
#             birthday_this_year = user["birthday"].replace(year=today.year + 1)

#         """
#         Додайте на цьому місці перевірку, чи не буде 
#         припадати день народження вже наступного року.
#         """
        
            

#         if 0 <= (birthday_this_year - today).days <= days:
#             """ 
#             Додайте перенесення дати привітання на наступний робочий день,
#             якщо день народження припадає на вихідний. 
#             """
            

#             congratulation_date_str = date_to_string(birthday_this_year)
#             upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
#     return upcoming_birthdays

# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Bob", "birthday": "1985.12.31"},
#     {"name": "Bib", "birthday": "1985.01.01"}
# ]
# prepared_users = prepare_user_list(users)
# print(get_upcoming_birthdays(prepared_users))


# from datetime import datetime, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()      

# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)

# def adjust_for_weekend(birthday):
#     if birthday.weekday() >= 5:
#         birthday = find_next_weekday(birthday, 0)
#         return birthday
#     else:
#         return birthday


# from datetime import datetime, date, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")

# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     print(prepared_list)
#     return prepared_list

# def find_next_weekday(start_date, weekday):
#     day_start_date = start_date.weekday()
#     if weekday - day_start_date <= 0:
#         return start_date + timedelta(weekday - day_start_date + 7)
#     else:
#         return start_date + timedelta(weekday - day_start_date)
    
# def adjust_for_weekend(birthday):
#     if birthday.weekday() >= 5:
#         birthday = find_next_weekday(birthday, 0)
#         return birthday
#     else:
#         return birthday

# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#     for el in users:
#         el["birthday"] = el["birthday"].replace(year=today.year)
#         if 0 < (el["birthday"] - today).days < days:
#             upcoming_birthdays.append({"name": el["name"], "congratulation_date": date_to_string(el["birthday"])})   
#     return upcoming_birthdays

# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Bob", "birthday": "1985.12.10"},
#     {"name": "Bib", "birthday": "1985.12.15"}
# ]

"""

"""


# from datetime import datetime, date, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")

# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list

# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)

# def adjust_for_weekend(birthday):
#     if birthday.weekday() >= 5:
#         return find_next_weekday(birthday, 0)
#     return birthday

# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#     for user in users:
#         birthday_this_year = user["birthday"].replace(year=today.year)
#         if birthday_this_year < today:
#             birthday_this_year = user["birthday"].replace(year=today.year + 1)
#         if 0 <= (adjust_for_weekend(birthday_this_year) - today).days <= days:
#             congratulation_date_str = date_to_string(adjust_for_weekend(birthday_this_year))
#             upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
#     return upcoming_birthdays


# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Bob", "birthday": "1985.12.31"},
#     {"name": "Bib", "birthday": "1985.01.01"},
#     {"name": "Jeck", "birthday": "1985.01.04"},
#     {"name": "Deniels", "birthday": "1985.12.29"}
# ]
# prepared_users = prepare_user_list(users)
# print(get_upcoming_birthdays(prepared_users))



from collections import UserDict
from datetime import datetime, date, timedelta

class Field:
    def __init__(self, value):
        self.value = value
        # print(value)

    def __str__(self):
        # print(str(self.value))
        return str(self.value)

class Name(Field):
    pass
    
class Phone(Field): 
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError

    def __str__(self):
        return str(self.value)
    
class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            value = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    birthday_list = []

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    
    def add_phone(self, value):
        self.phones.append(Phone(value))

    def add_birthday(self, value):
        self.birthday = Birthday(value)
        Record.birthday_list.append({"name": self.name.value, "birthday": self.birthday.value})

    def remove_phone(self, value):
        self.phones = [p for p in self.phones if p.value != value]

    def edit_phone(self, old_phone, new_phone):
        if old_phone in (p.value for p in self.phones):
            self.phones = [p if p.value != old_phone else Phone(new_phone) for p in self.phones]
        else:
            raise ValueError

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
            else:
                None
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

class AddressBook(UserDict):  
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name) -> Record:
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def date_to_string(date):
        return date.strftime("%d.%m.%Y")
   
    def find_next_weekday(start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    def adjust_for_weekend(birthday):
        if birthday.weekday() >= 5:
            return AddressBook.find_next_weekday(birthday, 0)
        return birthday

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = AddressBook.find_next_weekday(date.today(), 0)
        for el in Record.birthday_list:
            birthday_this_year = el["birthday"].replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = el["birthday"].replace(year=today.year + 1)
            if 0 <= (AddressBook.adjust_for_weekend(birthday_this_year) - today).days <= days:
                congratulation_date_str = AddressBook.date_to_string(AddressBook.adjust_for_weekend(birthday_this_year))
                upcoming_birthdays.append({"name": el["name"], "birthday": congratulation_date_str})
        return upcoming_birthdays
    
    def show_birthday(self, name):
        for el in Record.birthday_list:
            if el["name"] == name:
                return AddressBook.date_to_string(el.get("birthday"))
    
    def __str__(self):
        return f"Record in AddressBook:\n{("\n".join(el for el in self.data))}"
        
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("22.12.2000")
# john_record.add_phone(" 234567890")
book.add_record(john_record)
# print(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_birthday("16.12.1997")
book.add_record(jane_record)

# # Виведення всіх записів у книзі
# print(book.prepare_user_list())
john = book.find("John")

print(john)
# john.edit_phone("1234567890", "1112223333")
# print(jane_record)
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# # Видалення запису Jane
# # book.delete("Jane")
print(book.show_birthday("John"))
# print(Record.add_birthday())
print(book.get_upcoming_birthdays())