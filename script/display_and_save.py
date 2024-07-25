import json
import logging


logger = logging.getLogger(__name__)


def display_output(data: list[dict[str, str]]) -> None:
    """
    Функция для отображения на экране результатов соревнований
    """
    print(
        f"| {'Занятое место':^15} | {'Нагрудный номер':^15} | "
        f"{'Имя':^15} | {'Фамилия':^15} | {'Результат':^15} |"
    )
    print(
        "| --------------- | --------------- | --------------- | "
        " -------------- | --------------- |"
    )
    for i, result in enumerate(data, start=1):
        try:
            result_str = (
                f"| {i:^15} | {result['number']:^15} | {result['name']:^15} | "
                f"{result['surname']:^15} | "
                f"{result['result'][2:-4].replace('.', ','):^15} |"
            )
            print(result_str)
        except KeyError as ex:
            logger.error(f"Key missing trying parse data for displaying: {ex}")
            continue


def save_results_in_json(results: list[dict[str, str]], path: str) -> None:
    """
    Функция сохраняет результаты соревнований в json файл
    :param results: список с итоговыми данными
    :param path: str путь для сохранения файла
    """
    logger.info("Save output in file")
    save_dict = {}
    for i, result in enumerate(results, start=1):
        try:
            save_dict[str(i)] = {
                "Нагрудный номер": str(result["number"]),
                "Имя": result["surname"],
                "Фамилия": result["name"],
                "Результат": result["result"],
            }
        except KeyError as ex:
            logger.warning(f"Key does not exist {ex}")
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(save_dict, file, ensure_ascii=False, indent=4)
    except FileExistsError as ex:
        logger.error(f"Error {ex}")
    except IOError as ex:
        logger.error(f"Error i/a {ex}")
