"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low_limit=1
    high_limit=101
    
    while True:
        count += 1
        predict_number = np.random.randint(low_limit, high_limit)  # предполагаемое число
        if predict_number<number:
            low_limit=predict_number 
            #если число меньше загаданного, диапазон генерируемого числа сужается слева
        if predict_number>number:
            high_limit=predict_number    
            #если число больше загаданного, диапазон генерируемого числа сужается справа       
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ( int ): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #список, содержащий кол-ва попыток для каждого загаданного числа в массиве (1000)
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
