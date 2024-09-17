from flask import Flask, jsonify, request
import sqlite3, json


def allUsers(): #Lista de todos os usuários
    listaUsuarios = query("SELECT * FROM tbUsuario")
    return listaUsuarios

def usuario(id): #Retorna os dados de 1 usuario
    retornoUsuario = query(f"SELECT id, usuario, email, createdOn, status FROM tbUsuario WHERE id='{id}'")
    return retornoUsuario

def login(): #Realiza login com senha
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    query_login = f"SELECT * FROM tbUsuario WHERE usuario='{usuario}' and senha='{senha}'"
    print(query_login)
    retornoUsuario = query(f"{query_login}")
    return retornoUsuario

def update(atualizacao): #Atualizar usuario ja existente
    try:
        retorno="OK"
        dados_json = json.loads(str(atualizacao))
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
        print(resposta)
        
    except sqlite3.OperationalError as e:
        # Captura erros relacionados à operação do banco de dados (como tabela não encontrada)
        retorno=f"Erro operacional: {e}"
    except sqlite3.DatabaseError as e:
        # Captura erros gerais de banco de dados
        retorno=f"Erro de banco de dados: {e}"
    except Exception as e:
        # Captura qualquer outra exceção genérica
        retorno=f"Ocorreu um erro inesperado: {e}"
    return retorno
def delete():
    id = request.form.get('id')
    usuario = request.form.get('usuario')
    retorno = "Apagado com sucesso"
    if usuario!="" and id!="":
        query = f"DELETE FROM tbUsuario Where id={id} and usuario='{usuario}'"
        print(query)
        retorno = queryAddUpdate(query)
        if retorno=="":
            retorno="Apagado com sucesso"
        else:
            retorno=f"Problema ao Apagar: {retorno}"
    else:
        retorno = "Execução falhou"
    return retorno
def add():#Inserir um usuario novo
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    email = request.form.get('email')
    print(f"{usuario},{senha},{email}")
    resposta="Atualizado com sucesso"
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
    print(f"***********{resposta}")
    return resposta;
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
    rows = cursor.fetchall() #TODO dar um jeito de fazer esse retorno ser JSON
    # Exibe os dados
    print("Dados da tabela:")
    # for row in rows:
    #     print(row)
    return rows

    # Fecha a conexão com o banco de dados
    conn.close()
