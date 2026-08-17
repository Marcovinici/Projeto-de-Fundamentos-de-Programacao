import json
import os
from usuario import *
from menus.menus_e_submenus import menu

while True:
    # Sequencia de execução para realizar o login e cadastro de usuários
    usuario, senha = tela_de_login()
    # Retorna True ou False 
    verificar_usuario(usuario, senha)
    # Verifica se o usuário existe e, caso não exista, oferece a opção de cadastrar um novo usuário
    cadastrar_ou_tentar_novamente(usuario, senha)
    # Leva ao menu principal caso o usuário seja encontrado e a senha esteja correta.
    menu(usuario)
