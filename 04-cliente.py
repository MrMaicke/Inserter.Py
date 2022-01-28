import sqlite3

conn = sqlite3.connect("cliente.db")
cursor = conn.cursor()

cursor.execute("""
create table if not exists cliente(
        icliente               INTEGER         NOT NULL PRIMARY KEY AUTOINCREMENT,
        cnpj                 VARCHAR(14)      NOT NULL,
        nome                 NVARCHAR(50)      NOT NULL,
        config                  TEXT,
        recebedoacao            Boolean,
        datacadastro            DateTime,
        dataatualizacao         DateTime
)
""")

print("coletor de cliente")
p_cnpj = input('CNPJ: ')
p_nome = input('Nome: ')
p_config = input('Config: ')
p_recebedoacao = input('Recebe Doação: ')
p_datacadastro = input('Data Cadastro: ')
p_dataatualizacao = input('Data Atualização: ')

cursor.execute("""
INSERT INTO cliente (cnpj, nome, config, recebedoacao, datacadastro, dataatualizacao)
VALUES (?,?,?,?,?,?)
""", (p_cnpj, p_nome, p_config, p_recebedoacao, p_datacadastro, p_dataatualizacao))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
