import sqlite3

conn = sqlite3.connect("ecoloop.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE informacoes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        localinstalacao TEXT NOT NULL,
        codigo INTEGER,
        senha     VARCHAR(11) NOT NULL,
        config TEXT NOT NULL,
        localizacao TEXT,
        wifi TEXT,
        notas VARCHAR(2) NOT NULL
)
""")

print("coletor")
p_localInstalacao = input('LocalInstalação: ')
p_codigo = input('Código: ')
p_senha = input('Senha: ')
p_config = input('Config: ')
p_localizacao = input('Localização: ')
p_wifi = input('WiFi: ')
p_notas = input('Notas: ')

# print("residuo")
# p_residuo = input('Residuo: ')
# p_descricao = input('Descrição: ')

# print("ColetorXResidou")
# p_coletor = input('Coletor: ')
# p_residuo = input('Residuo: ')

# print("local")
# p_nomefantasia = input('NomeFantasia: ')
# p_razaosocial = input('RazãoSocial: ')
# p_cnpj = input('CNPJ: ')
# p_endereco = input('Endereço: ')
# p_complemento = input('Complemento: ')
# p_bairro = input('Bairro: ')
# p_cidade = input('Cidade: ')
# p_estado = input('Estado: ')
# p_cep = input('Cep: ')
# p_localfaturamento = input('LocalFaturamento: ')
# p_coordenadas = input('Coordenadas: ')
# p_datacadastro = input('DataCadastro: ')
# p_dataatualizacao = input('DataAtualização: ')
# p_notas = input('Notas: ')

# print("contato")
# p_local = input('Local: ')
# p_nome = input('Nome: ')
# p_funcao = input('Função: ')
# p_telefone1 = input('Telefone1: ')
# p_telefone2 = input('Telefone2: ')
# p_email1 = input('email1: ')
# p_email2= input('email2: ')
# p_datacadastro = input('DataCadastro: ')
# p_dataatualizacao = input('DataAtualização: ')
# p_notas = input('Notas: ')

# print("Função")
# p_funcao = input('Função: ')

# print("instituição")
# p_localInstituicao = input('LocalInstalação: ')
# p_nome = input('Nome: ')
# p_conf = input('Config: ')
# p_datacadastro = input('DataCadastro: ')
# p_dataatualizacao = input('DataAtualização: ')

# print("movimentacao")
# p_coletor = input('Coletor: ')
# p_datahora = input('DataHora: ')
# p_residuo = input('Residuo: ')
# p_quantidade = input('Quantidade: ')
# p_instituicao = input('Instituição: ')

# print("fidelidade")
# p_coletor = input('Coletor: ')
# p_datahora = input('DataHora: ')
# p_residuo = input('Residuo: ')
# p_cpf = input('CPF: ')
# p_quantidade = input('Quantidade: ')
# p_transacao = input('Transação: ')
# p_status = input('Status: ')

cursor.execute("""
INSERT INTO informacoes (localinstalacao, codigo, senha, Config, Localizacao, WiFi, Notas)
VALUES (?,?,?,?,?,?,?)
""", (p_localInstalacao, p_codigo, p_senha, p_config, p_localizacao, p_wifi, p_notas ))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()

2
2