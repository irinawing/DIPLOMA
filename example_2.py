import seaborn as sns
import matplotlib.pyplot as plt

# Выбираем стиль в Seaborn
sns.set(style="darkgrid")
# Составляем массив
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Пример использоавния библиотеки Seaborn
sns.lineplot(x=x, y=y)
plt.title("Линейный график (Seaborn)")
plt.show()
