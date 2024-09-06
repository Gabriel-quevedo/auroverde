import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('produtos.db')

# Criar um cursor
c = conn.cursor()

# Criar tabela
c.execute('''
    CREATE TABLE produtos (
        codigo INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        descricao TEXT,
        valor REAL NOT NULL,
        imagem TEXT,
        categoria TEXT NOT NULL
    )
''')

# Adicionar alguns produtos
produtos = [
    (1, 'Produto Rosto 1', 'Descrição do Produto Rosto 1', 10.00, 'produto_rosto1.jpg', 'rosto'),
    (2, 'Produto Rosto 2', 'Descrição do Produto Rosto 2', 15.00, 'produto_rosto2.jpg', 'rosto'),
    (3, 'Produto Corpo 1', 'Descrição do Produto Corpo 1', 20.00, 'produto_corpo1.jpg', 'corpo'),
    (4, 'Produto Cabelo 1', 'Descrição do Produto Cabelo 1', 25.00, 'produto_cabelo1.jpg', 'cabelo'),
    # Adicione mais produtos conforme necessário
]

c.executemany('''
    INSERT INTO produtos (codigo, nome, descricao, valor, imagem, categoria)
    VALUES (?, ?, ?, ?, ?, ?)
''', produtos)

# Salvar (commit) as mudanças
conn.commit()

# Fechar a conexão
conn.close()
