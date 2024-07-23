import json


def display_output(data: list[dict[str, str]]) -> None:
    '''
    Функция для отображения на экране результатов соревнований
    '''
    print(f"| {'Занятое место':^15} | {'Нагрудный номер':^15} | {'Имя':^15} | {'Фамилия':^15} | {'Результат':^15} |")
    print("| --------------- | --------------- | --------------- | --------------- | --------------- |")
    for i, result in enumerate(data, start=1):
        print(f"| {i:^15} | {result['number']:^15} | {result['surname']:^15} | {result['name']:^15} | {result['result'][2:-4].replace('.', ','):^15} |")


def save_results_in_json(results: list[dict[str, str]], path: str) -> None:
    '''
    Функция сохраняет результаты соревнований в json файл
    :param results: список с итоговыми данными
    :param path: str путь для сохранения файла
    '''
    save_dict = {}
    for i, result in enumerate(results, start=1):
        save_dict[str(i)] = {
            "Нагрудный номер": str(result['number']),
            "Имя": result['surname'],
            "Фамилия": result['name'],
            "Результат": result['result']
        }
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(save_dict, file, ensure_ascii=False, indent=4)
