# API_tests_for_YandexDisk
Тестирование работы с файлами на YandexDisk через API
<br /> <br />

## Загрузка и настройка готового проекта
• Версия Python: 3.10

• После скачивания проекта к себе на компьютер не забудьте установить необходимые зависимости, прописав к консоли команду: 
<code>pip install requirements.txt</code>

• Для корректной работы проекта: 
1) Создайте приложение в Yandex перейдя по ссылке: <code>https://oauth.yandex.ru/client/new/</code>:
- Задайте любое название для вашего приложения
- В разделе "Платформы приложения" выберите "Веб-сервисы"
- в разделе "Доступ к данным" выберите следующие обязательные параметры: 
- -> Чтение всего Диска
- -> Запись в любом месте на Диске
- -> Доступ к информации о Диске
- Нажмите "Создать приложение"
2) Для корректной работы автотестов не забудьте создать файл ".env", куда поместите свои <code>CLIENT_ID</code> и <code>CLIENT_SECRET</code>. Если хотите скрыть свои личные данные, помещайти их в файл ".env", в ином случае, можете задать переменные в файле settings.py, а затем импортировать данный файл в файл, в котором собираетесь использовать необходимые переменные
3) Запустите скрипт "get_token.py" и полученный токен вставьте в поле [your token], находящееся в файле test_creating_a_folder.py
4) Можете запускать автотесты
<br /> <br />

## Работа с командами, запуск автотестов через консоль
• Для запуска всех существующих тестов в проекте: <code>pytest</code>
<br /> <br />
