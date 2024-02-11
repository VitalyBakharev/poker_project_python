import sqlite3

# Функция для создания базы данных и таблицы, если их нет
def create_database():
    connection = sqlite3.connect('poker_recommendations.db')
    cursor = connection.cursor()

    # Создание таблицы, если ее нет
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            position TEXT,
            hand TEXT,
            recommendation TEXT
        )
    ''')

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

# Функция для добавления записи в таблицу
def insert_recommendation(position, hand, recommendation):
    connection = sqlite3.connect('poker_recommendations.db')
    cursor = connection.cursor()

    # Вставка данных в таблицу
    cursor.execute('''
        INSERT INTO recommendations (position, hand, recommendation)
        VALUES (?, ?, ?)
    ''', (position, hand, recommendation))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

# Пример использования
create_database()

# Предположим, у вас есть позиция, рука и рекомендация
position = "utg"
hand = "AK"
recommendation = "fold"

# Добавляем запись в базу данных
insert_recommendation(position, hand, recommendation)

print("Запись добавлена в базу данных.")

