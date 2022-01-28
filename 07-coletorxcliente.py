import sqlite3

conn = sqlite3.connect("coletorxcliente.db")
cursor = conn.cursor()

cursor.execute("""
create table if not exists coletorxcliente(
        idcoletor               INTEGER         NOT NULL,
        idcliente              INTEGER         NOT NULL
)
""")

print("coletor de coletorxcliente")
p_idcoletor = input('id coletor: ')
p_idcliente = input('id cliente: ')

cursor.execute("""
INSERT INTO coletorxcliente (idcoletor, idcliente)
VALUES (?,?)
""", (p_idcoletor, p_idcliente))

conn.commit()

print('Dado inserido com sucesso.')

conn.close()
