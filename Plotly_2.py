import pandas as pd
import plotly.express as px

class Graph:
    def __init__(self, title, x_label, y_label, x_data, y_data):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.x_data = x_data
        self.y_data = y_data

    def plot(self):
        # Рисуем график согласно переданным переменным х и у
        fig = px.bar(x=self.x_data, y=self.y_data)
        # Передаем название графикаб наменование осей х и у
        fig.update_layout(title=self.title, xaxis_title=self.x_label, yaxis_title=self.y_label)
        # Рисуем график
        fig.show()

# Запускаем код
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
    # print(subset['Country'], subset['Value'])

    # Строим график, передаем необходимые переменные
    graph = Graph(title="Курс Валют 2005", x_label="Страна", y_label="USD to RUB", x_data=subset['Country'], y_data=subset['Value'])

    # Выводим график
    graph.plot()