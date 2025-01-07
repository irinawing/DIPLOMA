# Сравнительный анализ библиотек визуализации данных: Matplotlib, Seaborn и Plotly
В современном мире визуализация данных становится критически важным инструментом для анализа и интерпретации информации. Визуализация данных — это графическое представление информации и аналитики: графики, диаграммы, карты, дашборды. Цифры в таблицах и документах не показывают наглядно взаимосвязи между процессами, периоды роста или спада, зависимости показателей. Визуальный формат представляет информацию и вырисовывает цельную картину происходящего. Когда за обилием цифр легко утратить смысл, стоит обратиться к визуализации больших данных. Этот инструмент приводит огромное количество информации в порядок, помогает быстрее понимать её, подчёркивает тренды. В бизнесе визуализация помогает на многих этапах — от кадровых решений до предоставления скидки конкретному покупателю.

Этот проект направлен на сравнительный анализ трех популярных библиотек визуализации данных в Python: Matplotlib, Seaborn и Plotly. 
Мы изучим их возможности, особенности и различия, а также сделаем выводы по выбору наиболее подходящей библиотеки для различных задач.

## Содержание

1. [Цели и задачи работы](#Цели-и-задачи)
2. [Краткий обзор библиотек](#Краткий-обзор-библиотек)
   - [1. Matplotlib](#Matplotlib)
   - [2. Seaborn](#Seaborn)
   - [3. Plotly](#Plotly)
4. [Пример визуализайций](#Примеры-визуализаций)
5. [Сравнение библиотек](#Сравнение-библиотек)
6. [Функциональность библиотек](#Функциональность-библиотек)
   - [1. Matplotlib](#Matplotlib(1))
   - [2. Seaborn](#Seaborn(1))
   - [3. Plotly](#Plotly(1))
7. [Заключение](#Заключение)
8. [Установка](#Установка)
9. [Источники](#Источники)

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
Пример использования для создания **столбчатой диаграммы**:
   ```python
   import matplotlib.pyplot as plt
   
   # Пример данных
   categories = ['A', 'B', 'C', 'D']
   values = [10, 20, 15, 30]
   
   plt.bar(categories, values)
   plt.title('Столбчатая диаграмма с Matplotlib')
   plt.show()

```
![image](https://github.com/user-attachments/assets/5ae236d7-aec8-442c-b33e-45ae08390885)

### Примеры 2: Seaborn
Пример использования для создания **линейного графика**:
   ```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

sns.lineplot(x=x, y=y)
plt.title("Линейный график (Seaborn)")
plt.show()

```
![image](https://github.com/user-attachments/assets/c49b91d5-150e-4e27-92c3-fcbf66b9cf61)

### Примеры 3: Plotly
Пример использования для создания **диаграммы рассеяния**:
   ```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 4, 9, 16, 25], mode='markers'))
fig.update_layout(title='Диаграмма рассеяния (Plotly)', xaxis_title='X', yaxis_title='Y')
fig.show()

```
![image](https://github.com/user-attachments/assets/6adb597c-4ba2-42e7-957f-dbc923fe9d1e)

## Рекомендации по выбору библиотеки

- **Matplotlib:** Для высококачественных статических графиков и сложных визуализаций.
- **Seaborn:** Для удобного создания статистических графиков и работы с Pandas.
- **Plotly:** Для интерактивных графиков и визуализаций, требующих взаимодействия с пользователем.

## Сравнение библиотек

| Особенность | Matplotlib	| Seaborn	| Plotly |
|-------------|------------|-----------|--------|
| Простота использования	| Средняя, требует параметры для кастомизации	| Высокая, очень удобно для работы с минимумом кода	| Очень высокая, простой синтаксис, поддержка интерактивности |
| Поддержка интерактивности (web разработки)	| Нет, нужны дополнительные библиотеки	| Нет	| Да |
| Типы графиков	| Все стандартные типы графиков	| Статистические графики	| Интерактивные (web) и 3D графики |
| Анимация	| Нет	| Нет	| Да, поддержка через динамические данные |
| Сложность графиков	| Высокая (много настроек)	| Низкая (готовые стили, функции и цветовые шаблны)	| Средняя (для базовых графиков) |
| Использование с Pandas	| Хорошо	| Отлично	| Хорошо |
| Настройка графиков	| Очень высокая	| Средняя	| Средняя |
| Производительность	| Хорошо для малых и средних объемов данных	| Хорошо для статистических графиков	| Хорошая, но может снижаться при работе с большими объемами данных |
| Визуальное оформление	| Базовое	| Очень красивое по умолчанию	| Высококачественное, но требует больше ресурсов |
| Подходит для	| Простейших и сложных графиков	| Статистических данных	| Интерактивных (web) и динамичных графиков, поддержка JavaScript |


## Заключение

Каждая из библиотек имеет свои сильные и слабые стороны.

**Matplotlib** подходит для любых статических графиков, но требует тщательного кодирования всех параметров визуализации.

**Seaborn** — для статистических визуализаций, не требует большого количество кода, отлажены стили, много готовых шаблонов цветовой палитры. 

**Plotly** — для интерактивных графиков, в основном используется в веб-приложениях.


## Установка

pip install matplotlib 

pip install seaborn 

pip install plotly

pip install pandas

## Источники

**Python для сложных задач. Наука о данных**. 2-е междунар. изд. / Плас Вандер Джейк — Астана: "Спринт Бук", 2024. — 592 с.


https://matplotlib.org/

https://seaborn.pydata.org/

https://plotly.com/python/


https://blog.skillfactory.ru/glossary/matplotlib/

https://blog.skillfactory.ru/glossary/seaborn/

https://blog.skillfactory.ru/vizualizatsiya-dannyh-v-python-s-pomoschyu-plotly/
