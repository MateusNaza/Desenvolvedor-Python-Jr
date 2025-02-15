# Desenvolvedor-Python-Jr

# Índice

1. [Preparação de ambiente](#preparação-de-ambiente)    
2. [Data Analysis](#2-data-analysis)
   - [Detalhes do código](#detalhes-do-código)
   - [Como executar o código](#como-executar-o-código)
3. [Web Framework](#3-web-framework)
   - [Detalhes do código](#detalhes-do-código-1)
   - [Como executar o app](#execução-do-app)
4. [Asynchronous Programming](#4-asynchronous-programming)
   - [Detalhes do código](#detalhes-do-código-2)
   - [Como executar o código](#como-executar-o-código-1)
6. [Containerization](#6-containerization)
   - [Detalhes do Desenvolvimento](#detalhes-do-desenvolvimento)
   - [Como executar o código](#como-executar-o-código-2)

---
# Preparação de ambiente       
    
Para preparar o ambiente escolhi por usar o ambiente virtual do python (venv), sendo assim, consigo ter um ambiente de desenvolvimento desacoplado para instalar as dependências necessárias. Abaixo seguem comandos que efeutei no terminal para preparar esse ambiente:    
    
```bash
# Detalhe importante!! Criei esse ambiente na pasta raiz do repositório
# Cria um novo ambiente venv dentro de uma pasta chamada ".venv"
python -m venv .venv

# Inicia o ambiente
source .venv/bin/activate

# Instala as bibliotecas necessárias
pip install flask pandas asyncio

# Cria um arquivo requirements.txt com todas as bibliotecas e dependências que tenho instaladas no meu ambiente
pip freeze > requirements.txt
```

# 2. Data Analysis
    
## Detalhes do código    
    
Para efetuar as análises nos dados de venda eu utilizei a biblioteca pandas e segui os seguintes passos:    
    
- Criei meu arquivo '.csv' com dados de vendas de produtos hospitalares, seguindo a estrutura de colunas proposta no exercício.    
- Li o arquivo de vendas e salvei dentro de um _Dataframe_ chamado 'vendas'.    
- Criei uma nova coluna 'total' que basicamente multiplica a 'quantidade' pelo 'valor_unitario'.    
- Calculei o faturamento por produto agrupando o _Dataframe_ por produto e somando os valores da coluna 'total'.    
- Para encontrar o produto de maior e menor faturamento eu utilizei respectivamente as funções _idxmax_ e _idxmin_, juntamente com a função _loc_.    
    
## Como executar o código    
    
1. Estando na pasta raiz do repositório, instale as dependências: ```bash pip install -r requirements ```
2. Acesse a pasta '2. Data Analysis' atravéz do comando: ```bash cd 2.\ Data\ Analysis/```
3. Execute o script: ```bash python main.py ```
    

# 3. Web Framework    
         
## Detalhes do código       
     
No código eu sigo as seguintes estapas:    
    
- Importo de dentro da biblioteca flask classes e funções que utilizarei
- Inicio o meu app Flask
- Defino o primeiro Endpoint 'GET'
- Abixo do decorador crio uma função que retorna uma mensagem de saudação personalizada com o nome utilizado na URL
- Defino o segundo endpoint 'POST' e logo abaixo crio a função soma()
- Chamo a função de inicialização do meu app
    

## Execução do app

Para executar o app deve se seguir os seguintes passos:
    
1. Estando na pasta raiz do repositório, instale as dependências: ```bash pip install -r requirements ```
2. Acesse a pasta '3. Web Framework' atravéz do comando: ```bash cd 3.\ Web\ Frameworks/```
3. Inicie o app: ```bash python app.py ```
    
    
Agora você está com o app rodando na porta 5000, para acessá-lo atravéz da requisição GET basta:    
    
1. Colar essa URL em um navegador web, substituindo 'SeuNome' pelo seu nome: http://127.0.0.1:5000/saudacao?nome=SeuNome    
    
    
Já para a requisição POST, podemos acessar via POSTMAN, cURL, mas nesse projeto achei melhor criar um código python utilizando da biblioteca requests. Para efetuá-la:
    
1. Abra o arquivo nums_para_somar.py e substitua os números por os que você deseja somar (Opcional)
2. Abra um novo terminal, e, caso não esteja na pasta '3. Web Framework', acesse atravéz do comando: ```bash cd 3.\ Web\ Frameworks/```
3. Execute o Script de requisição: ```bash python requisicao_post.py ```
4. O resultado deve aparecer logo em seguida no terminal.
    

# 4. Asynchronous Programming
     
## Detalhes do código    
    
Para essa atividade utilizei a biblioteza _asyncio_ do python, criei uma função sincrona e uma assíncrona para verificar a diferença de performance. Abaixo segue o passo a passo:
    
- Criei uma função de chamada síncrona que utiliza o modulo _sleep_ da biblioteca _time_
- Para executar as três funões de chamada e medir o tempo de execução utilizei uma função *main_sync*
- Criei uma função assíncrona que utiliza o modulo _sleep_ porém dessa vez da biblioteca _asyncio_
- Para executar a função assíncrona três vezes e medir o tempo utilizei a função *main_async*
- Simulei uma das funções gastando 2 segundos de tempo de execução e as outras duas gastando 1 segundo de execução, fiz isso para os dois cenários.
    
>**Resultado:**    
>As funções síncronas levaram **4 segundos** para executar
>Já as funções assíncronas foram **2 segundos** de execução
>Ou seja, o tempo de execução caiu pela metade quando usamos as funções assíncronas
    
## Como executar o código    
    
1. Estando na pasta raiz do repositório, instale as dependências: ```bash pip install -r requirements ```
2. Acesse a pasta '4.\ Asynchronous\ Programming' atravéz do comando: ```bash cd 4.\ Asynchronous\ Programming```
3. Execute o script: ```bash python main.py ```
     
      
# 6. Containerization    
     
## Detalhes do desenvolvimento
     
Para containerizar minha aplicação, criei uma imagem _docker_ que reproduz meu ambiente de execução local dentro de um container. Após construir o _Dockerfile_ executei os seguintes passos:
     
1. Construí minha imagem: ```bash docker build -t app_flask .```
2. Verifiquei os dados dela: ```bash docker images```
3. Rodei um container para testar se estava funcionando como deveria: ```bash docker run -d --rm -p 5000:5000 app_flask```
       
>Resolvi também subir essa imagem para o Docker Hub, poise assim facilita o Deploy posteriormente.
     
4. Fiz o login no Docker Hub: ```bash docker login```
5. Em paralelo, criei um novo repositório no _Docker Hub_ ![repositório no docker hub](assets/dockerhub.png)
5. 'Tagueei' minha imagem: ```bash tag app_flask mateusnazahub/flask_app:latest```
6. Subi ela para o _Docker Hub_: ```bash push mateusnazahub/flask_app:latest```
     
## Como executar o código 
     
1. Acesse a pasta '6. Containerization' atravéz do comando: ```bash cd 6.\ Containerization```
2. Construa a imagem: ```bash docker build -t app_flask .```
3. Inicie um container a partir da imagem criada: ```bash docker run -d --rm -p 5000:5000 app_flask```

A partir desse momento o app estará rodando na porta 5000 do localhost, para acessá-lo basta:

1. Colar essa URL em um navegador web, substituindo 'SeuNome' pelo seu nome: http://127.0.0.1:5000/saudacao?nome=SeuNome


