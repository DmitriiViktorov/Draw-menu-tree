# Тестовое задание UpTrader

Это приложение - моя реализация тестового задания на должность Junior Python Backend Developer

Вот текст тестового задания:
https://docs.google.com/document/d/1XTnbcXhejyGB-I2cHRiiSZqI3ElHzqDJeetwHkJbTa8/edit

## Установка

Для запуска приложение необходимо выполнить несколько шагов, описанных далее

### Шаги установки:

1. **Клонирование репозитория:**
   
   Для установки необходимо клонировать репозиторий с помощью следующей команды:
   ```bash
   git clone https://github.com/DmitriiViktorov/Draw-menu-tree.git
   ```

2. **Установка зависимостей**
   
   Создайте виртуальное окружение и установите зависимости:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
   pip install -r requirements.txt
    ```

3. **Выполните миграции**

   Перейдите в директорию с проектом и примените миграции для настройки базы данных:

   ```bash
   cd draw_menu_tree/
   python manage.py makemigrations
   python manage.py migrate
    ```
   
4. **Заполнение базы данных (опционально)**
   Для ускорения знакомства с данным приложением существует 2 способа заполнить базу данных стартовыми значениями.


   - Запустить команду, которая создаст набор связанных меню и подменю в базе данных
  
      ```bash
      python manage.py fill_db
      ``` 
   - Загрузить данные в базу из приложенного json файла.
      ```bash
      python manage.py loaddata menu_item.json
      ```   
   
5. **Запуск сервера**
   
   ```bash
   python manage.py runserver
   ```

    После успешного запуска сервис будет доступен по адресу http://127.0.0.1:8000/


## Подробности работы приложения

Для отображения древовидной структуры меню используются templatetags {% draw_menu %}. Для формирования набора данных для отрисовки меню 
используется 1 запрос к базе. Каждый пункт меню при нажатии отображает меню относительно этого элемента.
Из дополнительных модулей установлен django-debug-toolbar. Весь код выполнен только с использованием Django и Python без дополнительных библиотек.

## Пример работы приложения

![menu_example](/draw_menu_tree/media/Menu_01.png)

## Контактная информация

В случае возникновения вопросов, комментариев, замечаний по работе приложения вы можете связаться со мной:
- Email: viktorovokrl@gmail.com
- Github: https://github.com/DmitriiViktorov/twitter
- Telegram: https://t.me/ViktorovDV

