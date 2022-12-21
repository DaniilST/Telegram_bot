# Система цифровой обработки изображений (Фотограм)
__⭐Проект участвует в конкурсе⭐ - команда "afaik"__

## :robot: Проект

На данный момент все редакторы изображений являются достаточно тяжеловесными, кроме того, большая часть из них является платными, что несет за собой дополнительные сложности по установке.

Разработанная система предназначена для тех людей, которые хотят быстро и бесплатно отредактировать свое изображение. 
Созданная система позволяет выполнять различные математические операции над изображениями, 
что позволит в конечном итоге получить отредактированное изображение.

## :robot: Технические детали
__Функциональность данного Телеграм-бота:__
1. Применение попиксельных операций над двумя изображениями.
2. Применение к выбранному изображению градационных преобразований:
   - Затемнение изображения.
   - Осветление изображения.
   - Негатив.
   - Повышения контрастности изображения.
3.Применение интерполяции к изображению.

__Используемый стек технологий:__
  1. Язык программирования Python.
  2. Бибилиотека AIOGram. Данная библиотека используется для разработки серверной части Telegram-бота.
  3. Библиотека NumPy. Данная библиотка позволяет оптимизировать роботу с математическим аппратом.
  4. Библиотека Matplotlib. Данная библиотека позволяет создавать графики.
  5. Библиотека Pillow. Данная библиотека позволяет работать с изображением.
  6. Консольная утилита Git. Данная утилита позволяет внедрить систему контроля версиями в проект.

## :robot: Развертывание проекта
1. Перейти в директорию ```/Telegram_bot```. 
2. Создать виртуальную среду. 
   ```
    python3 main.py
   ```
3. Активировать виртуальную среду, используя команду:<br>
   _Windows:_
   ``` 
   venv/Scripts/activate
   ```
   _Mac OS / Linux:_
   ``` 
   source mypython/bin/activate
   ```
   
4. Установить все пакеты, которые перечислены в файле _requirements.txt_. Для этого использовать команду:
   ```
   pip install -r requirements.txt
   ```
5. Создать файл _config.json_.
6. В файле _config.json_ создать переменные:<br>
__telegram_bot_token__ - содержит токен бота. Тип: __str__.<br>
__project_static_path__ - содержит путь к папке со статическими файлами. Тип: __str__
```json
{
  "telegram_bot_token": "token_bot",
  "project_static_path": "./data"
}
```
7. Запустить файл _main.py_, используя команду:
```
python main.py
```
## :robot: Пример работы проекта
__Пример:__ На видео ниже представлен пример применения интерполяции к изображению.

[🎥 Ссылка на демонстрационное видео.](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg")
## :robot: Состав команды
__Состав команды:__
1. Степанов Даниил ИДМ-22-01 (Роли: РП, СП, ВН, НИ, БА, АД, КО, ПП).

## :robot: Landing page
[Landing page](https://landing1-j90370996.6e7oz.landing.myjino.ru/)



