arquivo = open("usuario.txt", "a")

def cadastrar():
    while True:
        usuario = str(input("usuário: "))
        senha = str(input("Senha: "))

        with open("usuario.txt", "r") as arquivo:
            for linha in arquivo:
                separador = linha.split(",")
                if usuario in separador:
                    print("Erro")
                    return(cadastrar)
        with open("usuario.txt", "a") as arquivo:
            arquivo.write(f"{usuario},{senha}\n")
