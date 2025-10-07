import sqlite3

#EXERCÍCIO 1:
conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

#EXERCÍCIO 2:
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT           
)
""")

#EXERCÍCIO 3:
#cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ("João Batista", 17, "Godim33@gmail.com"))
#cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ("Maria Eduarda", 18, "Duda4034@gmail.com"))
#cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ("Ricardo Silva", 17, "RicardinhoSilva08@gmail.com"))

#EXERCÍCIO 4:
#cursor.execute('SELECT * FROM alunos')
#print(cursor.fetchall())

#EXERCÍCIO 5:
#cursor.execute('SELECT * FROM alunos WHERE id = 2')
#print(cursor.fetchall())

#EXERCÍCIO 6:
#cursor.execute('UPDATE alunos SET idade = "18" WHERE id = "3"')

#EXERCÍCIO 7:
#cursor.execute('DELETE FROM alunos WHERE id = "2" ')


conn.commit()
con.close()
