arquivo = open("banco_dados.txt", "a")

def cadastrar():
    while True:
        usuario = str(input("usuário: "))
        senha = str(input("Senha: "))

        with open("banco_dados.txt", "r") as arquivo:
            for linha in arquivo:
                separador = linha.split(",")
                if usuario in separador:
                    print("Erro")
                    return(cadastrar)
        with open("banco_dados.txt", "a") as arquivo:
            arquivo.write(f"{usuario},{senha}\n")
