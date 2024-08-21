# frontend
FROM node:14-alpine AS build

WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# backend
FROM python:3.9-slim
WORKDIR /app
COPY backend/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ /app/backend/
COPY --from=build /app/build /app/build
ENV FLASK_APP=backend/app.py
EXPOSE 5000


CMD ["python", "backend/app.py"]
