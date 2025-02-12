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
```