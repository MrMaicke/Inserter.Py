import sqlite3

conn = sqlite3.connect("coletorxresiduo.db")
cursor = conn.cursor()

cursor.execute("""
create table if not exists coletorxresiduo(
        icoletor                INTEGER         NOT NULL PRIMARY KEY AUTOINCREMENT,
        idresiduo               INTEGER,
        pontos                  INTEGER
)
""")

print("coletor de coletorxcliente")
p_idresiduo = input('idresiduo: ')
p_pontos = input('pontos: ')

cursor.execute("""
INSERT INTO coletorxresiduo (idresiduo, pontos)
VALUES (?,?)
""", (p_idresiduo, p_pontos))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
