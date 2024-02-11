import sqlite3

def poker_recommender_from_db(position, hand):
    # Преобразование входных данных в нижний регистр
    position = position.lower()
    hand = hand.lower()

    # Подключение к базе данных
    connection = sqlite3.connect('poker_recommendations.db')
    cursor = connection.cursor()

    # Выборка рекомендации из базы данных
    cursor.execute('''
        SELECT recommendation FROM recommendations
        WHERE position=? AND hand=?
    ''', (position, hand))

    result = cursor.fetchone()

    # Закрываем соединение с базой данных
    connection.close()

    # Если запись найдена в базе данных, возвращаем рекомендацию
    if result:
        print("Данные найдены в базе данных.")
        return result[0]
    else:
        # В противном случае, используем стандартную логику
        print("Данные не найдены в базе данных. Используется стандартная логика.")
        return poker_recommender_default_logic(position, hand)

def poker_recommender_default_logic(position, hand):
    # Стандартная логика вашей функции
    valid_positions = {"utg", "utg+1", "utg+2", "lj", "hj", "co", "bu", "sb", "bb"}
    valid_hands = { ... }  # Ваш список рук

    # Логика определения рекомендации в зависимости от позиции и руки
    if position in {"sb", "bb"}:
        return "check"
    else:
        return "call"  # В остальных случаях - вызов

# Пример использования
position = input("Введите вашу позицию за столом: ")
hand = input("Введите ваши карты: ")

recommendation = poker_recommender_from_db(position, hand)
print("Рекомендация:", recommendation)
