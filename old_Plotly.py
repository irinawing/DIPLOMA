import pandas as pd
import scipy

# Загружаем датасет Wine в массив pandas
url = "https://archive.ics.uci.edu/static/public/109/data.csv"
columns = ['Alcohol','Malicacid','Ash','Alcalinity_of_ash','Magnesium','Total_phenols','Flavanoids','Nonflavanoid_phenols','Proanthocyanins','Color_intensity','Hue','0D280_0D315_of_diluted_wines','Proline','class']
wine = pd.read_csv(url, header = 1, names=columns)
# display(wine)

# Визуализация с использованием Plotly

import plotly.express as px
from plotly.figure_factory import create_distplot

# Визаулизация гистограммы (распределения Гаусса)
fig = px.histogram(wine, x='Alcohol', color='class', barmode='overlay', title='Гистограмма Вин - Plotly',
                   labels={'Alcohol': 'Крепость вина в градусах', 'count': 'Частота'})

fig.update_layout(xaxis_title='Крепость вина в градусах', yaxis_title='Частота')
fig.show()

# Визаулизация гистограммы (с кривой распределения Гаусса)
group_labels = ['Частота']
x = [wine.Alcohol]
fig = create_distplot(x, group_labels, curve_type='normal')
fig.update_layout(xaxis_title='Крепость вина в градусах', yaxis_title='Частота')
fig.show()

# Визаулизация Круговой диагармы в красных тонах
import plotly.express as px
fig = px.pie(wine, values='Alcohol', names='class', color_discrete_sequence=px.colors.sequential.RdBu)
fig.show()