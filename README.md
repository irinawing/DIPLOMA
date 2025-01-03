# Сравнительный анализ библиотек визуализации данных: Matplotlib, Seaborn и Plotly
В современном мире визуализация данных становится критически важным инструментом для анализа и интерпретации информации. Визуализация данных — это графическое представление информации и аналитики: графики, диаграммы, карты, дашборды. Цифры в таблицах и документах не показывают наглядно взаимосвязи между процессами, периоды роста или спада, зависимости показателей. Визуальный формат представляет информацию и вырисовывает цельную картину происходящего. Когда за обилием цифр легко утратить смысл, стоит обратиться к визуализации больших данных. Этот инструмент приводит огромное количество информации в порядок, помогает быстрее понимать её, подчёркивает тренды. В бизнесе визуализация помогает на многих этапах — от кадровых решений до предоставления скидки конкретному покупателю.

Этот проект направлен на сравнительный анализ трех популярных библиотек визуализации данных в Python: Matplotlib, Seaborn и Plotly. 
Мы изучим их возможности, особенности и различия, а также сделаем выводы по выбору наиболее подходящей библиотеки для различных задач.

## Цели и задачи работы

**Основная цель работы:** Провести сравнительный анализ библиотек визуализации данных Matplotlib, Seaborn и Plotly.

**Задачи работы:**
- Изучить функциональность каждой из библиотек.
- Создать две-три визуализации на одном наборе данных для сопоставимости.
- Провести сравнительный анализ визуализаций по критериям эстетики, информативности и удобства использования.
- Подготовить рекомендации по выбору библиотеки в зависимости от потребностей пользователя.
- Выводы.

## Краткий обзор библиотек

### Matplotlib
- **Описание:** Одна из самых популярных библиотек для статической визуализации данных в Python.
- **Основные особенности:** Гибкость в кастомизации графиков, поддержка различных типов визуализаций.
- **Области применения:** Научные исследования, инженерия, создание статических отчетов.

### Seaborn
- **Описание:** Библиотека, построенная на основе Matplotlib, упрощает создание статистических графиков.
- **Основные особенности:** Встроенные стили и палитры, поддержка визуализации статистических данных.
- **Области применения:** Научные исследования, анализ данных.

### Plotly
- **Описание:** Библиотека для создания интерактивных графиков, доступных через веб-браузер.
- **Основные особенности:** Поддержка интерактивности и анимации, возможность создания 3D визуализаций.
- **Области применения:** Бизнес-аналитика, веб-разработка, создание интерактивных отчетов.

## Функциональность библиотек

### Matplotlib
- Создание различных типов графиков (линейные, столбчатые, 3D и др.).
- Обширные возможности настройки всех элементов графиков.
- Поддержка сохранения графиков в различных форматах.

### Seaborn
- Упрощение создания статистических графиков.
- Уменьшено количество необходимого кода.
- Реализован внутренний механизм Pandas для работы с данными.
- Удобные предустановленные стили и шаблоны.
- Предустановленные стили для более привлекательных графиков, что упрощает дизайн.

### Plotly
- Создание интерактивных графиков с возможностью интеграции с веб-приложениями.
- Поддержка 3D графиков и карт.

## Примеры визуализаций

### Пример 1: Matplotlib
![image](https://github.com/user-attachments/assets/7bb23165-835d-4c5e-bff1-532907226046)

### Примеры 2: Seaborn
![image](https://github.com/user-attachments/assets/38adb446-be0f-42ab-8440-8d9d5447d0db)
![image](https://github.com/user-attachments/assets/66bec675-6bfe-4893-8e59-d862e05e6fc5)


### Примеры 3: Plotly
![image](https://github.com/user-attachments/assets/4321846b-9b8f-4126-b06d-af03d0d6bca4)
![image](https://github.com/user-attachments/assets/310879a8-81b1-41e8-83ff-ee041264fbc3)
![image](https://github.com/user-attachments/assets/f904128e-957b-4930-9ffd-eec451e3888d)


## Рекомендации по выбору библиотеки

- **Matplotlib:** Для высококачественных статических графиков и сложных визуализаций.
- **Seaborn:** Для удобного создания статистических графиков и работы с Pandas.
- **Plotly:** Для интерактивных графиков и визуализаций, требующих взаимодействия с пользователем.

## Заключение

Каждая из библиотек имеет свои сильные и слабые стороны.

Matplotlib подходит для любых статических графиков, но требует тщательного кодирования всех параметров визуализации.

Seaborn — для статистических визуализаций, не требует большого количество кода, отлажены стили, много готовых шаблонов цветовой палитры. 

Plotly — для интерактивных графиков, в основном используется в веб-приложениях.


## Установка

pip install matplotlib 

pip install seaborn 

pip install plotly

pip install pandas


### DataSet setup

from ucimlrepo import fetch_ucirepo

wine = fetch_ucirepo(id=109)

X = wine.data.features

y = wine.data.targets

print(wine.metadata)

print(wine.variables)


## Источники

Python для сложных задач. Наука о данных. 2-е междунар. изд. / Плас Вандер Джейк — Астана: "Спринт Бук", 2024. — 592 с.


https://matplotlib.org/

https://seaborn.pydata.org/

https://plotly.com/python/


https://blog.skillfactory.ru/glossary/matplotlib/

https://blog.skillfactory.ru/glossary/seaborn/

https://blog.skillfactory.ru/vizualizatsiya-dannyh-v-python-s-pomoschyu-plotly/
