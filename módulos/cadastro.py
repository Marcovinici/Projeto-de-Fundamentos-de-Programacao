# Nesse código ocorrerá o cadastro do usuário no sistema. O mesmo deverá fornecer um nome de usuário e criar uma senha.
#Cadastro

# Esse script:
#Será responsável por controlar o cadastro de usuários

# Estratégia:
#:Usando o json como sistema de banco de dados esse script:
#lê o json, grava os usuários, verifica duplicatas e coordena o cadastro

# Miguel Macedo Ferreira
# 12/08/2026

#------------------------
#info importante:
#Falta tetsar a integração com o resto das coisas
#A cópia que eu fiz para teste local funcionou normalmente
#===============================================================================================
# imports
#--------------------------------
import json
import os

#=====================================================
#Funções para carregar os usuários existentes
#=====================================================

def carregar_usuarios(arquivo="usuarios.json"):
    if not os.path.exists(arquivo):
        return []
     #verifica se o arquivo .json existe
    try:
        with open(arquivo, "r", encoding="utf-8") as arquivo_json:
            return json.load(arquivo_json)
    except json.JSONDecodeError:
        return []

#=====================================================
#Função para salvar usuários 
#=====================================================

def salvar_usuarios(usuarios, arquivo="usuarios.json"):
    with open(arquivo, "w", encoding="utf-8") as arquivo_json:
        json.dump(usuarios, arquivo_json, indent=4, ensure_ascii=False)

#=====================================================
#Função para evitar duplicatas
#=====================================================

def usuario_existe(usuarios, nome_usuario):
    for usuario in usuarios:
        if usuario["nome_usuario"] == nome_usuario:
            return True

    return False

#=====================================================
#Função para solicitar dados
#=====================================================

def cadastrar_usuario():
    usuarios = carregar_usuarios()
    #Faz o cadastro 
    print("\n=== CADASTRO DE USUÁRIO ===")

    nome_usuario = input("Nome de usuário: ").strip()
    senha = input("Senha: ").strip()

    #Evita erros de nome
    if nome_usuario == "":
        print("O nome de usuário não pode ficar vazio.")
        return False
    
    #evita erros de senha
    if senha == "":
        print("A senha não pode ficar vazia.")
        return False

    #Se o usuário existe ele não registra
    if usuario_existe(usuarios, nome_usuario):
        print("Esse nome de usuário já está cadastrado.")
        return False

    #Adiciona novo usuário a lista
    novo_usuario = {
        "nome_usuario": nome_usuario,
        "senha": senha
    }
    
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)

    print("Usuário cadastrado com sucesso!")
    return True
