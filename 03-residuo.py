from sqllib import *

sqlExecute("""
create table if not exists residuo (
        idresiduo               INTEGER         NOT NULL PRIMARY KEY AUTOINCREMENT,
        idtiporesiduo           INTEGER         NOT NULL,
        residuo                 ARCHAR(50)      NOT NULL,
        descricao               TEXT            NOT NULL,
        label                   VARCHAR(50)     NOT NULL,
        tamanho                 VARCHAR(50)     NOT NULL,
        pontos                  INTEGER         NOT NULL,
        valor                   DECIMAL(11,2),
        config                  TEXT,
        datacadastro            DateTime,
        dataatualizacao         DateTime
)
""")

print("Informe os dados do coletor de residuo:\n")
p_idtiporesiduo = input('idTipo Residuo: ')
p_residuo = input('Residuo: ')
p_descricao = input('Descrição: ')
p_label = input('Label: ')
p_tamanho = input('Tamanho: ')
p_pontos = input('Pontos: ')
p_valor = input('Valor: ')
p_config = input('Config: ')
#p_datacadastro = input('Data Cadastro: ')
#p_dataatualizacao = input('Data Atualização: ')
# see: https://www.sqlitetutorial.net/sqlite-date-functions/sqlite-date-function/
sqlExecute("""
INSERT INTO residuo (idtiporesiduo, residuo, descricao, label, tamanho, pontos, valor, config, datacadastro, dataatualizacao)
VALUES (?,?,?,?,?,?,?,?,DATE('now'),DATETIME('now','localtime'))
""", (p_idtiporesiduo, p_residuo, p_descricao, p_label, p_tamanho, p_pontos, p_valor, p_config))

print('\nDados inseridos com sucesso.\nListando todos os dados')

dados = sqlSelect("""
SELECT * FROM residuo;
""")

for linha in dados:
    print(linha)
