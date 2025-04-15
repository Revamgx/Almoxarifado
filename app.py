from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            local TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    local = request.form['local']
    
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO produtos (nome, quantidade, local) VALUES (?, ?, ?)', (nome, quantidade, local))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
