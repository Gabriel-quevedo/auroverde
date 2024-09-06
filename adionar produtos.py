import sqlite3
import tkinter as tk
from tkinter import messagebox
from flask import Flask, render_template, request

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('produtos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Função para criar a tabela 'produtos' se não existir
def criar_tabela_produtos():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            valor REAL,
            categoria TEXT,
            imagem TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar o produto ao banco de dados
def adicionar_produto_bd(nome, descricao, valor, categoria, imagem):
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO produtos (nome, descricao, valor, categoria, imagem)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, descricao, valor, categoria, imagem))
    conn.commit()
    conn.close()

# Função para mostrar uma janela gráfica (Tkinter) e inserir dados
def mostrar_janela_cadastro():
    def adicionar_produto():
        nome = entry_nome.get()
        descricao = entry_descricao.get()
        valor = entry_valor.get()
        categoria = entry_categoria.get()
        imagem = entry_imagem.get()

        if nome and valor and categoria:
            try:
                valor = float(valor)
                adicionar_produto_bd(nome, descricao, valor, categoria, imagem)
                messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
                janela.destroy()  # Fecha a janela após adicionar o produto
            except ValueError:
                messagebox.showerror("Erro", "O valor deve ser numérico.")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")

    # Cria uma nova janela para o formulário
    janela = tk.Tk()
    janela.title("Cadastro de Produto")

    # Rótulos e campos de entrada
    tk.Label(janela, text="Nome").grid(row=0, column=0)
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela, text="Descrição").grid(row=1, column=0)
    entry_descricao = tk.Entry(janela)
    entry_descricao.grid(row=1, column=1)

    tk.Label(janela, text="Valor").grid(row=2, column=0)
    entry_valor = tk.Entry(janela)
    entry_valor.grid(row=2, column=1)

    tk.Label(janela, text="Categoria").grid(row=3, column=0)
    entry_categoria = tk.Entry(janela)
    entry_categoria.grid(row=3, column=1)

    tk.Label(janela, text="Imagem (URL)").grid(row=4, column=0)
    entry_imagem = tk.Entry(janela)
    entry_imagem.grid(row=4, column=1)

    # Botão para adicionar produto
    tk.Button(janela, text="Adicionar Produto", command=adicionar_produto).grid(row=5, column=1)

    janela.mainloop()

# Configuração do Flask para adicionar produtos via interface web
app = Flask(__name__)

# Rota para exibir o formulário de adicionar produto
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_produto_web():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = float(request.form['valor'])
        categoria = request.form['categoria']
        imagem = request.form['imagem']
        
        adicionar_produto_bd(nome, descricao, valor, categoria, imagem)
        return 'Produto adicionado com sucesso!'
    
    return render_template('adicionar.html')

# Função principal para rodar tanto a janela gráfica quanto o Flask
if __name__ == '__main__':
    # Criar tabela no banco de dados se não existir
    criar_tabela_produtos()

    # Opção 1: Janela gráfica para inserir produto
    mostrar_janela_cadastro()

    # Opção 2: Servidor Flask para acessar via web
    app.run(debug=True)
