# Imagem base para construção
FROM python:3.12.1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia todos os arquivos para dentro do container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define a variável de ambiente para o Flask
ENV FLASK_APP=app.py

# Expõe a porta 5000 do contêiner
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
