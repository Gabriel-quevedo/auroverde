from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('produtos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Função para criar a tabela produtos, se não existir
def criar_tabela_produtos():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            imagem TEXT,
            categoria TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('test.html')

# Rota para adicionar novos produtos
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = request.form['valor']
        imagem = request.form['imagem']
        categoria = request.form['categoria']
        
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO produtos (nome, descricao, valor, imagem, categoria) VALUES (?, ?, ?, ?, ?)', 
            (nome, descricao, valor, imagem, categoria)
        )
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('adicionar.html')

# Rota para exibir produtos de uma categoria específica
@app.route('/<categoria>')
def exibir_produtos(categoria):
    if categoria not in ['Rosto', 'Cabelo', 'Pele', 'todas']:
        return "Categoria não encontrada", 404
    
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produtos WHERE categoria = ?', (categoria,)).fetchall()
    conn.close()
    
    # Renderiza o template da categoria específica
    return render_template(f'{categoria}.html', produtos=produtos, categoria=categoria)

# Rota para exibir todos os produtos
@app.route('/todas')
def exibir_todos_produtos():
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produtos').fetchall()
    conn.close()
    return render_template('todas.html', produtos=produtos)

# Rota para exibir os detalhes de um produto específico
@app.route('/produto/<int:id>')
def ver_produto(id):
    conn = get_db_connection()
    produto = conn.execute('SELECT * FROM produtos WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('produto_detalhes.html', produto=produto)

if __name__ == '__main__':
    criar_tabela_produtos()  # Garantir que a tabela seja criada ao iniciar o servidor
    app.run(debug=True)
