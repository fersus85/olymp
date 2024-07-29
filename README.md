# Olympic script.
Python-скрипт, предназначенная для парсинга данных из файлов, обработки их и сохранения в новый файл. Выполнено по ТЗ, см. TZ.md

## Стек
python = "3.9"
встроенные библиотеки python

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/fersus85/olymp.git
    ```
2. Перейдите в директорию проекта:
    ```bash
    cd olymp
    ```
3. Создайте виртуальное и активируйте окружение:
  ```bash
    python3.9 -m venv venv
    source venv/bin/activate
  ```

## Запуск
  ```bash
  python3.9 -m script.main
  ```

## Запуск тестов
  ```bash
  python3.9 -m unittest discover -s script/tests
  ```
