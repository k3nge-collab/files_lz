import matplotlib.pyplot as plt
import pandas as pd
p = 'titanic.parquet'  # Путь к исходному файлу
with open(p):  # Проверка наличия файла встроенными средствами Python
    d = pd.read_parquet(p)  # Чтение файла parquet
c = p.replace('.parquet', '.csv')
d.to_csv(c, index=False, encoding='utf-8')  # Сохранение в формат CSV
f = pd.read_csv(c)  # Чтение созданного CSV для проверки
f.columns = f.columns.str.lower()
s = (f.groupby(['pclass', 'survived']).size().unstack(fill_value=0))  # Группировка по классу и выживаемости
s.rename(columns={0: 'Погибли', 1: 'Выжили'}, inplace=True)
a = s.plot(kind='bar',figsize=(9, 6),color=['#d9534f', '#5cb85c'],edgecolor='black',rot=0,)  # Построение гистограммы
plt.title('Выживаемость пассажиров Титаника в зависимости от класса билета',fontsize=14,)
plt.xlabel('Класс билета (Pclass)', fontsize=12)
plt.ylabel('Количество пассажиров', fontsize=12)
plt.legend(title='Статус')
plt.grid(axis='y', linestyle='--', alpha=0.6)
for i in a.containers:
    a.bar_label(i, padding=3)  # Подписи значений над столбцами
plt.tight_layout()
plt.show()  # Отображение графика