import sqlite3

conn = sqlite3.connect("ecoloop.db")
cursor = conn.cursor()

cursor.execute("""
create table if not exists movimento (
        idmovimento     INTEGER     NOT NULL PRIMARY KEY AUTOINCREMENT,
        idcoletor       INTEGER     NOT NULL,
        cpf             VARCHAR(11) NOT NULL,
        datahora        datetime    NOT NULL,
        idresiduo       integer     not null,
        pontos          integer     not null,
        idlocal         integer     not null,
        transacao       TEXT,
        status          TEXT
)
""")

print("coletor de movimento")
idcoletor = input('idColetor: ')
cpf = input('CPF: ')
datahora = input('DataHora: ')
idresiduo = input('idResiduo: ')
pontos = input('Pontos: ')
idlocal = input('idLocal: ')
transacao = input('Transação: ')
status = input('Status: ')

cursor.execute("""
INSERT INTO movimento (idcoletor, cpf, datahora, idresiduo, pontos, idlocal, transacao, status)
VALUES (?,?,?,?,?,?,?,?)
""", (idcoletor, cpf, datahora, idresiduo, pontos, idlocal, transacao, status))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
