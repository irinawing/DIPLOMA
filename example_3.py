import plotly.graph_objects as go

# Пример использоавния библиотеки Plotly
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 4, 9, 16, 25], mode='markers'))
fig.update_layout(title='Диаграмма рассеяния (Plotly)', xaxis_title='X', yaxis_title='Y')
fig.show()