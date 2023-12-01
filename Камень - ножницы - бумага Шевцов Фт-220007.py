import random
import logging
from datetime import datetime

# Настройка логгера
logging.basicConfig(filename='game_log.log', level=logging.INFO)

# Функция для получения выбора пользователя
def get_user_choice():
    user_choice = input("Выберите камень (к), ножницы (н) или бумагу (б): ").lower()
    if user_choice not in ['к', 'н', 'б']:
        logging.error(f"{datetime.now()} - Неправильный ввод: {user_choice}")
        print("Неправильный ввод! Попробуйте еще раз.")
        return get_user_choice()
    return user_choice

# Функция для получения выбора компьютера
def get_computer_choice():
    return random.choice(['к', 'н', 'б'])

# Функция для определения победителя
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья"
    elif (user_choice == 'к' and computer_choice == 'н') or (user_choice == 'н' and computer_choice == 'б') or (user_choice == 'б' and computer_choice == 'к'):
        return "Вы выиграли!"
    else:
        return "Вы проиграли."

# Основная функция игры
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    logging.info(f"{datetime.now()} - Пользователь выбрал: {user_choice}, Компьютер выбрал: {computer_choice}, Результат: {result}")
    print(f"Компьютер выбрал: {computer_choice}")
    print(result)

# Запуск игры
play_game()
