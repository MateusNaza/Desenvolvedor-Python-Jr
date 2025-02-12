# Desenvolvedor-Python-Jr
    
## 3. Web Framework    
    
### Preparação de ambiente    
    
Para preparar o ambiente escolhi por usar o ambiente virtual do python (venv), sendo assim, consigo ter um ambiente de desenvolvimento desacoplado para instalar as dependências necessárias. Abaixo seguem comandos que efeutei no terminal para preparar esse ambiente:    
    
```bash
# Detalhe importante!! Criei esse ambiente na pasta raiz do repositório
# Cria um novo ambiente venv dentro de uma pasta chamada ".venv"
python -m venv .venv

# Inicia o ambiente
source .venv/bin/activate

# Instala a biblioteca necessária
pip install flask

# Cria um arquivo requirements.txt com todas as bibliotecas e dependências que tenho instaladas no meu ambiente
pip freeze > requirements.txt
```    
    

### Detalhes do código    
No código eu sigo as seguintes estapas:    
    
- Importo de dentro da biblioteca flask classes e funções que utilizarei
- Inicio o meu app Flask
- Defino o primeiro Endpoint 'GET'
- Abixo do decorador crio uma função que retorna uma mensagem de saudação personalizada com o nome utilizado na URL
- Defino o segundo endpoint 'POST' e logo abaixo crio a função soma()
- Chamo a função de inicialização do meu app
    

### Execução do app

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


