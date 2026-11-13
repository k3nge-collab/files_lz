import docx  # для работы с документом
from collections import Counter
import matplotlib.pyplot as plt  # для построения графика
l = docx.Document('lion.docx')
d = docx.Document()  # файл для вывода таблицы
t = []
a = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
     'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']  # строчные буквы для фильтрации
b = d.add_table(rows=1, cols=3)
b.style = 'Table Grid'  # стиль таблицы
h = b.rows[0].cells
h[0].text = 'Слово'  # заголовки таблицы
h[1].text = 'Частота встречи, раз'
h[2].text = 'Частота встречи, %'
t = '\n'.join([p.text for p in l.paragraphs])  # извлекаем текст из документа
u = t.lower()
w = u.split()  # разбиваем на отдельные слова
f = [
    x.strip(" ,.!?()[]{}'\"-_@")
    for x in w
    if len(x) > 0 and all(c in a for c in x.strip(" ,.!?()[]{}'\"-_@"))  # фильтруем слова и знаки препинания
]
k = Counter(f)
n = len(f)  # общее количество слов
for x, c in k.items():
    p = (c / n) * 100  # частота в процентах
    r = b.add_row()
    r.cells[0].text = x  # заполняем ячейки таблицы
    r.cells[1].text = str(c)
    r.cells[2].text = str(p)
d.save('table.docx')  # сохраняем файл с таблицей
g = ''.join(filter(lambda x: 'а' <= x <= 'я', t.lower()))
m = Counter(g)  # считаем количество каждой буквы
s = sorted(m.keys())
v = [m[x] for x in s]  # сортируем буквы по алфавиту
plt.figure(figsize=(12, 6))
plt.bar(s, v, color='skyblue')  # строим столбчатую гистограмму
plt.xlabel('Буквы')
plt.ylabel('Количество')  # подписи осей
plt.title('Количество строчных русских букв в тексте')
plt.grid(axis='y')  # сетка для удобства чтения
plt.tight_layout()
plt.show()  # отображаем график