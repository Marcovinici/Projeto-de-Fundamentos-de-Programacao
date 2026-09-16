# MobCLI System

## Descrição do projeto
Projeto final para a disciplina de Fundamentos de Programação. Se trata de um sistema CLI destinado a usuários e administradores de rotas de mobilidade urbana.

## Equipe
- Alysson Davi Sampaio Silva
- Arthur Barros de Sá
- Edson Oliveira Santos
- Kauê Aparecido de Oliveira Silva
- Marcos Vinicius Tavares Batista
- Miguel Macedo Ferreira
- Tadeu Coêlho de Vasconcelos

## Problemas a serem resolvidos
- Ausência de um mapa que permita ao usuário se situar na cidade
- Ausência de um algoritmo que calcule a rota mais curta entre dois pontos informados
- Impossibilidade de acessar o histórico de rotas pesquisadas ou de rotas marcadas como favoritas
- Administrador não consegue ter um panorama de uso dos usuários porque não tem acesso a relatórios

## Funcionalidades
As funcionalidades exibidas abaixo não necessariamente são acessíveis diretamente ao usuário ou administrador, mas por certo estão acontecendo em segundo plano:
- [ ] Exibir interface que permita fazer cadastro ou login
- [ ] Salvar cadastro de usuários em um banco de dados
- [ ] Efetuar login como usuário ou administrador
- [ ] Verificar se um usuário já existe ao fazer login ou cadastro
- [ ] Sugerir cadastro ou nova tentativa em caso de falha no login
- [ ] Exibir um menu principal de opções após o login
- [ ] Permitir navegação entre menus e submenus, quando houver
- [ ] Exibir o mapa através do menu
- [ ] Calcular o caminho mais curto a partir da origem e destino informados
- [ ] Exibir o trajeto da rota no mapa
- [ ] Exibir a descrição de uma rota informada
- [ ] Salvar o histórico de rotas e rotas favoritas do usuário
- [ ] Exibir informações sobre o usuário logado
- [ ] Exibir relatório de uso (para administradores)
- [ ] Encerrar sessão (sair)

## Instruções de execução

#### Criando Venv

A criação de um ambiente virtual (virtual enviroment) é uma boa prática que evita que haja conflitos entre dependências do programa com as já existentes no sistema.

No terminal digite: 

```bash
python -m venv venv
```
O comando acima cria um ambiente virtual com nome "venv"

Depois ative o venv com:
```bash
source venv/bin/activate
```
No Linux

Ou, para Windows:
```powershell
venv\Script\activate 
```

#### Instalando Dependências

Com o venv criado, instale as bibliotecas necessárias para o funcionamento do programa com:
```bash
pip install -r requirements.txt
```

#### Executando o programa

Por fim, para iniciar o programa, execute o main:
```bash
python -m main
```
