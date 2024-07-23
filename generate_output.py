from datetime import timedelta, datetime


def calculate_durations(
        results: dict[int, dict[str, datetime]]) -> dict[int, timedelta]:
    '''
    Функция для вычисления времени прохождения дистанции.
    :param results: dict словарь с результатами спортсменов
    :return: словарь с номером спортсмена и временем прохождения дистанции
    '''
    durations = {}
    for number, times in results.items():
        duration = times['finish'] - times['start']
        durations[number] = duration
    return durations


def generate_output(competitors: dict[str, dict[str, str]],
                    durations: dict[int, timedelta]) -> list[dict[str, str]]:
    '''
    Функция для генерации выходных данных.
    :param competitors: dict словарь с номером и фио спортсмена
    :param durations: dict словарь с номером и результатом спортсмена
    :return: отсортированный список словарей с финальными данными
    '''
    output = []
    for number, fio in competitors.items():
        number = int(number.strip('\ufeff'))
        try:
            result_time = durations[number]
        except KeyError:
            continue
        output.append({
            'number': number,
            'name': fio['Name'],
            'surname': fio['Surname'],
            'result': result_time
        })
    output.sort(key=lambda x: x['result'])
    return output
