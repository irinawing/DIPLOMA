import pandas as pd

# Загружаем датасет Wine в массив pandas
url = "https://archive.ics.uci.edu/static/public/109/data.csv"
columns = ['Alcohol','Malicacid','Ash','Alcalinity_of_ash','Magnesium','Total_phenols','Flavanoids','Nonflavanoid_phenols','Proanthocyanins','Color_intensity','Hue','0D280_0D315_of_diluted_wines','Proline','class']
wine = pd.read_csv(url, header = 1, names=columns)
# display(wine)

# Визуализация с использованием MathPlotLib

from matplotlib import pyplot as plt

# wine['Alcalinity_of_ash'].plot(kind='hist', bins=20, title='Гистограмма Вин - Matplotlib')
# plt.gca().spines[['top', 'right',]].set_visible(True)

plt.figure(figsize=(10, 6))
for cls in wine['class'].unique():
    subset = wine[wine['class'] == cls]
    plt.hist(subset['Alcohol'], alpha=0.5, bins=10, label=str(cls) +' class')

plt.title('Гистограмма Вин - MathPlotLib')
plt.xlabel('Крепость вина в градусах')
plt.ylabel('Частота повторений')
plt.legend()
plt.grid(True)
plt.show()