from flask import Flask, jsonify, request
import sqlite3, json
app = Flask(__name__)

#MOSTRAR TODOS OS USUARIOS
@app.route('/api/usuario/list', methods=['GET'])
def allUsers():
    listaUsuarios = query("SELECT * FROM tbUsuario")
    return jsonify(message=listaUsuarios)
#MOSTRAR DADOS DO USURIO POR ID
@app.route('/api/usuario', methods=['GET'])
def usuario():
    id = request.args[('id')]
    retornoUsuario = query(f"SELECT * FROM tbUsuario WHERE id='{id}'")
    return jsonify(message=f"TESTE->{retornoUsuario[0][3]}")

@app.route('/api/usuario/login', methods=['POST'])
def login():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    retornoUsuario = query(f"SELECT * FROM tbUsuario WHERE usuario='{usuario}' and senha='{senha}'")
    return jsonify(message=f"{retornoUsuario}")

#ATUALIZAR USUARIO JA EXISTENTE
@app.route('/api/usuario/update', methods=['POST'])
def update():
    retorno=""
    atualizacao = request.form.get('update')
    #print(atualizacao)
    dados_json = json.loads(str(atualizacao))
    #print(dados_json['id'])

    id = dados_json['id']
    usuario = dados_json['usuario']
    senha = dados_json['senha']
    email = dados_json['email']
    status= dados_json['status']

    if id!="" and usuario!="" and senha!="" and email!="" and status!="":
        query = f"UPDATE tbUsuario set senha='{senha}', email='{email}', status='{status}' WHERE id={id}"
        print(query)
        resposta = queryAddUpdate(query)
        if resposta=="":
            resposta="Atualizado com sucesso"
        else:
            resposta=f"Problema na inserção: {resposta}"
    else:
        resposta = "Execução falhou"

    return jsonify(message=f"{retorno}")


@app.route('/api/usuario/add', methods=['POST'])
#INSERIR UM USUARIO NOVO
def add():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    email = request.form.get('email')
    print(f"{usuario},{senha},{email}")
    resposta=""
    if usuario!="" and senha!="" and email!="":
        query = f"INSERT INTO tbUsuario (usuario, senha, email, status) VALUES \
                ('{usuario}', '{senha}', '{email}',1)"
        print(query)
        resposta = queryAddUpdate(query)
        if resposta=="":
            resposta="Inserido com sucesso"
        else:
            resposta=f"Problema na inserção: {resposta}"
    else:
        resposta = "Execução falhou"
    return jsonify(message=f"{resposta}")
def queryAddUpdate(query):
    mensagemFinal = ""
    try:
        # Conecta ao banco de dados SQLite
        conn = sqlite3.connect("C:\Rafson\projetos\inventario\inventario01.db")

        # Cria um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Executa uma consulta SQL para selecionar todos os dados da tabela tbUsuario
        cursor.execute(query)
        conn.commit()
        conn.close()
    except sqlite3.OperationalError as e:
        # Captura erros relacionados à operação do banco de dados (como tabela não encontrada)
        mensagemFinal=f"Erro operacional: {e}"
    except sqlite3.DatabaseError as e:
        # Captura erros gerais de banco de dados
        mensagemFinal=f"Erro de banco de dados: {e}"
    except Exception as e:
        # Captura qualquer outra exceção genérica
        mensagemFinal=f"Ocorreu um erro inesperado: {e}"

    finally:
        print(mensagemFinal)
        return mensagemFinal
def query(query):
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect("C:\Rafson\projetos\inventario\inventario01.db")

    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Executa uma consulta SQL para selecionar todos os dados da tabela tbUsuario
    cursor.execute(query)

    # Recupera todos os resultados da consulta
    rows = cursor.fetchall()

    # Exibe os dados
    print("Dados da tabela:")
    # for row in rows:
    #     print(row)
    return rows

    # Fecha a conexão com o banco de dados
    conn.close()
if __name__ == '__main__':
    app.run(debug=True)