# Use uma imagem oficial de Python como base
FROM python:3.8-slim-buster

# Define o diretório de trabalho
WORKDIR /app

# Define as variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala as dependências do PostgreSQL
RUN apt-get update \
  && apt-get install -y postgresql gcc \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Atualiza o pip
RUN pip install --upgrade pip

# Copia o arquivo de requerimentos e instala as dependências
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copia o projeto
COPY . /app
