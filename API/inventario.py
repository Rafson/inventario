import usuario
from flask import Flask, jsonify, request, json, Response

app = Flask(__name__)


### USUARIO
#LIST
@app.route('/api/usuario/list', methods=['GET'])
def user_list():
    retorno_listaUsuarios = usuario.allUsers()
    return jsonify(message=retorno_listaUsuarios)
#GET USUARIO
@app.route('/api/usuario', methods=['GET'])
def user_get():
    id = request.args[('id')]
    retorno_usuario = usuario.usuario(id)
    return jsonify(message=retorno_usuario)
#UPDATE
    #in Body select x-www-form-urlencoded
    #key:user
    #value:you_json
    # {
    #     "email": "usuario1@example.com",
    #     "id": 1,
    #     "senha": "senha1",
    #     "status": 1,
    #     "usuario": "usuario1"
    # }
@app.route('/api/usuario/update', methods=['POST'])
def usuario_update():
    atualizacao = request.form.get('update')
    retorno_atualizacao = usuario.update(atualizacao)
    print(f"************{retorno_atualizacao}")
    return jsonify(message=retorno_atualizacao)
#ADD
@app.route('/api/usuario/add', methods=['POST'])
def usuario_add():
    retorno_add = usuario.add()
    return jsonify(message=f"{retorno_add}")
#DELETE
@app.route('/api/usuario/delete', methods=['POST'])
def usuario_delete():
    print('DELETE')
    retorno_delete = usuario.delete()
    return jsonify(message=f"{retorno_delete}")
    
#LOGIN
@app.route('/api/usuario/login', methods=['POST'])
def usuario_login():
    print('LOGIN')
    retorno_login = usuario.login()
    return jsonify(retorno_login)
#ESQUECI A SENHA
    #NAO ACHEI UM ENVIO DE EMAIL GRATIS PARA TESTAR
@app.route('/app/usuario/esqueci_senha', methods=['POST'])
def esqueci_senha(): #TODO FALTA TERMINAR ESSE METODO
    print('Esqueci a senha')
    retorno = usuario.esqueci_senha()
    return jsonify(retorno)

#TROCAR A SENHA
@app.route('/app/usuario/troca_senha', methods=['POST'])
def troca_senha(senha_atual, repita_senha_atual, senha_nova):
    retorno = ""
    if(senha_atual==senha_nova):
        print('A senha pode ser trocada')
        retorno = usuario.troca_senha()
    else:
        print('Atuais e repetida são diferentes')

#TESTE
@app.route('/api/usuario/teste', methods=['GET'])
def usuario_teste():
    dados = {
            "nome": "João",
            "idade": 30,
            "cidade": "São Paulo",
            "habilidades": ["Python", "Flask", "SQL"]
        }
    return Response(json.dumps(dados), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)