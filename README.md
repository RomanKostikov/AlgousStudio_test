# Тестовое задание от AlgousStudio

## ТЗ для позиции VFX Technical Engineer

### Задача:
1.	Создать кнопку в Blender, при нажатии на которую будет происходить:
•	Сохранение текущей сцены Blender.
•	Отправка POST-запроса на API Django-сервера, содержащего следующую информацию:
•	Имя пользователя.
•	Время сохранения.
•	Путь к сохраненному файлу на диске.
2.	Развернуть Django-приложение на бесплатном VPS-сервере, которое:
•	Принимает реквест от Blender и сохраняет данные (имя пользователя, время, путь к файлу) в базу 
данных.
•	Предоставляет интерфейс админки, где можно увидеть записи из базы данных.

### Шаги выполнения:
1.	Blender:
•	Установите Blender, если он у вас не установлен: Blender Download.
•	Ознакомьтесь с документацией по написанию скриптов на Python для Blender: Blender Python API.
2.	VPS:
•	Зарегистрируйтесь и получите бесплатный VPS сервер на одной из платформ:
•	Heroku
•	AWS Free Tier
•	Google Cloud Free Tier
•	DigitalOcean (с бесплатным кредитом)
•	Настройте Docker и разверните Django-приложение, которое принимает POST-запросы и сохраняет 
данные в базу данных.

### Требования:
•	Blender: Напишите скрипт на Python, который добавляет кнопку в интерфейс Blender. При нажатии 
кнопки должна сохраняться текущая сцена, а затем отправляться POST-запрос с данными на API Django.
•	Django API: Разверните Django-приложение с REST API на вашем VPS. Реализуйте прием POST-запроса
и сохранение данных в базу данных.
•	Docker: Разверните ваше Django-приложение в Docker-контейнере на VPS.
•	База данных: Любая поддерживаемая Django база данных (SQLite, PostgreSQL, MySQL и т.д.).

### Ожидаемые результаты:
1.	GitHub-репозиторий, содержащий:
•	Скрипт для Blender, который можно установить и протестировать.
•	Dockerfile и инструкции для развертывания Django-приложения.
2.	Адрес и доступ к вашему Django-серверу:
•	URL, по которому можно проверить работу API.
•	Доступ к админке Django для проверки сохраненных данных.

### Критерии оценки:
•	Корректная работа кнопки в Blender (сохранение сцены и отправка реквеста).
•	Правильная работа Django API (прием данных и их запись в базу).
•	Прозрачная и простая установка и запуск как Blender-скрипта, так и Django-приложения.
•	Соответствие задания техническим требованиям.

### Полезные ссылки:
•	Blender Download
•	Blender Python API Documentation
•	Django Documentation
•	Docker Documentation
•	[VPS options (Heroku, AWS, Google Cloud, DigitalOcean)](https://www.heroku.com/, 
https://aws.amazon.com/free/, https://cloud.google.com/free, https://www.digitalocean.com/free)

## Решение:

### Инструкции по локальному запуску Django-приложения и настройке кнопки в Blender:

#### 1. Запуск Django-приложения локально

Шаг 1: Клонируйте репозиторий:
Скопируйте репозиторий с Django-приложением на локальный компьютер:
```bash
git clone <URL вашего репозитория>
cd <папка_проекта>
```