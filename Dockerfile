FROM node:14-alpine AS build

WORKDIR /app

COPY app/package*.json ./

RUN npm install

COPY app/ ./

RUN npm run build

FROM python:3.9-slim

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ . 

COPY --from=build /app/build /app
COPY --from=build /app/build/index.html /app/templates/index.html

ENV FLASK_APP=app/app.py

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "app/app.py"]
