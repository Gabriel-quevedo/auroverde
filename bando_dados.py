import sqlite3

# Conectar ao banco de dados (ou criar um novo, se não existir)
conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

# Criar a tabela de produtos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        codigo INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        imagem TEXT NOT NULL
    )
''')

# Inserir alguns dados de exemplo
cursor.execute('''
    INSERT INTO produtos (codigo, nome, descricao, valor, imagem)
    VALUES (1, 'Produto Rosto 1', 'Descrição do Produto Rosto 1', 10.00, 'produto_rosto1.jpg')
''')
cursor.execute('''
    INSERT INTO produtos (codigo, nome, descricao, valor, imagem)
    VALUES (2, 'Creme de cabelo, 'Descrição do Creme de cabelo', 15.00, 'Creme de cabelo.jpg')
''')
cursor.execute('''
    INSERT INTO produtos (codigo, nome, descricao, valor, imagem)
    VALUES (3, 'Produto Rosto 3', 'Descrição do Produto Rosto 3', 20.00, 'produto_rosto3.jpg')
''')

# Salvar as mudanças e fechar a conexão
conn.commit()
conn.close()
