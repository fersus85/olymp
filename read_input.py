import json
from datetime import datetime


def load_competitors_from_json(path: str) -> list[dict[str, str]]:
    '''
    Функция для чтения из json файла.
    :param path: str путь к файлу
    :return: список словарей с данными
    '''
    with open(path, 'r', encoding='utf-8') as file:
        competitors = json.load(file)
    return competitors


def load_results_from_txt(path: str) -> dict[int, dict[str, datetime]]:
    '''
    Функция для чтения из txt файла.
    :param path: str путь к файлу
    :return: словарь с данными по каждому спортсмену
    '''
    results = {}
    with open(path, 'r', encoding='utf-8-sig') as file:
        for line in file:
            number, flag, time = line.strip().split()
            number = int(number)
            if flag == 'start':
                start_time = datetime.strptime(time, "%H:%M:%S,%f")
                results.setdefault(number, {}).update(start=start_time)
            elif flag == 'finish':
                fin_time = datetime.strptime(time, "%H:%M:%S,%f")
                results.setdefault(number, {}).update(finish=fin_time)
    return results
