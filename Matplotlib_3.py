import pandas as pd
from matplotlib import pyplot as plt

class Graph:
    def __init__(self, title, x_label, y_label, x_data, y_data):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.x_data = x_data
        self.y_data = y_data

    def plot(self):
        # Устанавливаем размер гарфика
        plt.figure(figsize=(10, 6))
        # Рисуем график согласно переданным переменным х и у
        plt.pie(self.y_data, labels=self.x_data, autopct='%1.1f%%')
        # Название графика
        plt.title(self.title)
        # Рисуем график
        plt.show()

# Пример использования класса
if __name__ == "__main__":

    # Загружаем датасет Currency_Rates в массив pandas
    # Ссылка на файл в проекте
    url = "https://raw.githubusercontent.com/irinawing/DIPLOMA/refs/heads/main/Exchange_Rates.csv"
    # Описание столбцов файла
    columns = ['id','Country','Year','Series','Currency','Value']
    # загрузка массива данных
    rates = pd.read_csv(url, header = 1, names=columns)

    # Определяем выбор данных (фильтрум данные 2005 года)
    subset = rates[rates['Year'] == 2005]

    # Строим график, передаем необходимые переменные
    graph = Graph(title="Курс Валют 2005", x_label="Страна", y_label="USD to RUB", x_data=subset['Country'], y_data=subset['Value'])

    # Выводим график
    graph.plot()
