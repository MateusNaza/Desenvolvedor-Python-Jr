# Desenvolvedor-Python-Jr

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
    
1. Acesse a pasta '2. Data Analysis' atravéz do comando: ```bash cd 2.\ Data\ Analysis/```
2. Instale as dependências: ```bash pip install -r requirements ```
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
    
1. Acesse a pasta '3. Web Framework' atravéz do comando: ```bash cd 3.\ Web\ Frameworks/```
2. Instale as dependências: ```bash pip install -r requirements ```
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
    
    

