# Etapa 1: Construir o frontend
FROM node:14 AS build

WORKDIR /app

# Copiar arquivos do frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Etapa 2: Configurar o backend com Flask
FROM python:3.9-slim

WORKDIR /app

# Copiar e instalar dependências do backend
COPY backend/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código do backend e build do frontend
COPY backend/ /app/backend/
COPY --from=build /app/build /app/build

# Tornar o entrypoint.sh executável
RUN chmod +x /app/backend/entrypoint.sh

# Expor a porta do Flask
EXPOSE 5000

# Definir o comando de entrada
ENTRYPOINT ["/app/backend/entrypoint.sh"]
