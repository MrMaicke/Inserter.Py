import sqlite3

conn = sqlite3.connect("ecoloop.db")
cursor = conn.cursor()

cursor.execute("""
create table if not exists coletor (
        idcoletor               INTEGER         NOT NULL PRIMARY KEY AUTOINCREMENT,
        idcliente               INTEGER         NOT NULL,
        codigo                  VARCHAR(20)     NOT NULL,
        senha                   VARCHAR(10)     NOT NULL,
        localizacao             VARCHAR(100)    NOT NULL,
        coordenadas             VARCHAR(100)    NOT NULL,
        config                  TEXT            NOT NULL,
        redewifi                TEXT,
        rede4g                  TEXT,
        notas                   TEXT,
        datacadastro            DateTime,
        dataatualizacao         DateTime
)
""")

print("coletor de coletor")
idcliente = input('idCliente: ')
codigo = input('Codigo: ')
senha = input('Senha: ')
localizacao = input('Localizacao: ')
coordenadas = input('Coordenadas: ')
config = input('Config: ')
redewifi = input('redeWiFi: ')
rede4g = input('rede4G: ')
notas = input('Notas: ')
datacadastro = input('DataCadastro: ')
dataatualizacao = input('DataAtualizacao: ')

cursor.execute("""
INSERT INTO coletor (idcliente, codigo, senha, localizacao, coordenadas, config, redewifi, rede4g, notas, datacadastro, dataatualizacao)
VALUES (?,?,?,?,?,?,?,?,?,?,?)
""", (idcliente, codigo, senha, localizacao, coordenadas, config, redewifi, rede4g, notas, datacadastro, dataatualizacao))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
