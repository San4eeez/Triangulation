<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Triangulation Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #f4f4f4;
            padding: 5px;
            border-radius: 3px;
            display: block;
            margin: 10px 0;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 3px;
            overflow: auto;
        }
    </style>
</head>
<body>
    <h1>Triangulation Tool</h1>
    <p>Triangulation Tool — это инструмент для визуализации и расчета координат устройства на основе данных от трех башен. Проект написан на Python с использованием библиотеки Tkinter для создания графического интерфейса.</p>

    <h2>Содержание</h2>
    <ul>
        <li><a href="#установка">Установка</a></li>
        <li><a href="#использование">Использование</a></li>
        <li><a href="#структура-проекта">Структура проекта</a></li>
        <li><a href="#лицензия">Лицензия</a></li>
    </ul>

    <h2 id="установка">Установка</h2>
    <ol>
        <li>Убедитесь, что у вас установлен Python 3.x.</li>
        <li>Скачайте или клонируйте репозиторий:
            <pre><code>git clone https://github.com/ваш-пользователь/triangulation-tool.git
cd triangulation-tool</code></pre>
        </li>
        <li>Установите необходимые зависимости (если есть):
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>

    <h2 id="использование">Использование</h2>
    <ol>
        <li>Запустите приложение, выполнив команду:
            <pre><code>python main.py</code></pre>
        </li>
        <li>В открывшемся окне вы увидите карту с тремя башнями и устройством. Вы можете перетаскивать башни и устройство мышью.</li>
        <li>Введите координаты и радиусы башен в соответствующие поля и нажмите кнопку "Update Towers" для обновления параметров.</li>
        <li>Нажмите кнопку "Calculate Coordinates" для расчета координат устройства.</li>
    </ol>

    <h2 id="структура-проекта">Структура проекта</h2>
    <p>Проект состоит из нескольких файлов:</p>
    <ul>
        <li><code>main.py</code>: Точка входа в приложение.</li>
        <li><code>triangulation_app.py</code>: Основной класс приложения, который управляет пользовательским интерфейсом и логикой.</li>
        <li><code>tower.py</code>: Класс для представления башни.</li>
        <li><code>device.py</code>: Класс для представления устройства.</li>
        <li><code>utils.py</code>: Вспомогательные функции для триангуляции.</li>
    </ul>
</body>
