import sqlite3
import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

def make_name():
    sung = random.choice(fam_names)
    name = ''.join(random.sample(first_names, 2))

    return (sung + name, )

data = []
for _ in range(100):
    data.append(make_name())

conn = sqlite3.connect('C:/sqlite/test.db')

with conn:
    curr = conn.cursor()
    sql = 'insert into Student (name) values (?)'
    curr.executemany(sql, data)

    conn.commit()