import sqlite3

conn = sqlite3.connect("residuo.db")
cursor = conn.cursor()

cursor.execute("""
create table if not exists residuo(
        itiporesiduo               INTEGER         NOT NULL PRIMARY KEY AUTOINCREMENT,
        tiporesiduo                NVARCHAR(30)      NOT NULL,
        config                     TEXT
)
""")

print("coletor de residuo")
p_tiporesiduo = input('Tipo de residuo: ')
p_config = input('Config: ')


cursor.execute("""
INSERT INTO residuo (tiporesiduo, config)
VALUES (?,?)
""", (p_tiporesiduo, p_config))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
