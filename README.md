# Final_project

## Финальный проект по автоматизации тестирования

### Шаги
1. Склонировать проект `git clone https://github.com/Marina170220/Final_project.git`
2. Для авторизации на сайте необходимо получение кода на телефон. На главной странице сайта вводим номер телефона, вводим полученный код и авторизуемся на сайте. С помощью инструментов разработчика находим токен в разделе Приложение-> Файлы cookie-> BK_ACCESS_TOKEN.
Полученный токен необходимо добавить в файл с тестовыми данными test_data.json в качестве значения для ключа "token".
Обратите внимание, время действия токена ограничено!
2. Установить все зависимости `pip install -r requirements.txt`
3. Запустить тесты `python -m pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- allure
- configparser
- json

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./config - провайдер настроек
    - test_config.ini - настройки для тестов
- ./test_data - провайдер тестовых данных
    - test_data.json

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/cheat-sheet/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)
- [Про configparser](https://docs.python.org/3/library/configparser.html#module-configparser)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)
