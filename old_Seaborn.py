import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Загружаем датасет Wine в массив pandas
url = "https://archive.ics.uci.edu/static/public/109/data.csv"
columns = ['Alcohol','Malicacid','Ash','Alcalinity_of_ash','Magnesium','Total_phenols','Flavanoids','Nonflavanoid_phenols','Proanthocyanins','Color_intensity','Hue','0D280_0D315_of_diluted_wines','Proline','class']
wine = pd.read_csv(url, header = 1, names=columns)
# display(wine)

# Визуализация с использованием Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=wine, x='Alcohol', hue='class', bins=10, alpha=0.5, kde=False)

# Гистограмма - Seaborn
plt.title('Гистограмма Вин - Seaborn')
plt.xlabel('Крепость вина в градусах')
plt.ylabel('Частота повторений')
plt.grid(True)
plt.show()

# График оценки плоности ядра - Seaborn
plt.figure(figsize=(10, 6))
sns.kdeplot(data=wine, x='Alcohol', hue='class', multiple="stack")
plt.title('Оценка плотности ядра - Seaborn')
plt.xlabel('Крепость вина в градусах')
plt.ylabel('Частота повторений')
plt.grid(True)
plt.show()